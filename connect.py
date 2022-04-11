#!/usr/bin/env python
import socket
import settings
import connect_command
import threading
import ipaddress
import time

"""
يقوم بربط الخادم
ثم البحث عن خوادم عبر العميل
ثم إرسال الطلب من العميل لملف الرد (اوامر الإتصال) حسنا
يتم ارسال الطلب للخادم عبر دالة إرسال طلب من ملف اوامر الإتصال
"""

#status now
status_now = []
# shortcut for setting func
sconn = settings.get_value_setting
prossmsg = connect_command.prosses_messange

threads_run = {}
# sockets how server receve from clinet connection
server_reseve_from_clinet_socket={}
# socket how clinet send to server requist
clinet_send_to_servers_socket={}
# setting var for connection
start_port = sconn("start_port")
end_port = sconn("end_port")
my_port = start_port
# set time of create server
#time_of_bind_the_socket = None
# if bind the server
class server():

    """
    getting server and start listen to clinets
    """
    bind_the_socket = [0]
    # if not set in setting file
    my_ip = socket.gethostbyname_ex( socket.getfqdn() )[2][0] \
                    if not sconn("my_ip") else sconn("my_ip")

# for skip local host and finded servers
# altrnative this with dict clinet_send_to_servers_socket
skip_this_ids = []

# to connect with a new socket
def create_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server socket for receve requistes form clinet
server = create_socket()

# for easyer id
def generate_id(ip, port):
    return str(ip)+":"+str(port)

# for easyer ip for id
def get_ip_port_from_id(id_connection):
    ip, port = id_connection.split(":")
    return [ip, int(port)]

# getting own server
# if find port not available try with next port unless to end of ports num
# if can bind create thread to connection with server
# else all besy port return messange cant connect

def bind_my_server(ip = my_ip, start_port = start_port, end_port = end_port):
    global my_port

    while not bind_the_socket[0] and my_port <= end_port:
        try:
            server.bind((my_ip, my_port))
            print("connect with port {}".format(my_port))
            skip_this_ids.append("{}:{}".format(my_ip, my_port))
            print (skip_this_ids)

            bind_the_socket[0] = 1
            #bind_the_socket[1] = time.time()

        except:
            #print("fail to connect with port {}".format(my_port))
            my_port += 1

# i prefer to do that with more than one func becose it easy to mantenas (devlop)
# start listining to peers via socket
def server_listen_to_clinets():
    if bind_the_socket:
        while sconn("listening_peers"):
            #print(" my id {}{}".format(my_ip, my_port))
            server.listen(100)
            conn, addr = server.accept()
            threading.Thread(target=thread_server_connection_with_client, args=(generate_id(my_ip, my_port),conn,)).start()
            print("find clinet at {}".format(addr))
    else:
        print("oops all port are besy cant listen to (clinet)peers")
        # send error

# when listen to auther peer connect with my_server
def thread_server_connection_with_client(my_id, conn):
    # delete my_id not use
    print("now in a thread")
    #itr = 0

    try:
        global id_for_client
        id_for_client = conn.recv(1024)
        server_reseve_from_clinet_socket.append(id_for_client)
        while 1 :
            # send with connect_command return
            message = conn.recv(1024).decode()
            proseger = prossmsg(message)
            conn.sendall(proseger)
        # save id for peer
        #print ( f"peer itration {itr:=itr+1}" )
        #time.sleep(1)
        # save socket in dict
        ##server_reseve_from_clinet_socket[conn]= conn.recv(1024)
        # send my id to peer
        ##conn.sendall("{}".format(my_id).encode())
        #print("receve {} from ".format((conn.recv(1024))))
        # send list of ids to find peers quicly to peer
        #
    except Exception as err:
        #if err == "[Errno 106] Transport endpoint is already connected":
            #print("يووه مشكلة انه متصل فعلا !!! سبحان الله")
        #    pass
        #else:
        #print("there is \"{}\" ".format(err))
        #break
        # remove form avalable clinet
        print (f"oops {id_for_client} disconnected")
        server_reseve_from_clinet_socket.pop(id_for_client)

        pass

# this is petter than nmap becose its fastest
# this work only on first time
def clinet_find_expected_servers():
    # generate ips and range port
    my_ip_zero = ".".join(my_ip.split(".")[0:3])+".0"
    all_ips = ipaddress.IPv4Network('{}/24'.format(my_ip_zero))
    num_of_all_ids = len(list(all_ips)) * (end_port - start_port)
    print(f"num of ids = {num_of_all_ids}")
    for ip in all_ips:
        for port in range(start_port, end_port+1):
                # skip avalabe location and localhost
                #print("skip this ids", skip_this_ids)
                if generate_id(ip, port) not in skip_this_ids:
                    #peers_client.append(clinet_socket())
                    threads_run[generate_id(ip , port)] = threading.Thread(target=clinet_connect_with_server,
                                         args=(str(ip), port, generate_id(ip, port)))

                    # to wait to system finsh from old try connect socket
                    while 1:
                        if len(threads_run) <= sconn("max client search socket"):
                            #print("new inter")
                            threads_run[generate_id(ip, port)].start()
                            # stop after run
                            break
                    #t.join()
                        else :
                            #print(len(threads_run) , "run now ")
                            #time.sleep(.1)
                            pass

def clinet_connect_with_server(ip , port, id_server):
    # connect or skip this location
    # new socket for search
    # to easy delete it when not find or fail connection
    clinet_send_to_servers_socket[id_server] = create_socket()
    try:
            #clinet_send_to_servers_socket[id_server].settimeout(10)
            # [Errno 106] Transport endpoint is already connected
            ##print (ip, type (ip) , port,  type(port) , sep="\t")
            #print("send to {} with port {}".format(ip , port))
            clinet_send_to_servers_socket[id_server].connect((ip, port))
            clinet_send_to_servers_socket[id_server].sendall("{}".format(generate_id(my_ip , my_port)).encode())
            #id_for_peer = clinet_socket.recv()
            #print(id_for_peer, "--------------------------------------------------")

    except Exception as err:
        #print("_______________")
        if str(err) not in ["timed out1", "[Errno 113] No route to host", "[Errno 101] Network is unreachable"]  :
            #err = "غير موجود"
            print("id server {} is \"{}\" ".format(id_server, str(err)))
        #print("server id remove {}".format(id_server))
        clinet_send_to_servers_socket.pop(id_server)
        threads_run.pop(id_server)

    else:
        print("id server {} is \"found :)\" ".format(id_server, end = "\t"))



def sent_to_server(ser_id, m):
    """snet to peer (n) message (m) """
    ## with try
    # and reconnect if fail connect

def set_to_all_list(lst, m):
    # send to all ist ids from own dectinary
    pass

def prints(x):
    print("-"*50)
    print(x)

def main():
    #main method
    # dict for save available player in network {id :ip}

    prints("binding server now ...")
    bind_my_server()

    prints("start listening server to clinet ...")
    threading.Thread(target=server_listen_to_clinets).start()
    #server_listen_to_clinets()

    prints("start search to auther servers (peers) ...")
    #hreading.Thread(target=clinet_find_expected_servers).start()
    t = time.time()
    clinet_find_expected_servers()



    while 1:
        if len(threads_run) == 0 :
            prints(f"finsh search auther servers (peers) with num {len(clinet_send_to_servers_socket)}\
                    \n thats take {time.time()-t} ")
            break
        else:
            time.sleep(5)
            print("this still in network search \n{}".format(len(threads_run)))

    return
main()
