# Sparc Big Deal Subscription Pricing Tracker
The Scholarly Publishing and Academic Resources Coalition (SPARC) works to enable the open sharing of sale data of research results and educational materials. Publishers who sell these materials have access to all of the sale data, but the institutions that buy the materials do not. This market asymmetry leaves institutions at a disadvantage when determining the market price of the materials that the institution wants to purchase. Increased access to this data allows institutions to gain access to these materials at a more competitive and affordable price, which will democratize access to knowledge, accelerate discovery, and increase the return on our investment in research and education. As part of this mission, SPARC has developed the Big Deal Knowledge Bases, which details what thousands of peer institutions have paid for journal subscription packages.

Currently SPARC has made this data available to the public for free. The data is in a table format and users can filter out certain criteria and view the data that is relevant to them.  SPARC wants this data to be transformed into a more visually appealing output that is user friendly, that will allow buyers to make more informed purchases.

# Data Source

https://sparcopen.org/our-work/big-deal-knowledge-base/

# How-to

**Environment**
```
python3 -m venv <env_name>
source <env_name>/bin/activate
pip install -r requirements.txt
```

**Data Preparation before Visualization**

Download the data file from Big Deal Knowledge Base then rename and save it to /data/bigdeal.csv
```
git clone https://github.com/dzcyb0rg68/e583infovis_sparc.git
cd e583infovis_sparc
python data_prep.py
```

After you have executed data_prep.py, 3 additional files (data.csv, currency.csv, graph variables.csv) will be generated. They are the sources for Tableau visulization.  

**Visualization and Refresh Dashboard**

Download the Sparc Big Deal Subscription Pricing Tracker.twbx in tableau dashboard folder, open with tableau desktop, and click refresh data. 

# Visualization Preview
![alt text](https://github.com/dzcyb0rg68/e583infovis_sparc/blob/main/tableau%20dashboard/preview/All.png?raw=true)

# Paper Preview

<object data="https://github.com/dzcyb0rg68/e583infovis_sparc/blob/main/report/Visualization%20of%20Historical%20Prices%20for%20Journal%20Subscriptions.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://github.com/dzcyb0rg68/e583infovis_sparc/blob/main/report/Visualization%20of%20Historical%20Prices%20for%20Journal%20Subscriptions.pdf">
        <p>View the PDF report: <a href="https://github.com/dzcyb0rg68/e583infovis_sparc/blob/main/report/Visualization%20of%20Historical%20Prices%20for%20Journal%20Subscriptions.pdf">Download PDF</a>.</p>
    </embed>
</object>

