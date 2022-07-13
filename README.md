# Major Solar Flare Probability Forecast Board
# python 3.10.4

# DB config

- https://blogs.oracle.com/opal/post/connecting-to-oracle-cloud-autonomous-database-through-sqlalchemy
- need oci wallet files "db/instant/Wallet_DBYYYYmmDDHHMMSS"

- http://jsoc.stanford.edu/data/hmi/sharp/dataviewer/
- http://helio.mssl.ucl.ac.uk/hec/hec_gui_free.php
- https://iopscience.iop.org/article/10.3847/1538-4357/ab45e7

# ssh connect
```
$ ./scripts/oracle.bat
```

# oracle linux crontab
```
$ crontab -e
```
```
SHELL=/bin/bash
*/12 * * * * source /home/opc/MajorSolarFlareProbabilityForecastBoard/.venv/bin/activate && python /home/opc/MajorSolarFlareProbabilityForecastBoard/main.py > /dev/null
```

# running check
```
$ crotab -l
```