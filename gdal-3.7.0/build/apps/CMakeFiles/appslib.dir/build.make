# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build

# Include any dependencies generated for this target.
include apps/CMakeFiles/appslib.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include apps/CMakeFiles/appslib.dir/compiler_depend.make

# Include the progress variables for this target.
include apps/CMakeFiles/appslib.dir/progress.make

# Include the compile flags for this target's objects.
include apps/CMakeFiles/appslib.dir/flags.make

apps/CMakeFiles/appslib.dir/gdalinfo_lib.cpp.o: apps/CMakeFiles/appslib.dir/flags.make
apps/CMakeFiles/appslib.dir/gdalinfo_lib.cpp.o: ../apps/gdalinfo_lib.cpp
apps/CMakeFiles/appslib.dir/gdalinfo_lib.cpp.o: apps/CMakeFiles/appslib.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object apps/CMakeFiles/appslib.dir/gdalinfo_lib.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT apps/CMakeFiles/appslib.dir/gdalinfo_lib.cpp.o -MF CMakeFiles/appslib.dir/gdalinfo_lib.cpp.o.d -o CMakeFiles/appslib.dir/gdalinfo_lib.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalinfo_lib.cpp

apps/CMakeFiles/appslib.dir/gdalinfo_lib.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/appslib.dir/gdalinfo_lib.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalinfo_lib.cpp > CMakeFiles/appslib.dir/gdalinfo_lib.cpp.i

apps/CMakeFiles/appslib.dir/gdalinfo_lib.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/appslib.dir/gdalinfo_lib.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalinfo_lib.cpp -o CMakeFiles/appslib.dir/gdalinfo_lib.cpp.s

apps/CMakeFiles/appslib.dir/gdalbuildvrt_lib.cpp.o: apps/CMakeFiles/appslib.dir/flags.make
apps/CMakeFiles/appslib.dir/gdalbuildvrt_lib.cpp.o: ../apps/gdalbuildvrt_lib.cpp
apps/CMakeFiles/appslib.dir/gdalbuildvrt_lib.cpp.o: apps/CMakeFiles/appslib.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object apps/CMakeFiles/appslib.dir/gdalbuildvrt_lib.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT apps/CMakeFiles/appslib.dir/gdalbuildvrt_lib.cpp.o -MF CMakeFiles/appslib.dir/gdalbuildvrt_lib.cpp.o.d -o CMakeFiles/appslib.dir/gdalbuildvrt_lib.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalbuildvrt_lib.cpp

apps/CMakeFiles/appslib.dir/gdalbuildvrt_lib.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/appslib.dir/gdalbuildvrt_lib.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalbuildvrt_lib.cpp > CMakeFiles/appslib.dir/gdalbuildvrt_lib.cpp.i

apps/CMakeFiles/appslib.dir/gdalbuildvrt_lib.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/appslib.dir/gdalbuildvrt_lib.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalbuildvrt_lib.cpp -o CMakeFiles/appslib.dir/gdalbuildvrt_lib.cpp.s

apps/CMakeFiles/appslib.dir/gdal_grid_lib.cpp.o: apps/CMakeFiles/appslib.dir/flags.make
apps/CMakeFiles/appslib.dir/gdal_grid_lib.cpp.o: ../apps/gdal_grid_lib.cpp
apps/CMakeFiles/appslib.dir/gdal_grid_lib.cpp.o: apps/CMakeFiles/appslib.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object apps/CMakeFiles/appslib.dir/gdal_grid_lib.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT apps/CMakeFiles/appslib.dir/gdal_grid_lib.cpp.o -MF CMakeFiles/appslib.dir/gdal_grid_lib.cpp.o.d -o CMakeFiles/appslib.dir/gdal_grid_lib.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdal_grid_lib.cpp

apps/CMakeFiles/appslib.dir/gdal_grid_lib.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/appslib.dir/gdal_grid_lib.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdal_grid_lib.cpp > CMakeFiles/appslib.dir/gdal_grid_lib.cpp.i

apps/CMakeFiles/appslib.dir/gdal_grid_lib.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/appslib.dir/gdal_grid_lib.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdal_grid_lib.cpp -o CMakeFiles/appslib.dir/gdal_grid_lib.cpp.s

apps/CMakeFiles/appslib.dir/gdal_translate_lib.cpp.o: apps/CMakeFiles/appslib.dir/flags.make
apps/CMakeFiles/appslib.dir/gdal_translate_lib.cpp.o: ../apps/gdal_translate_lib.cpp
apps/CMakeFiles/appslib.dir/gdal_translate_lib.cpp.o: apps/CMakeFiles/appslib.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object apps/CMakeFiles/appslib.dir/gdal_translate_lib.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT apps/CMakeFiles/appslib.dir/gdal_translate_lib.cpp.o -MF CMakeFiles/appslib.dir/gdal_translate_lib.cpp.o.d -o CMakeFiles/appslib.dir/gdal_translate_lib.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdal_translate_lib.cpp

apps/CMakeFiles/appslib.dir/gdal_translate_lib.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/appslib.dir/gdal_translate_lib.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdal_translate_lib.cpp > CMakeFiles/appslib.dir/gdal_translate_lib.cpp.i

apps/CMakeFiles/appslib.dir/gdal_translate_lib.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/appslib.dir/gdal_translate_lib.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdal_translate_lib.cpp -o CMakeFiles/appslib.dir/gdal_translate_lib.cpp.s

apps/CMakeFiles/appslib.dir/gdal_rasterize_lib.cpp.o: apps/CMakeFiles/appslib.dir/flags.make
apps/CMakeFiles/appslib.dir/gdal_rasterize_lib.cpp.o: ../apps/gdal_rasterize_lib.cpp
apps/CMakeFiles/appslib.dir/gdal_rasterize_lib.cpp.o: apps/CMakeFiles/appslib.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object apps/CMakeFiles/appslib.dir/gdal_rasterize_lib.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT apps/CMakeFiles/appslib.dir/gdal_rasterize_lib.cpp.o -MF CMakeFiles/appslib.dir/gdal_rasterize_lib.cpp.o.d -o CMakeFiles/appslib.dir/gdal_rasterize_lib.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdal_rasterize_lib.cpp

apps/CMakeFiles/appslib.dir/gdal_rasterize_lib.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/appslib.dir/gdal_rasterize_lib.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdal_rasterize_lib.cpp > CMakeFiles/appslib.dir/gdal_rasterize_lib.cpp.i

apps/CMakeFiles/appslib.dir/gdal_rasterize_lib.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/appslib.dir/gdal_rasterize_lib.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdal_rasterize_lib.cpp -o CMakeFiles/appslib.dir/gdal_rasterize_lib.cpp.s

apps/CMakeFiles/appslib.dir/gdalwarp_lib.cpp.o: apps/CMakeFiles/appslib.dir/flags.make
apps/CMakeFiles/appslib.dir/gdalwarp_lib.cpp.o: ../apps/gdalwarp_lib.cpp
apps/CMakeFiles/appslib.dir/gdalwarp_lib.cpp.o: apps/CMakeFiles/appslib.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object apps/CMakeFiles/appslib.dir/gdalwarp_lib.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT apps/CMakeFiles/appslib.dir/gdalwarp_lib.cpp.o -MF CMakeFiles/appslib.dir/gdalwarp_lib.cpp.o.d -o CMakeFiles/appslib.dir/gdalwarp_lib.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalwarp_lib.cpp

apps/CMakeFiles/appslib.dir/gdalwarp_lib.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/appslib.dir/gdalwarp_lib.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalwarp_lib.cpp > CMakeFiles/appslib.dir/gdalwarp_lib.cpp.i

apps/CMakeFiles/appslib.dir/gdalwarp_lib.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/appslib.dir/gdalwarp_lib.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalwarp_lib.cpp -o CMakeFiles/appslib.dir/gdalwarp_lib.cpp.s

apps/CMakeFiles/appslib.dir/commonutils.cpp.o: apps/CMakeFiles/appslib.dir/flags.make
apps/CMakeFiles/appslib.dir/commonutils.cpp.o: ../apps/commonutils.cpp
apps/CMakeFiles/appslib.dir/commonutils.cpp.o: apps/CMakeFiles/appslib.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Building CXX object apps/CMakeFiles/appslib.dir/commonutils.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT apps/CMakeFiles/appslib.dir/commonutils.cpp.o -MF CMakeFiles/appslib.dir/commonutils.cpp.o.d -o CMakeFiles/appslib.dir/commonutils.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/commonutils.cpp

apps/CMakeFiles/appslib.dir/commonutils.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/appslib.dir/commonutils.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/commonutils.cpp > CMakeFiles/appslib.dir/commonutils.cpp.i

apps/CMakeFiles/appslib.dir/commonutils.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/appslib.dir/commonutils.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/commonutils.cpp -o CMakeFiles/appslib.dir/commonutils.cpp.s

apps/CMakeFiles/appslib.dir/ogrinfo_lib.cpp.o: apps/CMakeFiles/appslib.dir/flags.make
apps/CMakeFiles/appslib.dir/ogrinfo_lib.cpp.o: ../apps/ogrinfo_lib.cpp
apps/CMakeFiles/appslib.dir/ogrinfo_lib.cpp.o: apps/CMakeFiles/appslib.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "Building CXX object apps/CMakeFiles/appslib.dir/ogrinfo_lib.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT apps/CMakeFiles/appslib.dir/ogrinfo_lib.cpp.o -MF CMakeFiles/appslib.dir/ogrinfo_lib.cpp.o.d -o CMakeFiles/appslib.dir/ogrinfo_lib.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/ogrinfo_lib.cpp

apps/CMakeFiles/appslib.dir/ogrinfo_lib.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/appslib.dir/ogrinfo_lib.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/ogrinfo_lib.cpp > CMakeFiles/appslib.dir/ogrinfo_lib.cpp.i

apps/CMakeFiles/appslib.dir/ogrinfo_lib.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/appslib.dir/ogrinfo_lib.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/ogrinfo_lib.cpp -o CMakeFiles/appslib.dir/ogrinfo_lib.cpp.s

apps/CMakeFiles/appslib.dir/ogr2ogr_lib.cpp.o: apps/CMakeFiles/appslib.dir/flags.make
apps/CMakeFiles/appslib.dir/ogr2ogr_lib.cpp.o: ../apps/ogr2ogr_lib.cpp
apps/CMakeFiles/appslib.dir/ogr2ogr_lib.cpp.o: apps/CMakeFiles/appslib.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_9) "Building CXX object apps/CMakeFiles/appslib.dir/ogr2ogr_lib.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT apps/CMakeFiles/appslib.dir/ogr2ogr_lib.cpp.o -MF CMakeFiles/appslib.dir/ogr2ogr_lib.cpp.o.d -o CMakeFiles/appslib.dir/ogr2ogr_lib.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/ogr2ogr_lib.cpp

apps/CMakeFiles/appslib.dir/ogr2ogr_lib.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/appslib.dir/ogr2ogr_lib.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/ogr2ogr_lib.cpp > CMakeFiles/appslib.dir/ogr2ogr_lib.cpp.i

apps/CMakeFiles/appslib.dir/ogr2ogr_lib.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/appslib.dir/ogr2ogr_lib.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/ogr2ogr_lib.cpp -o CMakeFiles/appslib.dir/ogr2ogr_lib.cpp.s

apps/CMakeFiles/appslib.dir/gdaldem_lib.cpp.o: apps/CMakeFiles/appslib.dir/flags.make
apps/CMakeFiles/appslib.dir/gdaldem_lib.cpp.o: ../apps/gdaldem_lib.cpp
apps/CMakeFiles/appslib.dir/gdaldem_lib.cpp.o: apps/CMakeFiles/appslib.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_10) "Building CXX object apps/CMakeFiles/appslib.dir/gdaldem_lib.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT apps/CMakeFiles/appslib.dir/gdaldem_lib.cpp.o -MF CMakeFiles/appslib.dir/gdaldem_lib.cpp.o.d -o CMakeFiles/appslib.dir/gdaldem_lib.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdaldem_lib.cpp

apps/CMakeFiles/appslib.dir/gdaldem_lib.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/appslib.dir/gdaldem_lib.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdaldem_lib.cpp > CMakeFiles/appslib.dir/gdaldem_lib.cpp.i

apps/CMakeFiles/appslib.dir/gdaldem_lib.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/appslib.dir/gdaldem_lib.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdaldem_lib.cpp -o CMakeFiles/appslib.dir/gdaldem_lib.cpp.s

apps/CMakeFiles/appslib.dir/nearblack_lib.cpp.o: apps/CMakeFiles/appslib.dir/flags.make
apps/CMakeFiles/appslib.dir/nearblack_lib.cpp.o: ../apps/nearblack_lib.cpp
apps/CMakeFiles/appslib.dir/nearblack_lib.cpp.o: apps/CMakeFiles/appslib.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_11) "Building CXX object apps/CMakeFiles/appslib.dir/nearblack_lib.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT apps/CMakeFiles/appslib.dir/nearblack_lib.cpp.o -MF CMakeFiles/appslib.dir/nearblack_lib.cpp.o.d -o CMakeFiles/appslib.dir/nearblack_lib.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/nearblack_lib.cpp

apps/CMakeFiles/appslib.dir/nearblack_lib.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/appslib.dir/nearblack_lib.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/nearblack_lib.cpp > CMakeFiles/appslib.dir/nearblack_lib.cpp.i

apps/CMakeFiles/appslib.dir/nearblack_lib.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/appslib.dir/nearblack_lib.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/nearblack_lib.cpp -o CMakeFiles/appslib.dir/nearblack_lib.cpp.s

apps/CMakeFiles/appslib.dir/gdalmdiminfo_lib.cpp.o: apps/CMakeFiles/appslib.dir/flags.make
apps/CMakeFiles/appslib.dir/gdalmdiminfo_lib.cpp.o: ../apps/gdalmdiminfo_lib.cpp
apps/CMakeFiles/appslib.dir/gdalmdiminfo_lib.cpp.o: apps/CMakeFiles/appslib.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_12) "Building CXX object apps/CMakeFiles/appslib.dir/gdalmdiminfo_lib.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT apps/CMakeFiles/appslib.dir/gdalmdiminfo_lib.cpp.o -MF CMakeFiles/appslib.dir/gdalmdiminfo_lib.cpp.o.d -o CMakeFiles/appslib.dir/gdalmdiminfo_lib.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalmdiminfo_lib.cpp

apps/CMakeFiles/appslib.dir/gdalmdiminfo_lib.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/appslib.dir/gdalmdiminfo_lib.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalmdiminfo_lib.cpp > CMakeFiles/appslib.dir/gdalmdiminfo_lib.cpp.i

apps/CMakeFiles/appslib.dir/gdalmdiminfo_lib.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/appslib.dir/gdalmdiminfo_lib.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalmdiminfo_lib.cpp -o CMakeFiles/appslib.dir/gdalmdiminfo_lib.cpp.s

apps/CMakeFiles/appslib.dir/gdalmdimtranslate_lib.cpp.o: apps/CMakeFiles/appslib.dir/flags.make
apps/CMakeFiles/appslib.dir/gdalmdimtranslate_lib.cpp.o: ../apps/gdalmdimtranslate_lib.cpp
apps/CMakeFiles/appslib.dir/gdalmdimtranslate_lib.cpp.o: apps/CMakeFiles/appslib.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_13) "Building CXX object apps/CMakeFiles/appslib.dir/gdalmdimtranslate_lib.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT apps/CMakeFiles/appslib.dir/gdalmdimtranslate_lib.cpp.o -MF CMakeFiles/appslib.dir/gdalmdimtranslate_lib.cpp.o.d -o CMakeFiles/appslib.dir/gdalmdimtranslate_lib.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalmdimtranslate_lib.cpp

apps/CMakeFiles/appslib.dir/gdalmdimtranslate_lib.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/appslib.dir/gdalmdimtranslate_lib.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalmdimtranslate_lib.cpp > CMakeFiles/appslib.dir/gdalmdimtranslate_lib.cpp.i

apps/CMakeFiles/appslib.dir/gdalmdimtranslate_lib.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/appslib.dir/gdalmdimtranslate_lib.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalmdimtranslate_lib.cpp -o CMakeFiles/appslib.dir/gdalmdimtranslate_lib.cpp.s

appslib: apps/CMakeFiles/appslib.dir/gdalinfo_lib.cpp.o
appslib: apps/CMakeFiles/appslib.dir/gdalbuildvrt_lib.cpp.o
appslib: apps/CMakeFiles/appslib.dir/gdal_grid_lib.cpp.o
appslib: apps/CMakeFiles/appslib.dir/gdal_translate_lib.cpp.o
appslib: apps/CMakeFiles/appslib.dir/gdal_rasterize_lib.cpp.o
appslib: apps/CMakeFiles/appslib.dir/gdalwarp_lib.cpp.o
appslib: apps/CMakeFiles/appslib.dir/commonutils.cpp.o
appslib: apps/CMakeFiles/appslib.dir/ogrinfo_lib.cpp.o
appslib: apps/CMakeFiles/appslib.dir/ogr2ogr_lib.cpp.o
appslib: apps/CMakeFiles/appslib.dir/gdaldem_lib.cpp.o
appslib: apps/CMakeFiles/appslib.dir/nearblack_lib.cpp.o
appslib: apps/CMakeFiles/appslib.dir/gdalmdiminfo_lib.cpp.o
appslib: apps/CMakeFiles/appslib.dir/gdalmdimtranslate_lib.cpp.o
appslib: apps/CMakeFiles/appslib.dir/build.make
.PHONY : appslib

# Rule to build all files generated by this target.
apps/CMakeFiles/appslib.dir/build: appslib
.PHONY : apps/CMakeFiles/appslib.dir/build

apps/CMakeFiles/appslib.dir/clean:
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && $(CMAKE_COMMAND) -P CMakeFiles/appslib.dir/cmake_clean.cmake
.PHONY : apps/CMakeFiles/appslib.dir/clean

apps/CMakeFiles/appslib.dir/depend:
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0 /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps/CMakeFiles/appslib.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : apps/CMakeFiles/appslib.dir/depend
