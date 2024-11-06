########################################################################
## IMPORTS Libs
import sys
import os
import subprocess
from typing import Dict, Any
import time
import psutil
import GPUtil
import math
from typing import Dict, Any
import os
import subprocess
import platform
from firebase_admin import credentials, initialize_app, storage, db, delete_app
import concurrent.futures

########################################################################

########################################################################
# IMPORT .qrc
from src_1 import icones_interpreter
########################################################################

########################################################################
# IMPORT GUI SoftwareAI

########################################################################

########################################################################
# IMPORT GUI splash_screen
from src_1.ui_system_monitor import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
########################################################################

########################################################################
# IMPORT Pyside6

########################################################################
from PySide2extn.RoundProgressBar import roundProgressBar #IMPORT THE EXTENSION LIBRARY
from PySide2.QtCore import QTimer, Signal, QThread

x = 0
p = 1

# Caminhos possíveis para o nvidia-smi
possible_paths = [
    "C:\\Program Files\\NVIDIA Corporation\\NVSMI\\nvidia-smi.exe",
    "C:\\Windows\\System32\\nvidia-smi.exe",
    "/usr/bin/nvidia-smi",
    "/usr/local/bin/nvidia-smi"
]

nvidia_smi = None
for path in possible_paths:
    if os.path.exists(path):
        nvidia_smi = path
        break



########################################################################

class UpdateSystem(QThread):
    Cpu_signal = Signal(dict)
    finishedd = Signal()

    def __init__(self, nvidia_smi):
        super().__init__()
        self.nvidia_smi = nvidia_smi
        self.running = True

    def get_gpu_name(self):
        try:
            # Executa o comando para obter o nome da GPU
            result = subprocess.check_output(
                ["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"],
                universal_newlines=True
            )
            # Remove quebras de linha ou espaços extras
            return result.strip()
        except Exception as e:
            return "GPU não detectada"  # Retorno padrão caso ocorra algum erro
        
    def get_cpu_name(self):
        """Obtém a nomenclatura do processador."""
        if platform.system() == "Windows":
            # Comando para Windows
            command = "wmic cpu get name"
            cpu_name = subprocess.check_output(command, shell=True).decode().strip().split('\n')[1]
        elif platform.system() == "Linux":
            # Comando para Linux
            command = "cat /proc/cpuinfo | grep 'model name' | uniq"
            cpu_name = subprocess.check_output(command, shell=True).decode().strip().split(': ')[1]
        elif platform.system() == "Darwin":
            # Comando para macOS
            command = "sysctl -n machdep.cpu.brand_string"
            cpu_name = subprocess.check_output(command, shell=True).decode().strip()
        else:
            cpu_name = "Sistema não suportado."
        
        return cpu_name
    
    
    def get_total_ram(self):
        return psutil.virtual_memory().total / (1024 ** 3)

    def get_memory_usage_percent(self):
        return psutil.virtual_memory().percent
    
    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=0.1)

    def get_cuda_utilization(self):
        return self.run_command([self.nvidia_smi, "--query-gpu=utilization.gpu", "--format=csv,noheader,nounits"])
    
    def get_video_decode_percent(self):
        return self.run_command([self.nvidia_smi, "--query-gpu=utilization.decoder", "--format=csv,noheader,nounits"])

    def get_video_encode_percent(self):
        return self.run_command([self.nvidia_smi, "--query-gpu=encoder.stats.averageFps", "--format=csv,noheader,nounits"])

    def get_gpu_utilization(self):
        try:
            # Executa o comando nvidia-smi para obter a utilização da GPU em percentual
            result = subprocess.check_output(
                [self.nvidia_smi,  "--query-gpu=utilization.gpu", "--format=csv,noheader,nounits"],
                universal_newlines=True
            )
            # Remove espaços em branco e converte para inteiro
            utilization = result.strip()
            return utilization
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar nvidia-smi: {e}")
            return 0  # Retorna 0 ou outro valor padrão em caso de erro
        except FileNotFoundError:
            print("nvidia-smi.exe não foi encontrado. Certifique-se de que está instalado e no PATH.")
            return 0
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return 0

    def get_memory_used_mb(self):
        gpus = GPUtil.getGPUs()
        gpu = gpus[0]
        return gpu.memoryUsed

    def get_memory_total_mb(self):
        gpus = GPUtil.getGPUs()
        gpu = gpus[0]
        return gpu.memoryTotal

    def get_memory_usage_percentgpu(self):
        gpus = GPUtil.getGPUs()
        gpu = gpus[0]
        return (gpu.memoryUsed / gpu.memoryTotal) * 100

    def get_memory_free_mb(self):
        return self.run_command([self.nvidia_smi, "--query-gpu=memory.free", "--format=csv,noheader,nounits"])

    def get_gpu_temperature(self):
        return self.run_command([self.nvidia_smi, "--query-gpu=temperature.gpu", "--format=csv,noheader,nounits"])

    def get_gpu_frequency_video_clock(self):
        return self.run_command([self.nvidia_smi, "--query-gpu=clocks.video", "--format=csv,noheader,nounits"])

    def get_gpu_frequency_memory_clock(self):
        return self.run_command([self.nvidia_smi, "--query-gpu=clocks.mem", "--format=csv,noheader,nounits"])


    def run_command(self, cmd):
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout.strip()
        return float(output) if result.returncode == 0 and output != "[Not Supported]" else 0.0

    def run(self):
        while self.running:
            time.sleep(1)

            with concurrent.futures.ThreadPoolExecutor() as executor:
                gpu_name = executor.submit(self.get_gpu_name).result()  
                cpu_name = executor.submit(self.get_cpu_name).result()
                total_ram = executor.submit(self.get_total_ram).result()
                memory_usage_percent = executor.submit(self.get_memory_usage_percent).result()
                cpu_usage = executor.submit(self.get_cpu_usage).result()
                cuda_utilization = executor.submit(self.get_cuda_utilization).result()
                video_decode_percent = executor.submit(self.get_video_decode_percent).result()
                video_encode_percent = executor.submit(self.get_video_encode_percent).result()
                gpu_utilization = executor.submit(self.get_gpu_utilization).result()
                memory_used_mb = executor.submit(self.get_memory_used_mb).result()
                memory_total_mb = executor.submit(self.get_memory_total_mb).result()
                memory_usage_percent_gpu = executor.submit(self.get_memory_usage_percentgpu).result()
                memory_free_mb = executor.submit(self.get_memory_free_mb).result()
                gpu_temperature = executor.submit(self.get_gpu_temperature).result()
                gpu_frequency_video_clock = executor.submit(self.get_gpu_frequency_video_clock).result()
                gpu_frequency_memory_clock = executor.submit(self.get_gpu_frequency_memory_clock).result()
           
                metrics = {
                    'timestamp': time.time(),
                    'gpu_name': gpu_name,
                    'cpu_name': cpu_name,
                    'total_ram': total_ram,
                    'memory_usage_percent': memory_usage_percent,
                    'cpu_usage_percent': cpu_usage,
                    'cuda_usage_percent': cuda_utilization,
                    'video_encode_percent': video_encode_percent,
                    'video_decode_percent': video_decode_percent,
                    'gpu_utilization': gpu_utilization,
                    'gpu_temperature': gpu_temperature,
                    'gpu_frequency_memory_clock': gpu_frequency_memory_clock,
                    'gpu_frequency_video_encoder_decoder_clock': gpu_frequency_video_clock,
                    'memory_free_mb': memory_free_mb,
                    'memory_used_mb': memory_used_mb,
                    'memory_total_mb': memory_total_mb,
                    'memory_usage_percent_gpu': memory_usage_percent_gpu,
                }
                self.Cpu_signal.emit(metrics)

    def stop(self):
        self.running = False
        self.wait()

class MyWidget(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        loadJsonStyle(self, self.ui, jsonFiles={"JsonStyle/style.json"})

        self.label_gpu = self.ui.label_GPU
        self.label_cpu = self.ui.label_CPU
        self.label_ram = self.ui.label_RAM

        self.rpb_cpu = self.ui.widget_cpu
        #self.rpb.rpb_setTextRatio(1)  
        self.rpb_cpu.rpb_setLineWidth(10)
        self.rpb_cpu.rpb_setLineColor((29, 18, 117)) 


        self.rpb_ram = self.ui.widget_ram
        #self.rpb.rpb_setTextRatio(1)  
        self.rpb_ram.rpb_setLineWidth(10)
        #self.rpb.rpb_setLineColor((29, 18, 117)) 




        self.rpb_gpu_temperature = self.ui.widget_gpu_temperature
        self.rpb_gpu_temperature.rpb_setLineWidth(10)
        self.rpb_gpu_temperature.rpb_setLineColor((29, 18, 117)) 

        self.rpb_GPU_encode = self.ui.widget_GPU_encode
        self.rpb_GPU_encode.rpb_setLineWidth(10)
        self.rpb_GPU_encode.rpb_setLineColor((29, 18, 117)) 

        self.rpb_GPU_DECODE = self.ui.widget_GPU_DECODE
        self.rpb_GPU_DECODE.rpb_setLineWidth(10)
        self.rpb_GPU_DECODE.rpb_setLineColor((29, 18, 117)) 

        self.rpb_gpu = self.ui.widget_gpu
        self.rpb_gpu.rpb_setLineWidth(10)
        self.rpb_gpu.rpb_setLineColor((29, 18, 117)) 

        self.rpb_GPU_cuda = self.ui.widget_cuda
        self.rpb_GPU_cuda.rpb_setLineWidth(10)
        self.rpb_GPU_cuda.rpb_setLineColor((29, 18, 117)) 

        self.rpb_GPU_Memory = self.ui.widget_Memory
        self.rpb_GPU_Memory.rpb_setLineWidth(10)
        self.rpb_GPU_Memory.rpb_setLineColor((29, 18, 117)) 





        self.ui.page1ss.clicked.connect(lambda: self.ui.myStackedWidget.setCurrentWidget(self.ui.page))
        self.ui.page2ssss.clicked.connect(lambda: self.ui.myStackedWidget.setCurrentWidget(self.ui.page_2))

        self.threadUpdateloader = UpdateSystem(nvidia_smi)
        self.threadUpdateloader.Cpu_signal.connect(self.update_metrics)
        self.threadUpdateloader.start()


        #QAppSettings.updateAppSettings(self)


    def update_metrics(self, metrics):

        name_gpu = metrics.get('gpu_name', 0)
        self.label_gpu.setText(f"{name_gpu}")


        gpu_temperature = metrics.get('gpu_temperature', 0)
        print(gpu_temperature)
        self.rpb_gpu_temperature.rpb_setTextFormat('Value')
        try:
            self.rpb_gpu_temperature.rpb_setValue(gpu_temperature)
        except:
            pass

        video_encode_percent = metrics.get('video_encode_percent', 0)
        print(video_encode_percent)
        try:
            self.rpb_GPU_encode.rpb_setValue(video_encode_percent)
        except:
            pass


        video_decode_percent = metrics.get('video_decode_percent', 0)
        print(video_decode_percent)
        try:
            self.rpb_GPU_DECODE.rpb_setValue(video_decode_percent)
        except:
            pass


        gpu_utilization = metrics.get('gpu_utilization', 0)
        print(gpu_utilization)
        try:
            self.rpb_gpu.rpb_setValue(gpu_utilization)
        except:
            pass

        cuda_utilization = metrics.get('cuda_utilization', 0)
        print(cuda_utilization)
        try:
            self.rpb_GPU_cuda.rpb_setValue(cuda_utilization)
        except:
            pass

        memory_usage_percent_gpu = metrics.get('memory_usage_percent_gpu', 0)
        print(memory_usage_percent_gpu)
        try:
            self.rpb_GPU_Memory.rpb_setValue(memory_usage_percent_gpu)
        except:
            pass



        cpu_name = metrics.get('cpu_name', 0)
        self.label_cpu.setText(cpu_name)
        cpu_usage = metrics.get('cpu_usage_percent', 0)
        self.rpb_cpu.rpb_setValue(cpu_usage)


        total_ram = metrics.get('total_ram', 0)
        self.label_ram.setText(f"{total_ram:.2f}GB")
        memory_usage_percent = metrics.get('memory_usage_percent', 0)
        self.rpb_ram.rpb_setValue(memory_usage_percent)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    loading_screen = MyWidget()
    loading_screen.show()
    sys.exit(app.exec())