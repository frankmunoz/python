import json
import requests


def getAuthorHistory(author):
    history = []


    history.append(getAbout('saintamh'))
    history.append(getTitle(author))
    

    print(history)

#def getAuthorAbout():

def getAbout(username):
    url = 'https://jsonmock.hackerrank.com/api/article_users'
    about = ''
    params = dict(
        username=username,
    )

    response = requests.get(url=url, params=params)
    articles = response.json()['data']
    for article in articles:
        if article['about'] != '' and article['about'] is not None:
            #about.append(article['about'])
            about = article['about']

    return about

def getTitle(author):
    url = 'https://jsonmock.hackerrank.com/api/articles'
    title = []

    params = dict(
        author=author,
    )
    response = requests.get(url=url, params=params)
    articles = response.json()['data']

    for article in articles:
        if article['title'] != '' and article['title'] is not None:
            title.append(article['title'])
        elif article['story_title'] != '' and article['story_title'] is not None:
            title.append(article['story_title'])
    


    return title

#getAuthorHistory('epaga')
#getAuthorHistory('saintamh')
getAuthorHistory('patricktomas')

    
""""
def featuredProduct(products):
    # Write your code here
    featuredProduct = ''
    feature_frequency = 0 
    frequencies = {} 
    for product in products: 
        propductFrequency = frequencies.get(product,0)+1
        frequencies[product] = propductFrequency 

        if propductFrequency>feature_frequency:
            featuredProduct, feature_frequency = product, propductFrequency

        elif propductFrequency == feature_frequency and feature_frequency<product:
            featuredProduct=product

    return featuredProduct

products = ['greenPants', 'redHat', 'blackShirt','bluePants', 'redHat','pinkHat', 'blackShirt', 'greenPants','yellowShirt', 'yellowShirt']

print(featuredProduct(products))
"""
"""
def featuredProduct(products):
    # Write your code here

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    products_count = int(input().strip())

    products = []

    for _ in range(products_count):
        products_item = input()
        products.append(products_item)

    result = featuredProduct(products)

    fptr.write(result + '\n')

    fptr.close()
products = ['greenPants', 'redHat', 'blackShirt','bluePants', 'redHat','pinkHat', 'blackShirt', 'greenPants','yellowShirt', 'yellowShirt']

print(featuredProduct(products))

"""
"""
def featuredProduct(products):
    # Write your code here
    try:
        n = 10000 # Constraints 1 <= n <= 10^4
        if len(products)>n:
            raise TooMuchProductsError
        else:
            productFrequency = [] #List of product's frequencies
            featuredProductFollowingDay = [] #Final list with featured product
            for product in products:
                productFrequency.append(products.count(product)) #Add count frequency of each product into list
            
            featuredProductFollowingDay = max(list(zip(productFrequency, products))) #Maximum key and value frequency, product; Zip provides match between two lists (key, value) 
            return str(featuredProductFollowingDay[1]) #Returns the name of the featured product 
    except TooMuchProductsError:
        print("The products list is too large, try again!")


class TooMuchProductsError():
    #Raised when the products list count is too large
    pass

products = ['greenShirt', 'bluePants', 'redShirt','blackShoes', 'redPants', 'redPants', 'whiteShirt', 'redShirt']
products = ['greenPants', 'redHat', 'blackShirt','bluePants', 'redHat','pinkHat', 'blackShirt', 'greenPants','yellowShirt', 'yellowShirt']

print(featuredProduct(products))
"""