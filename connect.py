#!/usr/bin/env python
import socket
import settings
import connect_command
import threading
import ipaddress
import time
from sys import getsizeof

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


class location():
    """
    contains ip+port methods
    not need to save object becouse object is only test prosses

    """
    # vars
    locations_list = []
    #ip = None
    #port = None #alowse port int in var
    lock = threading.Lokc()

    @classmethod
    def set_ip_port(cls, ip_port):
        " like ('192.168.8.1', 15865')"
        # like "192.168.1.1:8080"
        cls.to_tuple(ip_port)
        ip_port if ip_port is not str\
           else [(ip, int(port)) for ip, port in str_.split(split_char)]

    def get_ip_and_port(cls, to_str=0):
        "in tuple ('ip', port)"
        "in str like '192.168.1.1:1321' "
        # re write to str func to more speed prosses
        return (cls.ip, cls.port) if to_str ==0 else\
                cls.ip+split_char+str(cls.port)

    # class method
    @classmethod
    def add_to_location_list(cls):
        "locaion =  (cls.ip, cls.port) #that use more cpu and ram"

        if cls.get_ip_and_port() in location.locations_list():
            return False
        else:
            try:
                # lock in write only ?
                location.lock_var.acquire()
                location.locations_list.append(cls)
                # unlock
                location.lock_var.release()
                return True
            except:
                return False

    # class method
    @classmethod
    def avalable_locations(cls):
        # for avoid it when scan new location
        return [node.get_ip_and_port() for node in cls.locations_list]+\
            [server_class.get_ip_and_port()]

    @classmethod
    def is_this_avalable_ip_port(cls, ip):
        return  cls.to_tuple(ip) in cls.avalable_locations()

    @classmethod
    def get_ip_port_not_used(cls):
        " get free ip and port (non use) "
        set(cls.get_passable_ip_port()).\
            symmetric_difference(cls.avalable_locations)

    @classmethod
    def get_passable_ip_port(cls):
        "possable that meas all range 'ip port' can connect with"
        [(ip, port)
         for ip in cls.get_possable_ip
         for port in cls.get_possable_ports() ]

    @classmethod
    def get_possable_ip(cls):
        return ipaddress.IPv4Interface(cls.get_current_ip()).network

    @classmethod
    def multi_ip_port_str_to_tuple(cls, str_, split_location="-"):
        """   "like 'ip:port-ip:port'"
        simplifde
        "ip:port-ip:port-ip:port-ip:port"
        split("-"),  [["ip:port"],["ip:port"],["ip:port"]]
        split(":"),   [["ip","port"],["ip","port"],["ip","port"]]
        int(port),   [["ip", port],["ip", port],["ip", port]]

        """
        return [cls.to_tuple(ip_port)
                for ip_port in str_.split(split_location)]

    @classmethod
    def multi_ip_port_list_to_str(cls, list_, split_location="-"):
        """
        like this [["ip", port],["ip", port],["ip", port]]
        to "ip:port-ip:port-ip:port-ip:port"
        join(":") nested list
        join("-") outer list
        """

        return split_location.join(
            [cls.to_str(list_2)  for list_2 in list_ ])

    # static method
    @staticmethod
    def get_current_ip():
        return socket.gethostbyname_ex( socket.getfqdn() )[2][0] \
                    if not get_value_setting("my_ip") else get_value_setting("my_ip")

    @staticmethod
    def get_possable_ports():
        # return available ports from setting
        return[port for port in range (get_value_setting("start_port")
                                 ,get_value_setting("end_port")+1)]

    @staticmethod
    def to_tuple(ip_port: str, split_char=":"):
        "this is list port must be int to decrese use cpu"
        if ip_port is str:
            ip_port = str_.split(split_char)
            ip_port[1] = int(str_[1])
        return tuple(ip_port)

    @staticmethod
    def to_str(ip_port: tuple, split_char=":"):
        "this is list port must be int to decrese use cpu"
        return ip_port[0]+split_char+ str(tuple_[1])
        #  str+str+str faster than use format

class server_class:

    my_ip = location.get_current_ip()
    active_server = None
    my_port =    get_value_setting("start_port")

    # server_socket socket for receve requistes form clinet
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @classmethod
    def __init__(cls):
        #print("start new server_socket")
        cls.bind_my_server()
        #if not exist only
        if cls.active_server is None:
            cls.server_listen_to_clinets()

    # getting own server_socket
    # if find port not available try with next port unless to end of ports num
    # if can bind create thread to connection with server_socket
    # else all besy port return messange cant connect

    @classmethod
    def bind_my_server(cls):
        print("my ip", cls.my_ip)
        if cls.active_server is None:
            for port in location.get_possable_ports():
                try:
                    cls.server_socket.bind((cls.my_ip, port))
                    print("connect with port {}".format(port))

                    cls.active_server = True
                    #bind_the_socket[1] = time.time()
                except:
                    #print("fail to connect with port {}".format(my_port))
                    print("cant connect")


    # i prefer to do that with more than one func becose it easy to mantenas (devlop)
    # start listining to peers via socket
    @classmethod
    def server_listen_to_clinets(cls):
        if get_value_setting("listening_peers") == 0:
            return False
        #print(" my id {}{}".format(my_ip, my_port))
        print("listing now to peer")
        cls.server_socket.listen(5)
        clinet_socket, addr = cls.server_socket.accept()
        # go final part
        #cls.after_find_peer(clinet_socket, clinet_socket.recv(1024))
        threading.Thread(
            target=client_node,
            kwargs={"clinet socket":clinet_socket,
                    "location":clinet_socket.recv(1024)}
                         ).start()
        #client_node(clinet_socket=clinet_socket)
        #print("find clinet at {}".format(addr))

    @classmethod
    def after_find_peer(cls, clinet_socket, location):
        list_location = get_ip_with_port_in_list(location)
        new = client_node()
        clinet_socket.recv(1024)
        new.set_client_socket(clinet_socket)
        new.set_str_location(location)
        #threading.Thread(target=client_node, kwargs={"clinet_socket":clinet_socket})

    @classmethod
    def get_ip_and_port(cls):
        if cls.active_server is not None:
            #only retern when active
            return (cls.active_server.my_ip, cls.active_server.my_port)


class client_node:

    # static var
    node_list = []

    # object var
    ip_port = None
    clinet_socket = None
    server_socket = None

    @classmethod
    def set_str_location(cls, str_location):
       #self.str_location = str_location
       self.ip_port = location.to_tuple(str_location)
       
       
    def set_client_socket(self, s):
        if s:
            self.clinet_socket = s

    def set_server_socket(self, s):
        if s:
            self.server_socket = s

    def get_ip_with_port(self):
        return (self.ip, self.port)


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

        # class meathod
    def set_my_clinet(cls, sock):


class search_auther_nodes():
    # find avoud locations
    # try connect
    # send connects to node to solve it
    #
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
            print("id server_socket {} is \"{}\" ".format(id_server, str(err)))
        #print("server_socket id remove {}".format(id_server))
        clinet_send_to_servers_socket.pop(id_server)
        threads_run.pop(id_server)

    else:
        print("id server_socket {} is \"found :)\" ".format(id_server, end = "\t"))



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

    prints("binding server_socket now ...")
    bind_my_server()

    prints("start listening server_socket to clinet ...")
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
    server_class()

main_()
