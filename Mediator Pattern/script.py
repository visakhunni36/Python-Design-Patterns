

# the python script

import mediator

reporter = mediator.Reporter()
db = mediator.DB()
tm = mediator.TestManager()
tm.setReporter(reporter)
tm.setDB(db)

reporter.setTM(tm)
db.setTM(tm)


# for the demo purpose, loop through the same test
# practically, there will be various unique tests and their objects
while(1):
  tc = mediator.TC()
  tc.setTM(tm)
  tm.setTC(tc)
  tc.setup()
  tc.execute()
  tc.tearDown()


































































