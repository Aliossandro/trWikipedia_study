from mw.xml_dump import Iterator
from mw.lib import reverts
# from mw.lib import persistence
# from pprint import pprint
# from mw.lib import sessions
import sys
import dbCreator

import bz2

def wikiParser(file_name):
    pageMetadata = []
    #create table
    dbCreator.create_table()
    # Construct dump file iterator
    counter = 0
    dump = Iterator.from_file(bz2.open(file_name))
    # dump = Iterator.from_file(open("/Users/alessandro/Documents/PhD/trWiki/trSample.xml"))

    # Iterate through pages
    pageAll = []

    for page in dump:
        if counter == 2500:
            conn = dbCreator.get_db_params()
            cur = conn.cursor()
            try:
                cur.executemany(
                    """INSERT INTO revision_metadata (bytes, namespace, page, par_Id, rev_Id, revert, reverted, time_Stamp, user_Id, user_Name) VALUES (%(bytes)s, %(namespace)s, %(page)s, %(parentId)s, %(revId)s, %(revert)s, %(reverted)s, %(time_stamp)s, %(userId)s, %(userName)s);""",
                    pageAll)
                conn.commit()
                # print('imported')
            except:
                conn.rollback()
                for stat in pageAll:
                    try:
                        cur.execute(
                            """INSERT INTO revision_metadata (bytes, namespace, page, par_Id, rev_Id, revert, reverted, time_Stamp, user_Id, user_Name) VALUES (%(bytes)s, %(namespace)s, %(page)s, %(parentId)s, %(revId)s, %(revert)s, %(reverted)s, %(time_stamp)s, %(userId)s, %(userName)s);""",
                            stat)
                        conn.commit()
                    except:
                        conn.rollback()
                        e = sys.exc_info()[0]
                        print("<p>Error: %s</p>" % e)
                        print('not imported, revision id error')
                        print(stat)
            pageAll = []
            counter = 0


        counter += 1
        checksum_revisions = []
        revertsList = []
        pageTitle = page.title.lower().replace(' ', '_')
        pageNS = page.namespace
        # state = persistence.State()

        # Iterate through a page's revisions
        for revision in page:
            revData = {}
            # print(revision.id, revision.contributor, revision.timestamp)
            revData['page'] = pageTitle
            revData['namespace'] = pageNS
            revData['bytes'] = revision.bytes
            revData['revId'] = revision.id
            revData['parentId'] = revision.parent_id
            revData['time_stamp'] = revision.timestamp.long_format().replace('T', ' ').replace('Z', ' ')
            if revision.contributor.id == None:
                revData['userId'] = 'ip'
            else:
                revData['userId'] = revision.contributor.id
            revData['userName'] = revision.contributor.user_text
            revData['revert'] = False
            revData['reverted'] = False

            pageMetadata.append(revData)
            checksum_revisions.append((revision.text, {"rev_id": revision.id}))
            # state.process(revision.text, revision=revision.id)

        # print(state.last)
        revertsList.append(list(reverts.detect(checksum_revisions)))
        # print(revertsList)
        for revvos in revertsList:
            for revvo in revvos:
                for revis in pageMetadata:
                    try:
                        if revis['revId'] == revvo.reverting['rev_id']:
                            revis['revert'] = True
                    except:
                        print(revvo)
                    for reverted in revvo.reverteds:
                        if revis['revId'] == reverted['rev_id']:
                            revis['reverted'] = True


        pageAll += pageMetadata
        pageMetadata = []

    conn = dbCreator.get_db_params()
    cur = conn.cursor()
    try:
        cur.executemany(
            """INSERT INTO revision_metadata (bytes, namespace, page, par_Id, rev_Id, revert, reverted, time_Stamp, user_Id, user_Name) VALUES (%(bytes)s, %(namespace)s, %(page)s, %(parentId)s, %(revId)s, %(revert)s, %(reverted)s, %(time_stamp)s, %(userId)s, %(userName)s);""",
            pageAll)
        conn.commit()
        # print('imported')
    except:
        conn.rollback()
        for stat in pageAll:
            try:
                cur.execute(
                    """INSERT INTO revision_metadata (bytes, namespace, page, par_Id, rev_Id, revert, reverted, time_Stamp, user_Id, user_Name) VALUES (%(bytes)s, %(namespace)s, %(page)s, %(parentId)s, %(revId)s, %(revert)s, %(reverted)s, %(time_stamp)s, %(userId)s, %(userName)s);""",
                    stat)
                conn.commit()
            except:
                conn.rollback()
                e = sys.exc_info()[0]
                print("<p>Error: %s</p>" % e)
                print('not imported, revision id error')
                print(stat)


def main():
    wikiParser(sys.argv[1])


if __name__ == "__main__":
    main()