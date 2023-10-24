# Batch Malware Set-Deobfuscation Tool

This is a Python script for deobfuscating malware batch files by replacing variables with their corresponding values.

add the following code to the end of the obfuscated batch file sample:

```
set > set_list.txt
```


## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Bamorph/set_deob.git
   ```

2. **Navigate to the Repository:**

   ```bash
   cd malware-deobfuscation
   ```

3. **Run the Deobfuscation Script:**

   Replace `<set_file>` and `<obfuscated_file>` with the paths to your "set" list file and obfuscated batch script file, respectively.

   ```bash
   python deobfuscate.py <set_file> <obfuscated_file>
   ```

4. **Deobfuscated Output:**

   The deobfuscated code will be saved in a file with the same name as the obfuscated file but with "_deob" added before the file extension.

   For example, if the obfuscated file is named "batchfuscation.bat," the deobfuscated file will be named "batchfuscation_deob.bat."

## Warning

**Caution**: This tool is designed for security analysts and researchers working with malware samples in controlled environments. Running or executing malware on your system is highly dangerous and should only be done in a secure and isolated environment, such as a sandbox or virtual machine. It is crucial to take all necessary precautions to prevent any unintended harm to your system or network.

**Never run malware on your production or personal devices. Always follow legal and ethical guidelines when handling and analyzing malware.**
