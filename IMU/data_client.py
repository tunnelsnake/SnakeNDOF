import receivefile
import data_parser
import clear_logs
import data_plot

c = clear_logs.Clear_logs()

input("Press A Key To Begin Data Reception")

rf = receivefile.Receivefile()
dp = data_parser.Data_parser()
plot = data_plot.Data_plot()