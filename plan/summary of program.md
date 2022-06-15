## A summary of how the program works

```mermaid
graph TD;
                
        subgraph main_file
    main
        end

        subgraph connection_file
        main_connection
        server
        listen
        search
        
            subgraph class node
            send_and_listen
            new_node
            end
        
        end

        
        subgraph message_file
        decode
        encode
        prosses
        end
        
        subgraph game_file
        game
        snake
        
        
        end
                
        %% main to connect_file
        main --> main_connection
        main_connection -. threading .-> search & server
        listen -.-> new_node
        search -.-> new_node
        server -.-> listen
        
        %% prosses message 
        prosses --> game
        game --> snake
        game -..-> encode
        
        
        %% connect_file to message_file
        send_and_listen --> decode
        decode --> prosses
        encode -.-o send_and_listen
        prosses -.-o encode
        
        %%


```
---
## موجز  لطريقة عمل البرنامج
```mermaid
graph TD;
                
        subgraph main_file
    main
        end

        subgraph connection_file
        main_connection
        server
        listen
        search
        
            subgraph class node
            send_and_listen
            new_node
            end
        
        end

        
        subgraph message_file
        decode
        encode
        prosses
        end
        
        subgraph game_file
        game
        snake
        
        
        end
                
        %% main to connect_file
        main --> main_connection
        main_connection -. threading .-> search & server
        listen -.-> new_node
        search -.-> new_node
        server -.-> listen
        
        %% prosses message 
        prosses --> game
        game --> snake
        game -..-> encode
        
        
        %% connect_file to message_file
        send_and_listen --> decode
        decode --> prosses
        encode -.-o send_and_listen
        prosses -.-o encode
        
        %%


```
