#! /usr/bin/env python3

import vcf

__author__ = 'ARNOLD Vivienne'


class Assignment2:
    
    def __init__(self, vcf_file, vcf_file_for_merge, merged_file_name):
        ## Check if pyvcf is installed
        print("PyVCF version: %s\n" % vcf.VERSION)

        self.vcf_file_chrA = vcf_file

        self.vcf_file_chrB = vcf_file_for_merge

        self.vcf_file_merged = merged_file_name

        print("Read data from selected file <"+self.vcf_file_chrA+">")

        self.number_of_variants = self.get_total_number_of_variants_of_file(self.vcf_file_chrA)

        self.average_phred = self.get_average_quality_of_file()

        self.variant_callers = self.get_variant_caller_of_vcf()

        self.human_reference_versions = self.get_human_reference_version()

        self.number_of_indels = self.get_number_of_indels()

        self.number_of_snvs = self.get_number_of_snvs()

        self.number_of_heterozygous_variants = self.get_number_of_heterozygous_variants()

        print("")

        self.merge = self.merge_chrs_into_one_vcf()

        if self.merge:
            self.number_of_variants_in_merged_file = self.get_total_number_of_variants_of_file(self.vcf_file_merged)


    def get_total_number_of_variants_of_file(self, file_name):
        """
        return total number of variants
        """
        print(" * Get total number of variants")

        total_number_of_variants = 0

        for record in vcf.Reader(open(file_name, "r")):
            total_number_of_variants += 1

        return total_number_of_variants

    def get_average_quality_of_file(self):
        """
        return average PHRED quality of all variants
        """
        print(" * Get average PHRED quality of all variants")
        sum_of_phred = 0

        for record in vcf.Reader(open(self.vcf_file_chrA, "r")):
            sum_of_phred += record.QUAL

        average_phred_quality = round((sum_of_phred / self.number_of_variants), 2)

        return average_phred_quality

    def get_variant_caller_of_vcf(self):
        """
        Return the variant caller name
        """
        print(" * Get variant caller name(s)")

        variant_callers = set()

        for record in vcf.Reader(open(self.vcf_file_chrA, "r")):
            for variant_caller in record.INFO["callsetnames"]:
                variant_callers.add(variant_caller)

        variant_callers.remove('')

        return sorted(variant_callers)

    def get_human_reference_version(self):
        """
        Return the genome reference version
        """
        print(" * Get human reference version(s)")

        human_reference_versions = set()

        for record in vcf.Reader(open(self.vcf_file_chrA, "r")):
            if 'difficultregion' in record.INFO.keys():
                for human_reference_version in record.INFO['difficultregion']:
                        human_reference_versions.add(human_reference_version)

        return sorted(human_reference_versions)

    def get_number_of_indels(self):
        """
        Return the number of identified INDELs
        """
        print(" * Get number of INDELs")

        number_of_indels = 0

        for record in vcf.Reader(open(self.vcf_file_chrA, "r")):
            if record.is_indel:
                number_of_indels += 1

        return number_of_indels

    def get_number_of_snvs(self):
        """
        Return the number of SNVs
        """
        print(" * Get number of SNVs")

        number_of_snvs = 0

        for record in vcf.Reader(open(self.vcf_file_chrA, "r")):
            if record.is_snp:
                number_of_snvs += 1

        return number_of_snvs
        
    def get_number_of_heterozygous_variants(self):
        """
        Return the number of heterozygous variants
        :return: 
        """
        print(" * Get number of heterozygous variants")

        number_of_heterozygous_variants = 0

        for record in vcf.Reader(open(self.vcf_file_chrA, "r")):
            number_of_heterozygous_variants += record.num_het

        return number_of_heterozygous_variants

    def merge_chrs_into_one_vcf(self):
        """
        Creates one VCF containing all variants of chr21 and chr22
        :return: number of total variants
        """
        print("Merge with file <" + self.vcf_file_chrB + "> into <" + self.vcf_file_merged + ">")

        fileA = open(self.vcf_file_chrA, 'r')
        fileB = open(self.vcf_file_chrB, 'r')
        fileA_lines = fileA.readlines()
        fileB_lines = fileB.readlines()

        merge_ability = False
        line_number = 0

        ## check merge ability
        for lineA in fileA_lines:
            if lineA[0] is not "#":
                break
            if lineA == fileB_lines[line_number]:
                merge_ability = True
                line_number += 1
            else:
                merge_ability = False
                line_number += 1

        fileA.close()
        fileB.close()

        if merge_ability == False:
            print(" * Failed to merge files due to differential headers")
            return False
        else:
            vcf_file_chrA = vcf.Reader(open(self.vcf_file_chrA), "r")
            vcf_file_chrB = vcf.Reader(open(self.vcf_file_chrB), "r")

            vcf_writer = vcf.Writer(open(self.vcf_file_merged, "w"), vcf_file_chrA)

            for vcf_file in [vcf_file_chrA, vcf_file_chrB]:
                for record in vcf_file:
                    vcf_writer.write_record(record)

            print(" * Merge succeed")

            return True

    def print_summary(self):
        """
        Prints every possible gained information.
        """

        print("\n"+" S U M M A R Y  ".center(80,"*"),"\n")

        print("Average PHRED quality:".ljust(25," ")+str(self.average_phred)+"\n")

        print("Number of variants:".ljust(25," ")+str(self.number_of_variants)+"\n")

        print("Variant caller:")
        for variant_caller in self.variant_callers:
            print("  * "+variant_caller)
        print("")

        print("Human reference version:")
        for human_reference_version in self.human_reference_versions:
            print("  * "+human_reference_version)
        print("")

        print("Number of INDELs:".ljust(25," ")+str(self.number_of_indels)+"\n")

        print("Number of SNVs:".ljust(25," ")+str(self.number_of_snvs)+"\n")

        print("Number of heterozygous variants:".ljust(35," ")+str(self.number_of_heterozygous_variants)+"\n")

        if self.merge:
            print("Number of variants in merged file:".ljust(35, " ")+str(self.number_of_variants_in_merged_file)+"\n")

        print("*"*80+"\n")
    
def main():
    print("Assignment 2\n")
    assignment2 = Assignment2("chr22_new.vcf", "chr21_new.vcf", "chr_22_merged_with_chr_21.vcf")
    assignment2.print_summary()
    print("Done with assignment 2")


if __name__ == '__main__':
    main()
