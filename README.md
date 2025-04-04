# RESTful_API_MongoDB_Database
This program is based on RESTful API. The core of this program has three main parts:</br></br>
1- Server (based on Flask Python)</br>
2- MongoDB Database</br>
3- Client</br></br>
**Operation:**</br>
Step1: The client sends RESTful API request to the server.</br>
Step2: Based on the request, server processes the request applies the changes to to MongoDB database.</br>
Step3: The operation is processed and the results are sent to the client.</br></br>
![Flux_Dev_A_futuristic_hightech_illustration_showcasing_a_RESTf_0](https://github.com/user-attachments/assets/391d0af5-1a24-4c8a-b2bf-bc2be5d27b34)

**Availabe Functionalities:**</br>
1- **insert_one_item** => This function is used to add one document to the database</br>
2- **insert_many_item** => This function is used to add more than one document to the database. The argument of this function must be a list data structure.
3- **get_one_query** => This function is used to get **just one query** from the database. Please note that based on the query, there might be other documents that satisfy the criteria but in this query just one of the is fetched.</br>
4- **get_all_query** => This funcrtion is used to get al the documents that satisfy the criteria. </br>
5- **update_one_doc** => This function is used to update an existing document.</br>
6- **aggregate_pipeline** => This function is used to queries including aggregations such as gropuing. The entire pipelien must be sent in a list format with just one element.</br>
7- **delete_one_doc** => This function is used to delete one document from the database.</br>
8- **delete_many_doc** => This fucntion is used to delete many docs from the database. </br>
