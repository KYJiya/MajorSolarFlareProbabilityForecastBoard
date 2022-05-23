# Major Solar Flare Probability Forecast Board
# python 3.10.4

# DB config

- https://blogs.oracle.com/opal/post/connecting-to-oracle-cloud-autonomous-database-through-sqlalchemy
- need oci wallet files "db/instant/Wallet_DBYYYYmmDDHHMMSS"


SELECT * FROM gevloc_sxr_flare 
WHERE (nar=13014) 
AND (xray_class LIKE 'M%' OR xray_class LIKE 'X%') 
AND (time_start>='2022-05-19 00:00:00' AND time_start<='2022-05-20 00:00:00')