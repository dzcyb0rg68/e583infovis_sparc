# Sparc Big Deal Subscription Pricing Tracker
SPARC (the Scholarly Publishing and Academic Resources Coalition) works to enable the open sharing of research outputs and educational materials in order to democratize access to knowledge, accelerate discovery, and increase the return on our investment in research and education. As part of this mission, SPARC has developed the Big Deal Knowledge Bases, which details what thousands of peer institutions have paid for journal subscription packages. 

Currently, the SPARC organization has made this data available to the public freely at  https://sparcopen.org/our-work/big-deal-knowledge-base/.  The data is in a table format and users can filter out certain criteria and view the data that is relevant to them. The SPARC organization wants this data transformed into a more visually appealing output so that the public would be able to gain insights easily than they are able to today.

# Data Source

https://sparcopen.org/our-work/big-deal-knowledge-base/

**How-to**

Environment
```
python3 -m venv <env_name>
source <env_name>/bin/activate
pip install -r requirements.txt
```

Data Preparation before Visualization
```
git clone https://github.com/dzcyb0rg68/e583infovis_sparc.git
cd e583infovis_sparc
python data_prep.py
```

# Visualization Preview
![alt text](https://github.com/dzcyb0rg68/e583infovis_sparc/blob/main/tableau%20dashboard/preview/All.png?raw=true)
