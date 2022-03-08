#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)               


# In[3]:



from flask import render_template, request
import joblib
    
@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "POST":
       
        purchases = request.form.get("purchases")
        suppcard = request.form.get("suppcard")
        purchases = float(purchases)
        suppcard = float(suppcard)
        print(purchases, suppcard)

        model1 = joblib.load("CCU_DT")
        pred1 = model1.predict([[purchases,suppcard]])
        s1 = "Upgrade = 1, No Upgrade = 0 ---> " + str(pred1[0])
        
        model2 = joblib.load("CCU_Reg")
        pred2 = model2.predict([[purchases,suppcard]])
        s2 = "Upgrade = 1, No Upgrade = 0 ---> " + str(pred2[0])
        
        model3 = joblib.load("CCU_NN")
        pred3 = model3.predict([[purchases,suppcard]])
        s3 = "Upgrade = 1, No Upgrade = 0 ---> " + str(pred3[0])
        
        model4 = joblib.load("CCU_RF")
        pred4 = model4.predict([[purchases,suppcard]])
        s4 = "Upgrade = 1, No Upgrade = 0 ---> " + str(pred4[0])
        
        model5 = joblib.load("CCU_GB")
        pred5 = model5.predict([[purchases,suppcard]])
        s5 = "Upgrade = 1, No Upgrade = 0 ---> " + str(pred5[0])
      
    
        return(render_template("index.html", result1="1", result2="1", result3="1", result4="1", result5="1"))
    else:
        return(render_template("index.html", result1="2", result2="2", result3="2", result4="2", result5="2"))


# In[ ]:


if __name__=="__main__": 
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:




