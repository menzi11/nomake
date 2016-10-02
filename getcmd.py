#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import getopt
import sys

'''
1. 处理所使用的函数叫getopt() ，因为是直接使用import 导入的getopt 模块，所以要加上限定getopt 才可以。 
2. 使用sys.argv[1:] 过滤掉第一个参数（它是执行脚本的名字，不应算作参数的一部分）。 
3. 使用短格式分析串"ho:" 。
   当一个选项只是表示开关状态时，即后面不带附加参数时，
   在分析串中写入选项字符。当选项后面是带一个附加参数时，
   在分析串中写入选项字符同时后面加一个":" 号 。所以"ho:" 就表示"h" 是一个开关选项；
   "o:" 则表示后面应该带一个参数。 
4. 使用长格式分析串列表：["help", "output="] 。长格式串也可以有开关状态，即后面不跟"=" 号。如果跟一个等号则表示后面还应有一个参数 。这个长格式表示"help" 是一个开关选项；"output=" 则表示后面应该带一个参数。 
5. 调用getopt 函数。函数返回两个列表：opts 和args 。opts 为分析出的格式信息。args 为不属于格式信息的剩余的命令行参数。opts 是一个两元组的列表。每个元素为：( 选项串, 附加参数) 。如果没有附加参数则为空串'' 。 
6. 整个过程使用异常来包含，这样当分析出错时，就可以打印出使用信息来通知用户如何使用这个程序。 
'''

def main(argv) :

    helpInfo = '''------ help info about nomake --------------
        try to use nomake, u can simply use it like this:
            cd "repo/"
            py nomake.py -o "d:/repo_buildMSVC" -vs2015 -icc
            py nomake.py -o "d:/repo_buildMinGW" -mingw -scons
            py nomake.py -o "~/repo_Xcode" -xcode -icc
        
        all the orders are here:
            
            -o "..."  : build the project in a dir.
            -h        : get some help info.
            -vs2015 : build vs2015 project
            -xcode    : build xcode project
            -scons    : build scons project
            -icc      : build Intel ICC complier project, since ICC
                        have to achive to other complier, u can only
                        use this flag when "-vs2015" or "-xcode"
            -mingw    : tell nomake to use MinGW as complier.
        
        '''

    buildDir = ''
    buildIDE = ""
    buildCompiler = ""
    buildUseICC = False

    allCmd = [ "help", "outfile=" , "complier=" , "ide=" , "ICC" ]

    allIDE = ( "vs2015" , "codeblock" , "xcode" , "scons" )
    allCompiler = ( "gcc" , "clang" , "msvc" )

    def testIDE( arg , T ) :
        if arg not in T :
            print( "flag \"" + arg + "\" is not a flag in " + T )
            sys.exit(2)

    try:
        opts, args = getopt.getopt( argv , 'ho:i:c:' , allCmd )
    except getopt.GetoptError:
        print( 'test.py -i <inputfile> -o <outputfile>' )
        sys.exit(2)
    if not opts :
        print(helpInfo)
        sys.exit(0)

    for opt, arg in opts:
        if opt in ('--help','-h'):
            print(helpInfo)
            sys.exit(0)
        if opt in ('-o' , "--outfile" ) :
            buildDir = arg
        elif opt in ( "-i" , "--ide" ):
            testIDE(arg,allIDE)
            buildIDE = arg
        elif opt in ( "-c" , "--complier" ) :
            testIDE(arg,allCompiler)
            buildCompiler = arg
        elif opt == "ICC" :
            buildUseICC = True


if __name__ == "__main__":
   main(sys.argv[1:]) #过滤掉第一个参数