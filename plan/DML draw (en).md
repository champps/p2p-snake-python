## draw dml classes

note : The dotted arrow from A to B means that B uses A in its operations

```mermaid
graph TD

a -.means b uses a.-> b
b -.means a uses b .-> a

c -- d inhetance from c --> d
d -- c inhetance from d --> c

static_method -- could be--> static_method & class_method


```
draw for api

connection file
```mermaid
classDiagram

        
class connection_api {
  <<static>> 
    get_reference_of_received_messages_list()
    get_reference_of_waiting_messages_list()
    get_reference_of_stable_nodes_list()
    get_reference_of_lost_connection()
}
```

messange file
```mermaid
classDiagram
%%-------------------------------------------------
class message_api  {
  <<static>>
  set_reference_of_received_messages_list()
  set_reference_of_waiting_messages_list()
  
  get_reference_of_own_received_messages_list()
  get_reference_of_own_waiting_messages_list()
  
}
%%-------------------------------------------------
class file  {
  <<object>>
  
}
  
%%-------------------------------------------------

```
  
 compress file
```mermaid
classDiagram

%%-------------------------------------------------
class compress_api  {
    <<static>>
    
    get_compress_object()
}

%%-------------------------------------------------
class compress  {
    <<object>>
    
    aliases = dict
    stuck_word = when no space to separate
    
    read_block()
    
    

}
```

game file
```mermaid
classDiagram

%%-------------------------------------------------

class game {
    <<object>>
       
        
}
```

snake file
```mermaid
classDiagram

%%-------------------------------------------------
class snake {
    <<static>>
    
}

%%-------------------------------------------------

```

Each module has an api class and test class
