# new crawler

check args
- period ok? V
- filter ok?

setting
- startAt, endAt -> datesArray V
- filter <- from rds

crawl
- login V
- for date in dates V
    with date && search query = "판매" show 50 rows
    parsing
    save by row

