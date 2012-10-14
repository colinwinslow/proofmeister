'''
Created on Oct 8, 2012

@author: colinwinslow
'''
import unittest
import boto


class Test(unittest.TestCase):


    def testS3(self):
        s3 = boto.connect_s3()
#        bucket = s3.create_bucket('testbucket.colinwinslow.com')
#        key = bucket.new_key('examples/BrainBodyWeight.csv')
#        key.set_contents_from_filename('/Users/colinwinslow/Desktop/BrainBodyWeight.csv')
#        key.set_acl('public-read')

        retrievedkey = s3.get_bucket('testbucket.colinwinslow.com').get_key('examples/BrainBodyWeight.csv')
        retrievedkey.get_contents_to_filename('/myfile.csv')
        print "done"


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()