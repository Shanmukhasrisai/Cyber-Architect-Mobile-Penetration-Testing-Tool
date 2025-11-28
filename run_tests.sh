#!/bin/bash
# Portable Mobile PenTest automation script
TARGET=$1
APK=$2
if [ -z "$TARGET" ]; then
  echo "Usage: ./run_tests.sh <target_ip_or_url> [apk_path]"
  exit 1
fi
python3 mobile_pentest_suite.py $TARGET $APK
if [ ! -z "$APK" ]; then
  echo "--- Additional APK checks ---"
  unzip -l "$APK"
  echo "Use tools like jadx, MobSF for advanced static analysis."
fi
echo "--- Finished ---"
