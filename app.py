from flask import Flask
app=Flask(_name_)
@app.route("/")
def hellow():
  return "hello world from Jenkins CI/CD"
if_name_=="__main__":
  app.run(host="0.0.0.0",port=5000)
