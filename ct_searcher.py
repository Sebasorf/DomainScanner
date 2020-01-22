import re
import requests

class CRSearcher():
    def __init__(self, domain):
        self.url = "https://crt.sh/?q=%.{0}&output=json"
        self.parent_domain = domain
        self.final_domain_list = []
        self.wildcard_domain_list = []
        
    def search_domains(self):
        # Sanitize domain
        self.parent_domain = re.sub('.*www\.','',self.parent_domain,1).split('/')[0].strip()
        print("\n[!] ---- TARGET: {0} ---- [!] \n".format(self.parent_domain))
        
        # Search in Certificate Transparency
        subdomains = []
        response = requests.get(self.url.format(self.parent_domain))
        if response.status_code != 200:
            print("Information not available!") 
            return None
        for (key,value) in enumerate(response.json()):
            subdomain = value['name_value']
            if '\n' in subdomain:
                subdomains = subdomains + subdomain.split('\n')
            else:
                subdomains.append(subdomain)
        subdomains = sorted(set(subdomains))    
        
        return self.__separate_subdomains(subdomains)
    
    	
    # Separate into wildcard, and final subdomains 
    def __separate_subdomains(self, subdomains):
    	wildcard_domains = []
    	explicit_domains = []
    	for subdomain in subdomains:
    		if '*.' in subdomain:
    			wildcard_domains.append(subdomain)
    		else:
    			explicit_domains.append(subdomain)
    	return {"Wildcard": wildcard_domains, "Explicit": explicit_domains}
        
        
        
    