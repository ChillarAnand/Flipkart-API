### Flipkart API
(Unofficial) Python API for Flipkart 

### Usage
    from flipkart import Flipkart

    f = Flipkart()
    results = f.search('iphone 5s')
    list_all = f.list_items(results)
    for title, url in list_all.items():
            print title, url

