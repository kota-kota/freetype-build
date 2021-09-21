set(LIB_PATH ${CMAKE_CURRENT_SOURCE_DIR}/library)

if(MSVC)
  # Visual C (Windows)

  # Not create ZERO_CHECK project
  set(CMAKE_SUPPRESS_REGENERATION true)
  # Use the FOLDER target property
  set_property(GLOBAL PROPERTY USE_FOLDERS ON)

  # Set library path
  set(LIB_INC_PATH ${LIB_PATH}/windows/include)
  if (CMAKE_CL_64)
    set(LIB_LINK_PATH ${LIB_PATH}/windows/lib/x64)
  else()
    set(LIB_LINK_PATH ${LIB_PATH}/windows/lib/x86)
  endif()

elseif(ANDROID)
  # Android
  set(LIB_INC_PATH ${LIB_PATH}/android/include)
  if (CMAKE_SYSTEM_PROCESSOR MATCHES "x86_64")
    set(LIB_LINK_PATH ${LIB_PATH}/android/lib/x86_64)
  elseif(CMAKE_SYSTEM_PROCESSOR MATCHES "aarch64")
    set(LIB_LINK_PATH ${LIB_PATH}/android/lib/arm64-v8a)
  endif()

else()
  # Linux
  set(LIB_INC_PATH ${LIB_PATH}/linux/include)
  if (CMAKE_SYSTEM_PROCESSOR MATCHES "x86_64")
    set(LIB_LINK_PATH ${LIB_PATH}/linux/lib/x86_64)
  elseif(CMAKE_SYSTEM_PROCESSOR MATCHES "aarch64")
    set(LIB_LINK_PATH ${LIB_PATH}/linux/lib/arm64)
  endif()
endif()

message(STATUS "LIB_INC_PATH: ${LIB_INC_PATH}")
message(STATUS "LIB_LINK_PATH: ${LIB_LINK_PATH}")
