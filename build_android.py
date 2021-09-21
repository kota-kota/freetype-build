import os
import shutil
import common as cmn

# Toolchain path
NDK_PATH = "/opt/android-sdk-linux/android-ndk-r21e"
TOOLCHAIN = os.path.join(NDK_PATH, "build/cmake/android.toolchain.cmake")
ANDROID_PLATFORM = "16"

# Install path
INSTALL_PREFIX_OS = os.path.join(cmn.INSTALL_PREFIX, "android")

def main():
  cmn.Log("Start " + __file__)
  cmn.Log("INSTALL_PREFIX_OS: " + INSTALL_PREFIX_OS)
  Build_freetype("x86_64", "Debug")
  Build_freetype("x86_64", "Release")
  Build_freetype("arm64-v8a", "Debug")
  Build_freetype("arm64-v8a", "Release")

#------------------------------------------------------------
# freetypeビルド
#    host       "x86_64" or "arm64-v8a"
#    build_type "Debug" or "Release"
def Build_freetype(host, build_type):
  cmn.Log("Build libpng host=" + host + " build_type=" + build_type)
  INSTALL_PREFIX = os.path.join(INSTALL_PREFIX_OS, host, build_type)
  os.chdir(cmn.FREETYPE_DIR)
  shutil.rmtree("build", ignore_errors=True)
  os.makedirs("build", exist_ok=True)
  os.chdir("build")
  # cmake generator
  cmd = ["cmake"]
  cmd += ["-DCMAKE_TOOLCHAIN_FILE=" + TOOLCHAIN]
  cmd += ["-DANDROID_ABI=" + host]
  cmd += ["-DANDROID_PLATFORM=" + ANDROID_PLATFORM]
  cmd += ["-DCMAKE_INSTALL_PREFIX=" + INSTALL_PREFIX]
  cmd += ["-DFT_WITH_ZLIB=ON -D FT_WITH_PNG=ON"]
  cmd += ["-DPNG_PNG_INCLUDE_DIR=" + os.path.join(INSTALL_PREFIX, "include")]
  cmd += ["-DPNG_LIBRARY=" + os.path.join(INSTALL_PREFIX, "lib", "libpng16.a")]
  cmd += [".."]
  cmn.Do(cmd)
  # cmake build
  cmd = ["cmake --build ."]
  cmd += ["--config " + build_type]
  cmn.Do(cmd)
  # cmake install
  cmd = ["cmake --install ."]
  cmd += ["--config " + build_type]
  cmn.Do(cmd)


if __name__ == '__main__':
    main()
