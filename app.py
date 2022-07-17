from flask import Flask,render_template,request
import pyfiglet 
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def formInput():
  font_names=[]
  file1 = open('fonts.txt', 'r')
  Lines = file1.readlines()
  count = 0
  SubmitBtn = request.form.get('Submit')
# Strips the newline character
  for line in Lines:
    count += 1
    font_names.append(line.strip())
  if SubmitBtn == "clicked":
    return render_template('Index.html',data=font_names,Output = output())
  return render_template('Index.html',data=font_names)
  
  
#@app.route('/form',methods=['GET','POST'])
def output():
  UserName = request.form.get('user_input').strip()
  fontName = request.form.get('comp_select')
  if fontName == "-- Select --":
    awesome_output = pyfiglet.figlet_format(UserName)
  else:
    awesome_output = pyfiglet.figlet_format(UserName,font=str(fontName))
  return awesome_output

if __name__ == "__main__":
   app.run(debug=True)
  #row row-cols-lg-auto g-3 align-items-center