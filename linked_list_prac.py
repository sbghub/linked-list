# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 21:12:38 2016

@author: Somak
"""
import pdb
class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.next = None

class LinkedList:        
    
    def __init__(self):
        self.__length = 0
        self.head = None
    
    def clear(self):
        self.__length = 0
        self.head = None
    
    def push(self, data):
        node = Node(data)
        
        if self.head==None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        
        self.__length += 1
        
    def pop(self):
        
        if self.head==None:
            return 'Error: the list is empty'
        
        node = self.head
        self.head = node.next
        
        return node.data
        
        self.__length -= 1
    
    def print_list(self):
        node = self.head
        while node!=None:
            print node.data
            node = node.next
    
    def get_item(self, index):
        i = 0
        data = None
        node = self.head
        if index >= self.__length:
            print "too far"
        
        while i <= index:
            data = node.data
            node = node.next
            i += 1
        
        return data
    
    def delete_item(self, index):
        i = 0
        node = self.head
        if index >= self.__length:
            print "too far"
        
        while i < index:
            prev = node
            node = node.next
            i += 1
            
        if index==0:
            self.head = node.next
        else:
            prev.next = node.next
        
        self.__length -= 1
    
    def insert_item(self, data, index):
        i = 0
        node = self.head
        new = Node(data)
        if index > self.__length:
            print "too far"
            return
        
        while i < index and node!=None:
            prev = node
            node = node.next
            i += 1
        
        if index==0:
            new.next = self.head
            self.head = new
        else:
            prev.next = new
            new.next = node
        
        self.__length += 1

    def get_length(self):
        return self.__length
    
    def partition(self, value):
        if self.__length >= 1:
            prev = self.head
            node = prev.next
        else:
            return "too few items to partition"
        
        while node != None:
            
            if node.data < value:
                prev.next = node.next
                node.next = self.head
                self.head = node
                node = prev
                
            prev = node
            node = node.next
    
    def remove_dups(self):
        node = self.head
        x = set()
        
        while node != None:
            x.add(node.data)
            node = node.next
        
        self.clear()
        
        for i in x:
            self.push(i)