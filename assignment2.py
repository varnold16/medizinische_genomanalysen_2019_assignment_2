#! /usr/bin/env python3

import vcf

__author__ = 'XXX'


class Assignment2:
    
    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        

    def get_average_quality_of_file(self):
        '''
        Get the average PHRED quality of all variants
        :return:
        '''    
        print("TODO")
        
        
    def get_total_number_of_variants_of_file(self):
        '''
        Get the total number of variants
        :return: total number of variants
        '''
        print("TODO")
    
    
    def get_variant_caller_of_vcf(self):
        '''
        Return the variant caller name
        :return: 
        '''
        print("TODO")
        
        
    def get_human_reference_version(self):
        '''
        Return the genome reference version
        :return: 
        '''
        print("TODO")
        
        
    def get_number_of_indels(self):
        '''
        Return the number of identified INDELs 
        :return: 
        '''
        print("TODO")
        

    def get_number_of_snvs(self):
        '''
        Return the number of SNVs
        :return: 
        '''
        print("TODO")
        
    def get_number_of_heterozygous_variants(self):
        '''
        Return the number of heterozygous variants
        :return: 
        '''
        print("TODO")
        
    
    def merge_chrs_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of chr21 and chr22
        :return: 
        '''
        print("TODO")
        
        print("Number of total variants")
        
    
    def print_summary(self):
        print("Print all results here")
    
    
def main():
    print("Assignment 2")
    assignment2 = Assignment2()
    assignment2.print_summary()
    print("Done with assignment 2")
        
        
if __name__ == '__main__':
    main()
   
    



