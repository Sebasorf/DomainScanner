import argparse
from ct_searcher import CRSearcher

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--domain', type=str, required=True, help="Target domain.")	
	args = parser.parse_args()
	cs_searcher = CRSearcher(args.domain)
	found_domains = cs_searcher.search_domains()
	print(found_domains)


main()
	
