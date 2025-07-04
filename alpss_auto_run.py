"""
Credit to Michael Cho
https://michaelcho.me/article/using-pythons-watchdog-to-monitor-changes-to-a-directory
"""

# %%

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from alpss_main import *
import os


class Watcher:

    # this is the directory where you will add the files to
    DIRECTORY_TO_WATCH = "/Users/piyushwanchoo/Library/CloudStorage/OneDrive-JohnsHopkins/Malon_PDV_scope/Cu_Polycrystals/Cu_100nm/20241205_varying_velocity_spall"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == "created":

            # Take any action here when a file is first created.
            print("Received created event - %s." % event.src_path)

            fname = os.path.split(event.src_path)[1]
            print(f"File Created:  {fname}")

            # use these function inputs the same as for the non-automated function alpss_run.py
            alpss_main(
                filename=fname,
                save_data="yes",
                start_time_user="none",
                header_lines=5,
                time_to_skip=6e-6,
                time_to_take=1e-6,
                t_before=10e-9,
                t_after=60e-9,
                start_time_correction=0e-9,
                freq_min=2.5e9,
                freq_max=5e9,
                smoothing_window=601,
                smoothing_wid=3,
                smoothing_amp=1,
                smoothing_sigma=1,
                smoothing_mu=0,
                pb_neighbors=400,
                pb_idx_correction=0,
                rc_neighbors=400,
                rc_idx_correction=0,
                sample_rate=80e9,
                nperseg=512,
                noverlap=435,
                nfft=5120,
                window="hann",
                blur_kernel=(5, 5),
                blur_sigx=0,
                blur_sigy=0,
                carrier_band_time=250e-9,
                cmap="viridis",
                uncert_mult=100,
                order=6,
                wid=25e7,
                lam=1547.532e-9,
                C0=3950,
                density=8900,
                delta_rho=9,
                delta_C0=23,
                delta_lam=8e-18,
                theta=0,
                delta_theta=5,
                exp_data_dir= "/Users/piyushwanchoo/Library/CloudStorage/OneDrive-JohnsHopkins/Malon_PDV_scope/Cu_Polycrystals/Cu_100nm/20241205_varying_velocity_spall",
                out_files_dir="/Users/piyushwanchoo/Library/CloudStorage/OneDrive-JohnsHopkins/Malon_PDV_scope/Cu_Polycrystals/Cu_100nm/20241205_varying_velocity_spall/Output",
                display_plots="yes",
                spall_calculation="yes",
                plot_figsize=(30, 10),
                plot_dpi=300,
            )


if __name__ == "__main__":
    w = Watcher()
    w.run()

# %%
