#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:27:10 2020

@author: zixiangpei
"""
import os
import time
import psutil

process = psutil.Process(os.getpid())


class PBTTrain:
    def __init__(self, step, eval, ready, exploit, explore, update, endofTrain, Population):
        self.step = step
        self.eval = eval
        self.ready = ready
        self.exploit = exploit
        self.explore = explore
        self.update = update
        #self.thetaHighestp = thetaHighestp
        self.P = Population
        self.endofTrain = endofTrain
        
    def __call__(self, worker):
        initial, QList = worker
        theta, h, p, t  = (initial["theta"], initial["h"], initial["p"], initial["t"])
        print("niubi")
        while not self.endofTrain(t): 
                print(t)
                #thetaList.put(theta["theta"][:])
                theta = self.step(theta, h)
                p = self.eval(theta)
                QList.put(p["p"])
                """
                if self.ready(p,t,self.P):
                    hPrime, thetaPrime = self.exploit(h, theta, p, self.P)
                    if theta != thetaPrime:
                        h, theta = self.explore(hPrime, thetaPrime, self.P)
                        p = self.eval(theta)
                """
                print(process.memory_info().rss)
                self.P, t = self.update(self.P, theta, h, p, t)
        #time.sleep(50)
        #bestthetaList.put(self.thetaHighestp(self.P))
        #return (self.thetaHighestp(self.P))