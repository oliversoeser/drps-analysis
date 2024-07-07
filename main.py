import sys

assert(len(sys.argv) == 2)

arg = sys.argv[1]

if arg == "scrape":
    import drps_analysis.scrape
elif arg == "graph":
    import drps_analysis.graph