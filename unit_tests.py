'''
I know of two ways to do it.

Method 1
The first method (which I prefer) is to use msbuild:

msbuild project.sln /Flags...
Method 2
You can also run:

vcexpress project.sln /build /Flags...
The vcexpress option returns immediately and does not print any output. I suppose that might be what you want for a script.

Note that DevEnv is not distributed with Visual Studio Express 2008 (I spent a lot of time trying to figure that out when I first had a similar issue).

So, the end result might be:

os.system("msbuild project.sln /p:Configuration=Debug")
You'll also want to make sure your environment variables are correct, 
as msbuild and vcexpress are not by default on the system path. 
Either start the Visual Studio build environment and run your script from there, 
or modify the paths in Python (with os.putenv).
'''