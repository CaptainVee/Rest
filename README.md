# Rest

## please view in raw mode
This is the documentation for the rest API

The various endpoint which you can call are ....

1. register/  
      POST: {
          "username": "string"   
          "email": "string"   
          "email2": "string"   
          "password": "string" 
        } 
  returns the username, email and password.
  
2. login/  
    POST: {
      "email": "string" 
      "username": "string", 
      "password": "string" 
    } 
    
   returns a token for authentication
    
3. logout/  
    #######yet to fill#########
    
4. /
  GET: \
  
  returns list of all the available products
  

5. product/create/  
    POST:
      "name":           "string"        #name of product  
      "url" :           "string"        #url of the company website  
      "caption" :       "string"        # a short description about the company (not more than 200 characters).  
      "download_link" : "string"        #(optional) for products with mobile app or downloadable products.  
      "status" :        "string"        # choice field        ('S', 'Private') 
                                                              ('P', 'Public') 
                                                              ('I', 'In_progress'). ##Note pass a single character to the API and not the full word. 
                                                              
      "topics" :        "string"       # multiple choice field      (1, 'IT and Software') 
                                                                    (2, 'Design') 
                                                                    (3, 'Personal Development') 
                                                                    (4, 'Marketing') 
                                                                    (5, 'Music') 
                                                                    (6, 'Cloud') ##Note pass integers to the API and not the full word. 
                                                                    
      "content" :     "string"         # a more detail description about the product 
      "twitter_url" :  "string"        # product's twitter url (optional) 
      "thumbnail" :    "string"        #product's logo or a thumbnail picture. (optional) 
      
      returns some of the data passed above
      
6. product/{ID}/detail/ 
        GET:
          returns details of a specific product 
        PATCH:
          collects the same data passed in product/create and update a particular product 
        DELETE:
          deletes a specific product
 
7. upvote/{ID}/ 
      POST:
       returns the home url 
       
8. comment/create/
      POST:
         "pk" : "string"  ## THIS SHOULD BE PASSED AS A QUERY PARAM and not on the body form. contains the id of the P
         "content" : "string" # this should be passed in the body form. contains comment
         
         returns the content of the comment

9. comment/reply/create/
      POST:
         "pk" : "string"  ## THIS SHOULD BE PASSED AS A QUERY PARAM and not on the body form. contains the id of the comment
         "content" : "string" # this should be passed in the body form. contains the reply to comment
                                                                    
      
10. profile/{ID}/
      GET:
         returns details about the profile
      PATCH:
         "user" : "string" # username
         "picture" : .jpg file  # profile picture
