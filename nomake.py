

def __get_file_extension(path):  
    return os.path.splitext(path)[1]

def set_solution_name( solutionName ) :
    solutionName = solutionName

def add_project( name , type = "lib" ) :
    if type != "lib" or type != "exe" or type != "dll" :
        raise "project " + name +" must have a type like \"exe\",\"lib\",\"dll\", but now it has type:" + type
    if name not in projects :
        projects[name]=dict()
        projects[projectName]["isAudioPlugin"] = False
        projects[projectName]["icon"] = ""
    projects[name]["type"] = type

def set_project_is_AudioPlugin( projectNames ) :
    check_project_exsit(projectNames)
    for x in projectNames :
        projects[x]["isAudioPlugin"] = True


def __add_files( projectNames , debugOrRel , fileOrDir , extNames , subStrInDict , useDirNotFile = False ) :
    check_project_exsit(projectNames)
    tmp = set()
    for root, dirs, files in list_dirs :
        for file in files :
            if __get_file_extension(file) is in extNames :
                tmp.add(file)
    for x in projectNames :
        if debugOrRel is None or "" in debugOrRel or "debug" in debugOrRel :
            projects[x]["icon"]["debug"][subStrInDict].add( tmp )
        if debugOrRel is None or "" in debugOrRel or "release" in debugOrRel :
            projects[x]["icon"]["release"][subStrInDict].add( tmp )

def add_includes( projectNames , debugOrRel , bit32Or64 , dir ) :
    __add_files(projectNames,debugOrRel,fileOrDir,??,"includes",True)


# the libName that u choose must be declared by nomake "save_ext_static_lib_to_system" 
# if u choose one or more projectsThatBuildInLib, the project will build
# in current solution.
# projectsThatBuildInLib are only possible when it is a nomake project
def add_static_lib( projectNames , libName , projectsThatBuildInLib = None ) :
    return


# save_ext_static_lib_to_system( "libpng" , \
#    "c:/SDKs/libpng" ,
#    { \
#        debug32:"c:/SDKs/libpng/slib_debug32_headers/"     , \
#        release32:"c:/SDKs/libpng/slib_release32_headers/" , \
#        debug64:"c:/SDKs/libpng/slib_debug64_headers/"     , \
#        release64:"c:/SDKs/libpng/slib_release64_headers/"   \
#    },
#    { 
#        debug32:"c:/SDKs/libpng/slib_debug32_headers/a.lib"     , \
#        release32:"c:/SDKs/libpng/slib_release32_headers/a.lib" , \
#        debug64:"c:/SDKs/libpng/slib_debug64_headers/a.lib"     , \
#        release64:"c:/SDKs/libpng/slib_release64_headers/a.lib"   \
#    })
#
def save_ext_lib_to_system( libName , libDir , includeDirs , libDirs ) :
    ?????

def add_headers( projectNames , debugOrRel , fileOrDir ) :
    __add_files(projectNames,debugOrRel,fileOrDir,[".h",".hpp"],"headers")


def add_cpp( projectNames , debugOrRel , fileOrDir , doNotComplie = False ) :
    __add_files(projectNames,debugOrRel,fileOrDir,[".h",".hpp"], doNotComplie ? "cpps_not_complie" : "cpps")

##! 将某个文件放入工程，但并不编译
def add_files( projectNames , debugOrRel , fileOrDir , extNames ) :
    __add_files(projectNames,debugOrRel,fileOrDir,extNames, "files_not_complie")

def add_icon( projectNames , file ) :
    check_project_exsit(projectNames)
    for x in projectNames :
        projects[x]["icon"] = file    

def set_project_VST_UniqueID( id ) :
    VST_UniqueID = id

add_project_build_path( ["h7s_exe"] , ["debug"] , ["32","64"] , "c:/test/debug" )

add_project_marco( ["h7s_exe"] , ["debug"] , "DEBUG" , "__DEBUG" , "_DEBUG" )

add_project_flag( ["h7s_exe"] , ["debug"] , "-O2" , "-SSE2" )

set_project_ICC_flags( ["h7s_exe"] , ["debug"] , "-O2" , "-SSE2" )

add_script_when_build_finished( ["AudioEffectImpl"] , "scripts/vst_rename.py" )

solutionName = str()
VST_UniqueID = str()
projects = dict()



nomake -out "d:/xxx" -msvc2015 -icc
nomake -out "d:/xxx" -mingw -makefile -icc

nomake -out "d:/xxx" -xcode -icc