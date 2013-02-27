# This is an example of how to parse ooniprobe reports

import yaml
import sys
print "Opening %s" % sys.argv[1]
f = open(sys.argv[1])
yamloo = yaml.safe_load_all(f)

report_header = yamloo.next()
print "ASN: %s" % report_header['probe_asn']
print "CC: %s" % report_header['probe_cc']
print "IP: %s" % report_header['probe_ip']
print "Start Time: %s" % report_header['start_time']
print "Test name: %s" % report_header['test_name']
print "Test version: %s" % report_header['test_version']

for report_entry in yamloo:
    print "Test: %s" % report_entry['test_name']
    print "Input: %s" % report_entry['input']
    print "Report: %s" % report_entry['report']

f.close()
