#!/usr/bin/env python
from bioseq.calculation.Seqcal import *
from bioseq.pattern.Seqpattern import *
from bioseq.Seqman.dnaconvert import *
import argparse

def myseq():
    parser = argparse.ArgumentParser(prog='myseq', description='Work with sequence')
    subparsers = parser.add_subparsers(title = 'commands', description= 'Please choose the command below:', dest = 'command')
    subparsers.required = True
    
    gc_parser = subparsers.add_parser('gcContent', help='Calculate GC content')
    gc_parser.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    
    count_parser = subparsers.add_parser('countBases', help='Count number of each base')
    count_parser.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    count_parser.add_argument("-r", "--revcomp", type=str, default=None, help="Convert DNA to reverse-complementary")
    
    transcription_parser = subparsers.add_parser('transcription', help='Convert DNA->RNA')
    transcription_parser.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    transcription_parser.add_argument("-r", "--revcomp", type=str, default=None, help="Convert DNA to reverse-complementary")
    
    translation_parser = subparsers.add_parser('translation', help='Convert DNA->Protein')
    translation_parser.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    translation_parser.add_argument("-r", "--revcomp", type=str, default=None, help="Convert DNA to reverse-complementary")
    
    enz_parser = subparsers.add_parser('enzTargetsScan', help='Find restriction enzyme')
    enz_parser.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    enz_parser.add_argument("-e", "--enz", type=str, default=None, help="Enzyme name")
    enz_parser.add_argument("-r", "--revcomp", type=str, default=None, help="Convert DNA to reverse-complementary")
    
    return parser

 
def main():
    parser = myseq()
    args = parser.parse_args()
    # print(args.seq, args.revcomp, args.enz)
    
    if args.seq == None:
        print("-------------\nError: You do not provide an argument\n-----------------\n")
    else:
        seq = args.seq.upper()
        # print(seq)


    # seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
    if args.command == 'transcription':
        if args.seq == None:
            exit(parser.parse_args(['transcription', '-h']))
        print("Input",args.seq, "\nTranscription= ",dna2rna(seq))
    
    if args.command == 'transcription':
        if args.revcomp == None:
            exit(parser.parse_args(['transcription', '-h']))
        print("Input",args.revcomp, "\nTranscription= ",dna2rna(reverseComplementSeq(seq)))
    
    if args.command == 'countBases':
        if args.seq == None:
            exit(parser.parse_args(['countBases', '-h']))
        print("Input",args.seq, "\nCountBases= ",countBasesDict(seq))
    
    if args.command == 'countBases':
        if args.revcomp == None:
            exit(parser.parse_args(['countBases', '-h']))
        print("Input",args.revcomp, "\nCountBases= ",countBasesDict(reverseComplementSeq(seq)))

    if args.command == 'translation':
        if args.seq == None:
            exit(parser.parse_args(['translation', '-h']))
        print("Input",args.seq, "\nTranslation= ",dna2protein(seq))

    if args.command == 'translation':
        if args.revcomp == None:
            exit(parser.parse_args(['translation', '-h']))
        print("Input",args.revcomp, "\nTranslation= ",dna2protein(reverseComplementSeq(seq)))
    
    if args.command == 'gcContent':
        if args.seq == None:
            exit(parser.parse_args(['gcContent', '-h']))
        print("Input",args.seq, "\ngcContent= ",gcContent(seq))
    
    if args.command == 'enzTargetsScan':
        if args.seq == None:
            exit(parser.parse_args(['enzTargetsScan', '-h']))
        print("Input",args.seq, "\nEcoRI sites= ",enzTargetsScan(seq, 'EcoRI'))
    
    if args.command == 'enzTargetsScan':
        if args.revcomp == None:
            exit(parser.parse_args(['enzTargetsScan', '-h']))
        print("Input",args.revcomp, "\nEcoRI sites= ",enzTargetsScan(reverseComplementSeq(seq),'EcoRI'))

if __name__ == '__main__':
    main()


### Example : Input 
# seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
    # # seqinput = seqinput.upper()
    # print("Transcription: ", dna2rna(seq))
    # print("Transcription: ", dna2rna(reverseComplementSeq(seq))
    # print("Translation: ", dna2protein(seq))
    # print("Translation: ", dna2protein(reverseComplementSeq(seq))
    # print("GC Content:", gcContent(seq))
    # print("Count Bases: ", countBasesDict(seq))
    # print("Count Bases: ", countBasesDict(reverseComplementSeq(seq))
    # print("Search EcoRI: ", enzTargetsScan(seq, 'EcoRI'))
    # print("Search EcoRI: ", enzTargetsScan(reverseComplementSeq(seq, 'EcoRI'))







