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
# shortcut for setting func
get_value_setting = settings.get_value_setting
prosses_manager = connect_command.prosses_messange


#this is not important maybe num of it imoportant
#threads_run = {}

class start_server():
    def __init__(self):
        self.obj = self

    #status = ["avalable", "busy", "not avalable", "progress"]
    # #clinet_send_to_servers_socket={}
    # setting var for connection
    start_port = get_value_setting("start_port")
    end_port = get_value_setting("end_port")
    # if bind the server
    my_ip = socket.gethostbyname_ex( socket.getfqdn() )[2][0] \
                    if not get_value_setting("my_ip") else get_value_setting("my_ip")

    # use list becouse can do change with refreance only
    # but sring use less ram
    bind_socket = False
    my_port =    get_value_setting("start_port")
    # if not set in setting file get it

    #def create_socket():
    #    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # server socket for receve requistes form clinet
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # for easyer id
    def generate_id(self, ip, port):
        return str(ip)+":"+str(port)

    # for easyer ip for id
    def get_ip_port_from_id(self, id_connection):
        ip, port = id_connection.split(":")
        return [ip, int(port)]

    # getting own server
    # if find port not available try with next port unless to end of ports num
    # if can bind create thread to connection with server
    # else all besy port return messange cant connect

    def bind_my_server(self):

        while self.bind_socket == 0 and self.my_port <= self.end_port:
            try:
                server.bind((my_ip, my_port))
                print("connect with port {}".format(my_port))
                skip_this_ids.append("{}:{}".format(my_ip, my_port))
                print (skip_this_ids)

                bind_socket = True
                #bind_the_socket[1] = time.time()

            except:
                #print("fail to connect with port {}".format(my_port))
                my_port += 1

    # i prefer to do that with more than one func becose it easy to mantenas (devlop)
    # start listining to peers via socket
    def server_listen_to_clinets():
        liste_to_peers = get_value_setting("listening_peers")
        if bind_socket:
            while liste_to_peers:
                #print(" my id {}{}".format(my_ip, my_port))
                server.listen(5)
                #socket, addr = server.accept()
                clinet_node(server.accept(), my_ip)
                #print("find clinet at {}".format(addr))
        else:
            #print("oops all port are besy cant listen to (clinet)peers")
            raise Exception
            # send error

class clinet_node (*args):
    def __init_(self, *args):
        print(args)


    clinet_node_list = []

    @staticmethod
    def avoid_this_location():
        start_server.my_ip
    # when listen to auther peer connect with my_server
    def thread_server_connection_with_client(my_id, socket):
        # delete my_id not use
        print("now in a thread")
        #itr = 0

        try:
            global id_for_client
            id_for_client = socket.recv(1024)
            server_reseve_from_clinet_socket.append(id_for_client)
            while 1 :
                # send with connect_command return
                message = socket.recv(1024).decode()
                proseger = prosses_manager(message)
                socket.sendall(proseger)
            ##socket.sendall("{}".format(my_id).encode())
            #print("receve {} from ".format((socket.recv(1024))))
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
                        if len(threads_run) <= get_value_setting("max client search socket"):
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
def main_():

main()
