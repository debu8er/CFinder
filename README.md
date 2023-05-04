# CFinder
This is tool for DNS BruteForce

# Requirments
This tool needs to install => ```subfinder - dnsx - jq```

# Help

```
usage: CFinder.py [-h] [-d DOMAIN] [-f FILENAME]

CFinder is a tool for get CIDR throught domain

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        domain input.
  -f FILENAME, --filename FILENAME
                        file input.
```

# Example command

```
python3 CFinder.py -d domain.tld

python3 CFinder.py -d domainfile
```
