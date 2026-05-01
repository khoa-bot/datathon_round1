# [EN] Import pandas for data manipulation and tabular data analysis.
# [VN] Nhập thư viện pandas để xử lý và phân tích dữ liệu dạng bảng.
import pandas as pd

# [EN] Import os to interact with the operating system, such as setting environment variables.
# [VN] Nhập thư viện os để tương tác với hệ điều hành, ví dụ như thiết lập biến môi trường.
import os

# [EN] Import random to control Python's built-in random number generation.
# [VN] Nhập thư viện random để kiểm soát việc tạo số ngẫu nhiên được tích hợp sẵn của Python.
import random

# [EN] Import numpy for numerical operations and array processing.
# [VN] Nhập thư viện numpy cho các phép toán số học và xử lý mảng.
import numpy as np

# [EN] Import pyplot from matplotlib for plotting charts and data visualization.
# [VN] Nhập pyplot từ matplotlib để vẽ biểu đồ và trực quan hóa dữ liệu.
import matplotlib.pyplot as plt

# [EN] Import regression metrics from scikit-learn to evaluate model performance.
# [VN] Nhập các số liệu đánh giá hồi quy từ scikit-learn để đo lường hiệu suất mô hình.
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# [EN] Import scalers from scikit-learn to normalize data ranges.
# [VN] Nhập các bộ chia tỷ lệ từ scikit-learn để chuẩn hóa phạm vi dữ liệu.
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# [EN] Import XGBRegressor, a powerful gradient boosting algorithm from xgboost.
# [VN] Nhập XGBRegressor, một thuật toán tăng cường gradient mạnh mẽ từ xgboost.
from xgboost import XGBRegressor

# [EN] Import Pipeline to chain together multiple data processing steps.
# [VN] Nhập Pipeline để kết nối chuỗi nhiều bước xử lý dữ liệu với nhau.
from sklearn.pipeline import Pipeline

# [EN] Import shap for explainable AI and determining feature importance.
# [VN] Nhập shap cho AI có thể giải thích được và xác định mức độ quan trọng của đặc trưng.
import shap

# [EN] Import sys to access system-specific parameters and Python versions.
# [VN] Nhập sys để truy cập các tham số dành riêng cho hệ thống và phiên bản Python.
import sys

# [EN] Import matplotlib base library to track its version.
# [VN] Nhập thư viện cơ sở matplotlib để theo dõi phiên bản của nó.
import matplotlib

# [EN] Import sklearn base library to track its version.
# [VN] Nhập thư viện cơ sở sklearn để theo dõi phiên bản của nó.
import sklearn

# [EN] Import platform to access OS/platform architecture information.
# [VN] Nhập thư viện platform để truy cập thông tin kiến trúc nền tảng/hệ điều hành.
import platform

# [EN] Import seaborn for statistical data visualization.
# [VN] Nhập thư viện seaborn cho trực quan hóa dữ liệu thống kê.
import seaborn as sns

# [EN] Import theilslopes from scipy for robust linear regression to ignore outliers.
# [VN] Nhập theilslopes từ scipy cho hồi quy tuyến tính mạnh mẽ để bỏ qua các điểm dị biệt.
from scipy.stats import theilslopes

# [EN] Define a function to capture and save the versions of all major libraries.
# [VN] Định nghĩa một hàm để thu thập và lưu các phiên bản của tất cả các thư viện chính.
def log_library_versions(report_file='report.txt'):
    """
    [EN] Captures and records the versions of the Python interpreter and all major libraries used in the environment.
    [VN] Ghi lại và lưu trữ các phiên bản của trình thông dịch Python và tất cả các thư viện chính được sử dụng trong môi trường.
    """
    # [EN] Create a list of tuples containing library names and their respective version strings.
    # [VN] Tạo một danh sách các bộ giá trị chứa tên thư viện và chuỗi phiên bản tương ứng của chúng.
    versions = [
        # [EN] Python version record.
        # [VN] Bản ghi phiên bản Python.
        ("Python", sys.version),
        # [EN] Operating System platform record.
        # [VN] Bản ghi nền tảng Hệ điều hành.
        ("Platform", platform.platform()),
        # [EN] Pandas version record.
        # [VN] Bản ghi phiên bản Pandas.
        ("Pandas", pd.__version__),
        # [EN] NumPy version record.
        # [VN] Bản ghi phiên bản NumPy.
        ("NumPy", np.__version__),
        # [EN] Matplotlib version record.
        # [VN] Bản ghi phiên bản Matplotlib.
        ("Matplotlib", matplotlib.__version__),
        # [EN] Seaborn version record.
        # [VN] Bản ghi phiên bản Seaborn.
        ("Seaborn", sns.__version__),
        # [EN] Scikit-Learn version record.
        # [VN] Bản ghi phiên bản Scikit-Learn.
        ("Scikit-Learn", sklearn.__version__),
        # [EN] SHAP version record.
        # [VN] Bản ghi phiên bản SHAP.
        ("SHAP", shap.__version__)
    ]

    # [EN] Construct the header string for the version report using string multiplication.
    # [VN] Xây dựng chuỗi tiêu đề cho báo cáo phiên bản bằng phép nhân chuỗi.
    header = "\n" + "="*50 + "\nENVIRONMENT & LIBRARY VERSIONS\n" + "="*50 + "\n"
    
    # [EN] Print the header to the console.
    # [VN] In tiêu đề ra màn hình console.
    print(header)
    
    # [EN] Open the specified report file in append mode.
    # [VN] Mở tệp báo cáo được chỉ định ở chế độ ghi nối thêm.
    with open(report_file, 'a') as f:
        # [EN] Write the header to the file.
        # [VN] Ghi tiêu đề vào tệp.
        f.write(header)
        
        # [EN] Iterate through the version list.
        # [VN] Lặp qua danh sách phiên bản.
        for name, version in versions:
            # [EN] Format each line with consistent padding for readability.
            # [VN] Định dạng mỗi dòng với khoảng cách lề nhất quán để dễ đọc.
            line = f"{name:<15}: {version}"
            
            # [EN] Display the formatted line in console.
            # [VN] Hiển thị dòng đã định dạng trên màn hình console.
            print(line)
            
            # [EN] Append the line to the file, followed by a newline.
            # [VN] Thêm dòng này vào tệp, theo sau là một ký tự xuống dòng.
            f.write(line + "\n")
            
    # [EN] Create a closing separator.
    # [VN] Tạo một dải phân cách kết thúc.
    footer = "="*50 + "\n"
    
    # [EN] Print the footer to console.
    # [VN] In phần kết thúc ra console.
    print(footer)
    
    # [EN] Re-open the file to append the footer.
    # [VN] Mở lại tệp để ghi nối thêm phần kết thúc.
    with open(report_file, 'a') as f:
        # [EN] Write the footer to the report file.
        # [VN] Ghi phần kết thúc vào tệp báo cáo.
        f.write(footer)

# [EN] Execute the version logging function immediately upon script start.
# [VN] Thực thi hàm ghi nhật ký phiên bản ngay lập tức khi bắt đầu kịch bản.
log_library_versions()

# [EN] Define a utility function to print text and append it to a log file.
# [VN] Định nghĩa một hàm tiện ích để in văn bản và nối nó vào tệp nhật ký.
def write_report(text):
    """
    [EN] Writes the provided text to a log file ('report.txt') and prints it to the console for real-time tracking.
    [VN] Ghi đoạn văn bản được cung cấp vào tệp nhật ký ('report.txt') và in ra màn hình console để theo dõi thời gian thực.
    """
    # [EN] Open 'report.txt' in append mode ('a') so previous contents are not overwritten.
    # [VN] Mở tệp 'report.txt' ở chế độ nối thêm ('a') để nội dung trước đó không bị ghi đè.
    with open('report.txt', 'a') as f:
        # [EN] Print to the standard output (console).
        # [VN] In ra đầu ra tiêu chuẩn (màn hình console).
        print(text)
        
        # [EN] Write the text into the file, appending a newline character at the end.
        # [VN] Ghi văn bản vào tệp, thêm ký tự xuống dòng ở cuối.
        f.write(text + '\n')
        
# [EN] Define a dummy logging function to suppress output when needed.
# [VN] Định nghĩa một hàm ghi nhật ký giả để chặn đầu ra khi cần thiết.
def write_report_false(text):
    """
    [EN] A dummy function that acts as a placeholder to suppress output printing and writing.
    [VN] Một hàm giả hoạt động như một trình giữ chỗ để chặn việc in và ghi đầu ra.
    """
    # [EN] Execute nothing (pass statement).
    # [VN] Không thực thi gì cả (lệnh pass).
    pass

# [EN] Define a constant SEED value to ensure consistent randomized operations.
# [VN] Định nghĩa một hằng số SEED để đảm bảo các hoạt động ngẫu nhiên diễn ra nhất quán.
SEED = 36

# [EN] Define a function to lock all random generators to the provided seed.
# [VN] Định nghĩa một hàm để khóa tất cả các bộ tạo số ngẫu nhiên bằng hạt giống được cung cấp.
def set_reproducibility(seed_value=36):
    """
    [EN] Fixes all possible sources of randomness to ensure identical results across multiple runs.
    [VN] Cố định tất cả các nguồn ngẫu nhiên có thể có để đảm bảo kết quả giống hệt nhau qua nhiều lần chạy.
    """
    # [EN] Set Python hash seed environment variable to the seed value.
    # [VN] Đặt biến môi trường hạt giống băm của Python thành giá trị hạt giống.
    os.environ['PYTHONHASHSEED'] = str(seed_value)
    
    # [EN] Set the built-in random module seed.
    # [VN] Đặt hạt giống cho mô-đun random tích hợp sẵn.
    random.seed(seed_value)
    
    # [EN] Set the numpy random number generator seed.
    # [VN] Đặt hạt giống cho bộ tạo số ngẫu nhiên của numpy.
    np.random.seed(seed_value)

# [EN] Execute the reproducibility setup immediately using the predefined SEED.
# [VN] Thực thi thiết lập tái lập ngay lập tức bằng cách sử dụng SEED đã được định nghĩa trước.
set_reproducibility(SEED)

# [EN] Load the dataset from 'sales.csv' into a pandas DataFrame.
# [VN] Tải tập dữ liệu từ 'sales.csv' vào pandas DataFrame.
sales = pd.read_csv('sales.csv')

# [EN] Convert the 'Date' column from string format to pandas datetime objects.
# [VN] Chuyển đổi cột 'Date' từ định dạng chuỗi sang đối tượng datetime của pandas.
sales['Date'] = pd.to_datetime(sales['Date'])

# [EN] Define a function to extract multiple time-based features from the Date column.
# [VN] Định nghĩa một hàm để trích xuất nhiều đặc trưng dựa trên thời gian từ cột Date.
def create_time_features(df):
    """
    [EN] Generates time-series features (e.g., year, month, cyclical features) based on the 'Date' column.
    [VN] Tạo các đặc trưng chuỗi thời gian (ví dụ: năm, tháng, các đặc trưng chu kỳ) dựa trên cột 'Date'.
    """
    # [EN] Create a copy of the dataframe to avoid setting with copy warnings.
    # [VN] Tạo một bản sao của dataframe để tránh cảnh báo gán giá trị trên bản sao.
    df = df.copy()
    
    # [EN] Extract the year from the date.
    # [VN] Trích xuất năm từ ngày tháng.
    df["year"] = df["Date"].dt.year
    
    # [EN] Extract the month number (1-12).
    # [VN] Trích xuất số tháng (1-12).
    df["month"] = df["Date"].dt.month
    
    # [EN] Extract the day of the month (1-31).
    # [VN] Trích xuất ngày trong tháng (1-31).
    df["day"] = df["Date"].dt.day
    
    # [EN] Extract the day of the week (0 = Monday, 6 = Sunday).
    # [VN] Trích xuất ngày trong tuần (0 = Thứ Hai, 6 = Chủ Nhật).
    df["dayofweek"] = df["Date"].dt.dayofweek
    
    # [EN] Extract the day of the year (1-365/366).
    # [VN] Trích xuất ngày trong năm (1-365/366).
    df["dayofyear"] = df["Date"].dt.dayofyear
    
    # [EN] Extract the ISO calendar week number and cast it to integer.
    # [VN] Trích xuất số tuần theo lịch ISO và chuyển sang kiểu số nguyên.
    df["weekofyear"] = df["Date"].dt.isocalendar().week.astype(int)
    
    # [EN] Extract the financial/calendar quarter (1-4).
    # [VN] Trích xuất quý tài chính/lịch (1-4).
    df["quarter"] = df["Date"].dt.quarter
    
    # [EN] Create a binary feature checking if the day is a weekend (Saturday or Sunday).
    # [VN] Tạo đặc trưng nhị phân kiểm tra xem ngày đó có phải là cuối tuần không (Thứ Bảy hoặc Chủ Nhật).
    df["is_weekend"] = (df["dayofweek"] >= 5).astype(int)
    
    # [EN] Create a binary feature checking if it is the first day of a month.
    # [VN] Tạo đặc trưng nhị phân kiểm tra xem đó có phải là ngày đầu tiên của tháng không.
    df["is_month_start"] = df["Date"].dt.is_month_start.astype(int)
    
    # [EN] Create a binary feature checking if it is the last day of a month.
    # [VN] Tạo đặc trưng nhị phân kiểm tra xem đó có phải là ngày cuối cùng của tháng không.
    df["is_month_end"] = df["Date"].dt.is_month_end.astype(int)
    
    # [EN] Generate cyclical sine feature for the month.
    # [VN] Tạo đặc trưng hình sin chu kỳ cho tháng.
    df["month_sin"] = np.sin(2 * np.pi * df["month"] / 12)
    
    # [EN] Generate cyclical cosine feature for the month.
    # [VN] Tạo đặc trưng hình cos chu kỳ cho tháng.
    df["month_cos"] = np.cos(2 * np.pi * df["month"] / 12)
    
    # [EN] Generate cyclical sine feature for the day of week.
    # [VN] Tạo đặc trưng hình sin chu kỳ cho ngày trong tuần.
    df["dow_sin"] = np.sin(2 * np.pi * df["dayofweek"] / 7)
    
    # [EN] Generate cyclical cosine feature for the day of week.
    # [VN] Tạo đặc trưng hình cos chu kỳ cho ngày trong tuần.
    df["dow_cos"] = np.cos(2 * np.pi * df["dayofweek"] / 7)
    
    # [EN] Generate 1st order cyclical sine feature for the day of year.
    # [VN] Tạo đặc trưng hình sin chu kỳ bậc 1 cho ngày trong năm.
    df["year_sin_1"] = np.sin(2 * np.pi * df["dayofyear"] / 365.25)
    
    # [EN] Generate 1st order cyclical cosine feature for the day of year.
    # [VN] Tạo đặc trưng hình cos chu kỳ bậc 1 cho ngày trong năm.
    df["year_cos_1"] = np.cos(2 * np.pi * df["dayofyear"] / 365.25)
    
    # [EN] Generate 2nd order cyclical sine feature for the day of year (bi-annual).
    # [VN] Tạo đặc trưng hình sin chu kỳ bậc 2 cho ngày trong năm (bán niên).
    df["year_sin_2"] = np.sin(4 * np.pi * df["dayofyear"] / 365.25)
    
    # [EN] Generate 2nd order cyclical cosine feature for the day of year (bi-annual).
    # [VN] Tạo đặc trưng hình cos chu kỳ bậc 2 cho ngày trong năm (bán niên).
    df["year_cos_2"] = np.cos(4 * np.pi * df["dayofyear"] / 365.25)
    
    # [EN] NEW FEATURE: isCovid (0 for before 2019, 1 for 2019 onward)
    # [VN] ĐẶC TRƯNG MỚI: isCovid (0 cho trước 2019, 1 cho 2019 trở đi)
    df["isCovid"] = (df["year"] >= 2019).astype(int)
    
    # [EN] Return the DataFrame augmented with the new features.
    # [VN] Trả về DataFrame đã được tăng cường với các đặc trưng mới.
    return df

# [EN] Prepare Features for the training dataset.
# [VN] Chuẩn bị các đặc trưng cho tập dữ liệu huấn luyện.
train_df = create_time_features(sales)

# [EN] Define the list of column names that will be used as input features for the model.
# [VN] Định nghĩa danh sách các tên cột sẽ được sử dụng làm đặc trưng đầu vào cho mô hình.
feature_cols = [
    # [EN] Basic calendar variables.
    # [VN] Các biến lịch cơ bản.
    "year", "month", "day", "dayofweek", "dayofyear", "weekofyear", "quarter",
    # [EN] Binary categorical date features.
    # [VN] Các đặc trưng ngày tháng phân loại nhị phân.
    "is_weekend", "is_month_start", "is_month_end",
    # [EN] Monthly cyclical features.
    # [VN] Các đặc trưng chu kỳ hàng tháng.
    "month_sin", "month_cos",
    # [EN] Weekly cyclical features.
    # [VN] Các đặc trưng chu kỳ hàng tuần.
    "dow_sin", "dow_cos",
    # [EN] Yearly cyclical features (annual and bi-annual).
    # [VN] Các đặc trưng chu kỳ hàng năm (thường niên và bán niên).
    "year_sin_1", "year_cos_1", "year_sin_2", "year_cos_2",
    # [EN] Indicator feature to capture the structural shift starting from 2019.
    # [VN] Đặc trưng chỉ báo để nắm bắt sự thay đổi cấu trúc bắt đầu từ năm 2019.
    "isCovid"
]

# [EN] Write a header logging the used features to the report.
# [VN] Ghi một tiêu đề nhật ký các đặc trưng đã sử dụng vào báo cáo.
write_report("Features used:")

# [EN] Write the string representation of the feature columns list to the report.
# [VN] Ghi dạng chuỗi của danh sách các cột đặc trưng vào báo cáo.
write_report(str(feature_cols))

# [EN] Initialize an empty list to store Mean Absolute Error values.
# [VN] Khởi tạo một danh sách trống để lưu trữ các giá trị Sai số Tuyệt đối Trung bình (MAE).
MAE = []

# [EN] Initialize an empty list to store Root Mean Squared Error values.
# [VN] Khởi tạo một danh sách trống để lưu trữ các giá trị Căn bậc hai Sai số Toàn phương Trung bình (RMSE).
RMSE = []

# [EN] Initialize an empty list to store R-squared (coefficient of determination) values.
# [VN] Khởi tạo một danh sách trống để lưu trữ các giá trị R-bình phương (hệ số xác định).
R2 = []

# [EN] Initialize a variable to keep track of the most recently trained model.
# [VN] Khởi tạo một biến để theo dõi mô hình được huấn luyện gần đây nhất.
last_trained_model = None

# [EN] Initialize a variable to store the latest training features used (for SHAP).
# [VN] Khởi tạo một biến để lưu trữ các đặc trưng huấn luyện mới nhất được sử dụng (cho SHAP).
last_train_features = None

# [EN] Define the cross-validation function that tests the model over expanding time windows.
# [VN] Định nghĩa hàm xác thực chéo kiểm tra mô hình qua các cửa sổ thời gian mở rộng.
def perform_cross_testing(valid_start, write_report=write_report):
    """
    [EN] Performs a single fold of time-series cross-validation.
    [VN] Thực hiện một nếp gấp (fold) của xác thực chéo chuỗi thời gian.
    """
    # [EN] Segment the training portion containing all dates before the validation start date.
    # [VN] Phân đoạn phần huấn luyện chứa tất cả các ngày trước ngày bắt đầu xác thực.
    train_part = train_df[train_df["Date"] < valid_start].copy()
    
    # [EN] Segment the validation portion containing dates starting from valid_start up to 12 months ahead.
    # [VN] Phân đoạn phần xác thực chứa các ngày bắt đầu từ valid_start lên đến 12 tháng sau.
    valid_part = train_df[(train_df["Date"] >= valid_start) & (train_df["Date"] < pd.to_datetime(valid_start) + pd.DateOffset(months=12))].copy()

    # [EN] Extract the input features for the training slice.
    # [VN] Trích xuất các đặc trưng đầu vào cho phần huấn luyện.
    X_train = train_part[feature_cols]
    
    # [EN] Extract the input features for the validation slice.
    # [VN] Trích xuất các đặc trưng đầu vào cho phần xác thực.
    X_valid = valid_part[feature_cols]

    # [EN] Extract the raw revenue target array for training and reshape for the scaler.
    # [VN] Trích xuất mảng mục tiêu doanh thu thô cho huấn luyện và định hình lại cho bộ chia tỷ lệ.
    y_train_raw = train_part["Revenue"].values.reshape(-1, 1)
    
    # [EN] Initialize a MinMaxScaler to normalize the target values between 0 and 1.
    # [VN] Khởi tạo MinMaxScaler để chuẩn hóa các giá trị mục tiêu trong khoảng từ 0 đến 1.
    target_scaler = MinMaxScaler()
    
    # [EN] Fit the scaler on the training targets and transform them into scaled values.
    # [VN] Khớp bộ chia tỷ lệ vào các mục tiêu huấn luyện và chuyển đổi chúng thành các giá trị đã chia tỷ lệ.
    y_train = target_scaler.fit_transform(y_train_raw).ravel()

    # [EN] Extract the raw revenue target array for the validation slice (no scaling needed for truth).
    # [VN] Trích xuất mảng mục tiêu doanh thu thô cho phần xác thực (không cần chia tỷ lệ cho giá trị thực).
    y_valid = valid_part["Revenue"].values

    # [EN] Log the temporal range of the training period.
    # [VN] Ghi nhật ký phạm vi thời gian của kỳ huấn luyện.
    write_report(f"\nTraining period: {train_part['Date'].min()} to {train_part['Date'].max()}")
    
    # [EN] Log the temporal range of the validation period.
    # [VN] Ghi nhật ký phạm vi thời gian của kỳ xác thực.
    write_report(f"Validation period: {valid_part['Date'].min()} to {valid_part['Date'].max()}")

    # [EN] Initialize a dictionary to store local models if needed.
    # [VN] Khởi tạo một từ điển để lưu trữ các mô hình cục bộ nếu cần.
    models = {}
    
    # [EN] Initialize a dictionary to store local predictions.
    # [VN] Khởi tạo một từ điển để lưu trữ các dự đoán cục bộ.
    predictions = {}

    # [EN] Model updated to strictly use n_estimators=140 and learning_rate=0.03
    # [VN] Mô hình được cập nhật để chỉ sử dụng nghiêm ngặt n_estimators=140 và learning_rate=0.03
    revenue_model_gb = Pipeline([
        # [EN] First pipeline step: Scale input features to standard normal distribution.
        # [VN] Bước đầu tiên của quy trình: Chia tỷ lệ các đặc trưng đầu vào theo phân phối chuẩn tiêu chuẩn.
        ("scaler", StandardScaler()), 
        # [EN] Second pipeline step: The XGBoost regressor model with strict predetermined hyperparameters.
        # [VN] Bước thứ hai của quy trình: Mô hình hồi quy XGBoost với các siêu tham số được xác định trước nghiêm ngặt.
        ("model", XGBRegressor(
            # [EN] Device target: CPU execution.
            # [VN] Mục tiêu thiết bị: thực thi trên CPU.
            device='cpu', 
            # [EN] Restrict to 1 thread to ensure deterministic behavior.
            # [VN] Hạn chế 1 luồng để đảm bảo hành vi mang tính xác định.
            n_jobs=1, 
            # [EN] Number of boosting trees.
            # [VN] Số lượng cây tăng cường.
            n_estimators=140, 
            # [EN] Step size shrinkage used in update to prevents overfitting.
            # [VN] Kích thước bước thu hẹp được sử dụng trong bản cập nhật để ngăn ngừa quá khớp.
            learning_rate=0.03, 
            # [EN] Exact greedy algorithm for tree building (more accurate, slower).
            # [VN] Thuật toán tham lam chính xác để xây dựng cây (chính xác hơn, chậm hơn).
            tree_method='exact', 
            # [EN] Maximum tree depth.
            # [VN] Độ sâu tối đa của cây.
            max_depth=5, 
            # [EN] Random seed for reproducibility.
            # [VN] Hạt giống ngẫu nhiên để tái lập.
            random_state=SEED, 
            # [EN] Subsample ratio of columns for each level.
            # [VN] Tỷ lệ mẫu phụ của các cột cho mỗi cấp độ.
            colsample_bylevel=0.8, 
            # [EN] Subsample ratio of columns when constructing each tree.
            # [VN] Tỷ lệ mẫu phụ của các cột khi xây dựng mỗi cây.
            colsample_bytree=0.5, 
            # [EN] L1 regularization term on weights.
            # [VN] Hệ số điều chuẩn L1 trên các trọng số.
            reg_alpha=0.1, 
            # [EN] L2 regularization term on weights.
            # [VN] Hệ số điều chuẩn L2 trên các trọng số.
            reg_lambda=4.0, 
            # [EN] Evaluation metric set to Root Mean Square Error.
            # [VN] Số liệu đánh giá được đặt thành Căn bậc hai của Sai số Bình phương Trung bình.
            eval_metric='rmse'
        ))
    ])
    
    # [EN] Fit the pipeline on the training data and scaled target variable.
    # [VN] Huấn luyện quy trình trên dữ liệu huấn luyện và biến mục tiêu đã được chia tỷ lệ.
    revenue_model_gb.fit(X_train, y_train)
    
    # [EN] Predict raw (scaled) validation target variables using the trained model.
    # [VN] Dự đoán các biến mục tiêu xác thực (đã được chia tỷ lệ) thô bằng cách sử dụng mô hình đã huấn luyện.
    valid_pred_raw_gb = revenue_model_gb.predict(X_valid)
    
    # [EN] Inverse transform the predictions back to the original revenue scale.
    # [VN] Chuyển đổi ngược các dự đoán trở lại thang đo doanh thu ban đầu.
    valid_pred_gb = target_scaler.inverse_transform(valid_pred_raw_gb.reshape(-1, 1)).ravel()
    
    # [EN] Ensure no predictions are negative by capping the minimum value at 0.
    # [VN] Đảm bảo không có dự đoán nào âm bằng cách giới hạn giá trị tối thiểu ở mức 0.
    predictions["GradientBoosting"] = np.maximum(valid_pred_gb, 0)

    # [EN] Print a header for the validation results section.
    # [VN] In một tiêu đề cho phần kết quả xác thực.
    write_report(f"\n===== Validation Results: Revenue =====")
    
    # [EN] Calculate the Mean Absolute Error between actuals and predictions.
    # [VN] Tính toán Sai số Tuyệt đối Trung bình giữa giá trị thực tế và giá trị dự đoán.
    mae = mean_absolute_error(y_valid, valid_pred_gb)
    
    # [EN] Calculate the Root Mean Squared Error between actuals and predictions.
    # [VN] Tính toán Căn bậc hai Sai số Toàn phương Trung bình giữa giá trị thực tế và giá trị dự đoán.
    rmse = mean_squared_error(y_valid, valid_pred_gb) ** 0.5
    
    # [EN] Calculate the R2 Score (coefficient of determination).
    # [VN] Tính Điểm R2 (hệ số xác định).
    r2 = r2_score(y_valid, valid_pred_gb)

    # [EN] Log the final computed metrics to the report file and console.
    # [VN] Ghi nhật ký các số liệu đã tính toán cuối cùng vào tệp báo cáo và màn hình console.
    write_report(f"\nValidation Results:")
    write_report(f"  MAE : {mae:.2f}")
    write_report(f"  RMSE: {rmse:.2f}")
    write_report(f"  R2  : {r2:.4f}")
    
    # [EN] Append the fold's MAE to the global list for later aggregation.
    # [VN] Thêm MAE của nếp gấp vào danh sách chung để tổng hợp sau.
    MAE.append(mae)
    
    # [EN] Append the fold's RMSE to the global list for later aggregation.
    # [VN] Thêm RMSE của nếp gấp vào danh sách chung để tổng hợp sau.
    RMSE.append(rmse)
    
    # [EN] Append the fold's R2 to the global list for later aggregation.
    # [VN] Thêm R2 của nếp gấp vào danh sách chung để tổng hợp sau.
    R2.append(r2)
    
    # ==========================================
    # ADDED CODE: Plotting Prediction vs Truth
    # ==========================================
    # [EN] Format the validation start date into a string for title and filename uses.
    # [VN] Định dạng ngày bắt đầu xác thực thành một chuỗi để sử dụng cho tiêu đề và tên tệp.
    date_str = pd.to_datetime(valid_start).strftime('%Y-%m-%d')
    
    # [EN] Initialize a matplotlib figure with a specific size (width=14, height=6).
    # [VN] Khởi tạo một hình matplotlib với kích thước cụ thể (chiều rộng=14, chiều cao=6).
    plt.figure(figsize=(14, 6))
    
    # [EN] Plot the actual valid revenues as a solid blue line.
    # [VN] Vẽ doanh thu hợp lệ thực tế dưới dạng một đường nét liền màu xanh dương.
    plt.plot(valid_part['Date'], y_valid, label='Actual Revenue (Truth)', color='dodgerblue', linewidth=2)
    
    # [EN] Plot the XGBoost predictions as a dashed orange line.
    # [VN] Vẽ các dự đoán của XGBoost dưới dạng một đường đứt nét màu cam.
    plt.plot(valid_part['Date'], valid_pred_gb, label='GBM Prediction', color='darkorange', linewidth=2, linestyle='--')
    
    # [EN] Set the main title of the plot showing the validation start date.
    # [VN] Đặt tiêu đề chính của biểu đồ hiển thị ngày bắt đầu xác thực.
    plt.title(f"Prediction vs Truth - 12 Month Validation Window (Start: {date_str})")
    
    # [EN] Set the label for the X-axis.
    # [VN] Đặt nhãn cho trục X.
    plt.xlabel("Date")
    
    # [EN] Set the label for the Y-axis.
    # [VN] Đặt nhãn cho trục Y.
    plt.ylabel("Revenue")
    
    # [EN] Add a legend in the upper left corner to differentiate the lines.
    # [VN] Thêm chú giải ở góc trên bên trái để phân biệt các đường biểu diễn.
    plt.legend(loc='upper left')
    
    # [EN] Enable a light background grid for easier value reading.
    # [VN] Bật một lưới nền nhạt để đọc giá trị dễ dàng hơn.
    plt.grid(True, alpha=0.3)
    
    # [EN] Format the output filename for the current validation fold's plot.
    # [VN] Định dạng tên tệp đầu ra cho biểu đồ của nếp gấp xác thực hiện tại.
    filename = f"pred_vs_truth_val_start_{date_str}.png"
    
    # [EN] Save the generated plot to the disk as a PNG file.
    # [VN] Lưu biểu đồ đã tạo vào đĩa dưới dạng tệp PNG.
    plt.savefig(filename, bbox_inches='tight', dpi=150)
    
    # [EN] Display the plot momentarily (if running interactively).
    # [VN] Hiển thị biểu đồ trong chốc lát (nếu chạy tương tác).
    plt.show()
    
    # [EN] Close the plot to free memory.
    # [VN] Đóng biểu đồ để giải phóng bộ nhớ.
    plt.close()
    
    # [EN] Return the fully trained model, feature subset, and fitted target scaler for external use.
    # [VN] Trả về mô hình đã huấn luyện hoàn chỉnh, tập hợp con đặc trưng và bộ chia tỷ lệ mục tiêu đã khớp để sử dụng bên ngoài.
    return revenue_model_gb, X_train, target_scaler

# [EN] Iterate through a monthly date range (Start of Month frequency) from Jan 2021 to June 2022.
# [VN] Lặp qua phạm vi ngày hàng tháng (Tần suất đầu tháng) từ tháng 1 năm 2021 đến tháng 6 năm 2022.
for valid_start in pd.date_range('2021-01-01', '2022-06-01', freq='MS'):
    # [EN] Execute the cross validation routine for each computed monthly start date.
    # [VN] Thực thi quy trình xác thực chéo cho mỗi ngày bắt đầu hàng tháng đã tính toán.
    perform_cross_testing(valid_start)

# [EN] Compute and print average overall MAE metrics.
# [VN] Tính toán và in các chỉ số MAE tổng thể trung bình.
write_report(f"Average MAE: {np.mean(MAE):.2f}")

# [EN] Compute and print average overall RMSE metrics.
# [VN] Tính toán và in các chỉ số RMSE tổng thể trung bình.
write_report(f"Average RMSE: {np.mean(RMSE):.2f}")

# [EN] Compute and print average overall R2 metrics.
# [VN] Tính toán và in các chỉ số R2 tổng thể trung bình.
write_report(f"Average R2: {np.mean(R2):.4f}")

# [EN] Calculate and print standard dev, minimum, maximum, and median for MAE across all folds.
# [VN] Tính toán và in độ lệch chuẩn, tối thiểu, tối đa và trung vị cho MAE trên tất cả các nếp gấp.
write_report(f"MAE - Std: {np.std(MAE):.2f}, Min: {np.min(MAE):.2f}, Max: {np.max(MAE):.2f}, Median: {np.median(MAE):.2f}")

# [EN] Calculate and print standard dev, minimum, maximum, and median for RMSE across all folds.
# [VN] Tính toán và in độ lệch chuẩn, tối thiểu, tối đa và trung vị cho RMSE trên tất cả các nếp gấp.
write_report(f"RMSE - Std: {np.std(RMSE):.2f}, Min: {np.min(RMSE):.2f}, Max: {np.max(RMSE):.2f}, Median: {np.median(RMSE):.2f}")

# [EN] Calculate and print standard dev, minimum, maximum, and median for R2 across all folds.
# [VN] Tính toán và in độ lệch chuẩn, tối thiểu, tối đa và trung vị cho R2 trên tất cả các nếp gấp.
write_report(f"R2 - Std: {np.std(R2):.4f}, Min: {np.min(R2):.4f}, Max: {np.max(R2):.4f}, Median: {np.median(R2):.4f}")

# [EN] Perform a final training run using all data before Dec 31, 2022, suppressing the log output.
# [VN] Thực hiện một lần huấn luyện cuối cùng sử dụng tất cả dữ liệu trước ngày 31 tháng 12 năm 2022, chặn đầu ra nhật ký.
last_trained_model, last_train_features, last_scaler = perform_cross_testing(pd.to_datetime('2022-12-31'), write_report_false)

# [EN] Check if the model has successfully been trained and features saved before running SHAP.
# [VN] Kiểm tra xem mô hình đã được huấn luyện thành công và các đặc trưng đã được lưu trước khi chạy SHAP chưa.
if last_trained_model is not None and last_train_features is not None:
    # [EN] Write section header for the SHAP explanation block.
    # [VN] Viết tiêu đề phần cho khối giải thích SHAP.
    write_report("\n===== SHAP Explanation for the Most Recent Model =====")
    
    # [EN] Log context that we are using the final trained model and training features as SHAP background.
    # [VN] Ghi chú ngữ cảnh rằng chúng ta đang sử dụng mô hình huấn luyện cuối cùng và đặc trưng huấn luyện làm nền SHAP.
    write_report("Using the last trained GradientBoosting model and the training feature set as the background dataset.")
    
    # [EN] Instantiate SHAP TreeExplainer passing the inner XGBoost model and the scaled training background data.
    # [VN] Khởi tạo SHAP TreeExplainer truyền vào mô hình XGBoost bên trong và dữ liệu nền huấn luyện đã chia tỷ lệ.
    explainer = shap.Explainer(
        last_trained_model.named_steps["model"],
        last_trained_model.named_steps["scaler"].transform(last_train_features)
    )
    
    # [EN] Compute SHAP values for all instances in the scaled training dataset.
    # [VN] Tính toán các giá trị SHAP cho tất cả các phiên bản trong tập dữ liệu huấn luyện đã chia tỷ lệ.
    shap_values = explainer(last_trained_model.named_steps["scaler"].transform(last_train_features))
    
    # [EN] Log success of SHAP value computation.
    # [VN] Ghi nhật ký thành công của việc tính toán giá trị SHAP.
    write_report("SHAP values computed for the training background dataset.")
    
    # [EN] Extract the base value (expected value) representing average model prediction before feature impacts.
    # [VN] Trích xuất giá trị cơ sở (giá trị kỳ vọng) đại diện cho dự đoán trung bình của mô hình trước các tác động đặc trưng.
    base_value = explainer.expected_value
    
    # [EN] Log the extracted expected base value.
    # [VN] Ghi nhật ký giá trị cơ sở kỳ vọng đã trích xuất.
    write_report(f"Model base value (expected output before feature contributions): {base_value}")

    # [EN] Compute the mean absolute SHAP value for each feature across the entire dataset.
    # [VN] Tính giá trị SHAP tuyệt đối trung bình cho mỗi đặc trưng trên toàn bộ tập dữ liệu.
    mean_abs_shap = np.abs(shap_values.values).mean(axis=0)
    
    # [EN] Create a sorted list of features based on their overall importance (mean absolute SHAP).
    # [VN] Tạo một danh sách các đặc trưng được sắp xếp dựa trên tầm quan trọng tổng thể của chúng (SHAP tuyệt đối trung bình).
    feature_importance = sorted(zip(feature_cols, mean_abs_shap), key=lambda x: x[1], reverse=True)

    # [EN] Log the start of the feature importance ranking output.
    # [VN] Ghi nhật ký phần đầu của kết quả xếp hạng tầm quan trọng của đặc trưng.
    write_report("\nFeature importance ranking based on mean absolute SHAP values:")
    
    # [EN] Loop through the entire feature importance list and format to console/file.
    # [VN] Lặp qua toàn bộ danh sách tầm quan trọng của đặc trưng và định dạng ra màn hình console/tệp.
    for feature, importance in feature_importance:
        # [EN] Log individual feature and its mean importance value.
        # [VN] Ghi nhật ký từng đặc trưng và giá trị quan trọng trung bình của nó.
        write_report(f"  {feature:>12}: {importance:.6f}")

    # [EN] Highlight and log only the top 5 most important features for a quick summary.
    # [VN] Nêu bật và ghi lại chỉ 5 đặc trưng quan trọng nhất để có một bản tóm tắt nhanh.
    write_report("\nTop 5 features by average SHAP impact:")
    
    # [EN] Iterate through the top 5 elements of the sorted importance list.
    # [VN] Lặp qua 5 phần tử trên cùng của danh sách mức độ quan trọng đã sắp xếp.
    for feature, importance in feature_importance[:5]:
        # [EN] Log individual top feature and its mean importance value.
        # [VN] Ghi nhật ký từng đặc trưng hàng đầu và giá trị quan trọng trung bình của nó.
        write_report(f"  {feature:>12}: {importance:.6f}")

    # [EN] Pick a specific sample row index (limit to 3, or max array size) to provide a local explanation.
    # [VN] Chọn một chỉ số hàng mẫu cụ thể (giới hạn là 3, hoặc kích thước mảng tối đa) để cung cấp giải thích cục bộ.
    sample_index = min(3, last_train_features.shape[0] - 1)
    
    # [EN] Extract the specific calendar Date of the chosen sample.
    # [VN] Trích xuất Ngày theo lịch cụ thể của mẫu được chọn.
    sample_date = train_df.loc[last_train_features.index[sample_index], "Date"]
    
    # [EN] Log the date being evaluated by the local SHAP explainer.
    # [VN] Ghi nhật ký ngày đang được trình giải thích SHAP cục bộ đánh giá.
    write_report(f"\nEvaluating SHAP local explainer for date: {sample_date.strftime('%B %d, %Y')}")
    
    # [EN] Extract the single row of computed SHAP arrays corresponding to the sample index.
    # [VN] Trích xuất hàng duy nhất của các mảng SHAP đã tính toán tương ứng với chỉ số mẫu.
    sample_shap_values = shap_values.values[sample_index]
    
    # [EN] Generate the actual model prediction for the chosen single sample instance.
    # [VN] Tạo dự đoán mô hình thực tế cho phiên bản mẫu duy nhất đã chọn.
    sample_prediction = last_trained_model.predict(last_train_features.iloc[[sample_index]])[0]
    
    # [EN] Extract the specific local base value (or scalar base value) for this single prediction.
    # [VN] Trích xuất giá trị cơ sở cục bộ cụ thể (hoặc giá trị cơ sở vô hướng) cho dự đoán đơn lẻ này.
    sample_base_value = base_value if np.ndim(base_value) == 0 else base_value[sample_index]

    # [EN] Log the detailed local explanation header.
    # [VN] Ghi nhật ký tiêu đề giải thích cục bộ chi tiết.
    write_report(f"Detailed SHAP contributions for sample index {sample_index}:")
    
    # [EN] Log the final raw prediction amount for this specific date sample.
    # [VN] Ghi nhật ký tổng số lượng dự đoán thô cho mẫu ngày cụ thể này.
    write_report(f"  Model prediction for sample: {sample_prediction:.2f}")
    
    # [EN] Log the baseline output start value for this specific date sample.
    # [VN] Ghi nhật ký giá trị bắt đầu đầu ra cơ sở cho mẫu ngày cụ thể này.
    write_report(f"  Base value for sample: {sample_base_value:.2f}")

    # [EN] Map features to their local SHAP values and sort by impact (highest positive contribution first).
    # [VN] Ánh xạ các đặc trưng tới giá trị SHAP cục bộ của chúng và sắp xếp theo tác động (đóng góp dương cao nhất đầu tiên).
    sample_feature_impact = sorted(zip(feature_cols, sample_shap_values), key=lambda x: x[1], reverse=True)
    
    # [EN] Log the header for top positive feature impact values.
    # [VN] Ghi nhật ký tiêu đề cho các giá trị tác động đặc trưng tích cực hàng đầu.
    write_report("  Top positive feature contributions for this sample:")
    
    # [EN] Iterate through and format the top 5 positive contributing features.
    # [VN] Lặp qua và định dạng 5 đặc trưng đóng góp tích cực hàng đầu.
    for feature, val in sample_feature_impact[:5]:
        # [EN] Log the individual feature and its numerical positive push.
        # [VN] Ghi nhật ký đặc trưng riêng lẻ và lực đẩy dương bằng số của nó.
        write_report(f"    {feature:>12}: {val:.6f}")

    # [EN] Log the header for top negative feature impact values.
    # [VN] Ghi nhật ký tiêu đề cho các giá trị tác động đặc trưng tiêu cực hàng đầu.
    write_report("  Top negative feature contributions for this sample:")
    
    # [EN] Re-sort the impact array (lowest first) and format the top 5 negative contributing features.
    # [VN] Sắp xếp lại mảng tác động (thấp nhất đầu tiên) và định dạng 5 đặc trưng đóng góp tiêu cực hàng đầu.
    for feature, val in sorted(sample_feature_impact, key=lambda x: x[1])[:5]:
        # [EN] Log the individual feature and its numerical negative drag.
        # [VN] Ghi nhật ký đặc trưng riêng lẻ và lực kéo âm bằng số của nó.
        write_report(f"    {feature:>12}: {val:.6f}")
else:
    # [EN] Fallback logging if model training failed or SHAP cannot run.
    # [VN] Ghi nhật ký dự phòng nếu quá trình huấn luyện mô hình thất bại hoặc không thể chạy SHAP.
    write_report("No trained model available for SHAP explanation.")

# ==========================================
# Official Test Submission Generation
# ==========================================
# [EN] Log section separator for generating final test submission predictions.
# [VN] Ghi chú phân cách phần để tạo dự đoán bài nộp bài kiểm tra cuối cùng.
write_report("\n===== Generating Official Submission =====")

# [EN] 1. Create a continuous daily date range for the required future forecasting horizon.
# [VN] 1. Tạo một phạm vi ngày liên tục hàng ngày cho chân trời dự báo tương lai bắt buộc.
future_dates = pd.date_range(start='2023-01-01', end='2024-07-01', freq='D')

# [EN] Initialize a completely empty pandas DataFrame structured around these future dates.
# [VN] Khởi tạo một pandas DataFrame hoàn toàn trống có cấu trúc xoay quanh những ngày tương lai này.
submission_df = pd.DataFrame({'Date': future_dates})

# [EN] 2. Apply our previously defined time-feature extraction function seamlessly.
# [VN] 2. Áp dụng trơn tru hàm trích xuất đặc trưng thời gian đã xác định trước đó của chúng tôi.
submission_df = create_time_features(submission_df)

# [EN] STRICT REQUIREMENT: For submission prediction, label isCovid must be all 0 (baseline normality).
# [VN] YÊU CẦU NGHIÊM NGẶT: Cho việc dự đoán nộp bài, nhãn isCovid phải hoàn toàn là 0 (bình thường theo mức cơ sở).
submission_df['isCovid'] = 0 

# [EN] Subset the future DataFrame to include exactly only the features expected by the trained model.
# [VN] Tập hợp con DataFrame tương lai để chỉ bao gồm chính xác các đặc trưng mong đợi bởi mô hình đã huấn luyện.
X_submission = submission_df[feature_cols]

# [EN] 3. Generate raw predictions using the final XGBoost pipeline for the entire submission window.
# [VN] 3. Tạo các dự đoán thô bằng cách sử dụng quy trình XGBoost cuối cùng cho toàn bộ cửa sổ nộp bài.
pred_raw_sub = last_trained_model.predict(X_submission)

# [EN] Transform predictions from scaled [0,1] space back into genuine currency amounts.
# [VN] Chuyển đổi các dự đoán từ không gian đã chia tỷ lệ [0,1] trở lại số tiền tệ thực tế.
pred_sub = last_scaler.inverse_transform(pred_raw_sub.reshape(-1, 1)).ravel()

# [EN] Attach the final predictions to the submission dataframe, strictly bounded at zero (no negative sales).
# [VN] Gắn các dự đoán cuối cùng vào dataframe nộp bài, bị giới hạn nghiêm ngặt ở mức 0 (không có doanh số âm).
submission_df['Revenue'] = np.maximum(pred_sub, 0)

# ==========================================
# ADDITIONAL LAYER: Theil-Sen Linear Adjustment
# ==========================================
# [EN] Log the initiation of the specific Theil-Sen drift adjustment post-processing phase.
# [VN] Ghi nhật ký khởi tạo pha hậu kỳ điều chỉnh độ trôi Theil-Sen cụ thể.
write_report("\n===== Applying Theil-Sen Linear Trend Adjustment =====")

try:
    # [EN] Read data from 'linear.csv' file into a DataFrame.
    # [VN] Đọc dữ liệu từ tệp 'linear.csv' vào một DataFrame.
    df_linear = pd.read_csv('linear.csv')

    # [EN] Convert the 'Date' column in the linear DataFrame to datetime format.
    # [VN] Chuyển đổi cột 'Date' trong DataFrame linear sang định dạng datetime.
    df_linear['Date'] = pd.to_datetime(df_linear['Date'])

    # [EN] Filter the DataFrame to include only records from the whole period of years 2012 to 2018.
    # [VN] Lọc DataFrame để chỉ bao gồm các bản ghi từ toàn bộ giai đoạn năm 2012 đến 2018.
    df_2012_2018 = df_linear[(df_linear['Date'] >= pd.to_datetime('2012-01-01')) & (df_linear['Date'] <= pd.to_datetime('2018-07-05'))].copy()

    # [EN] Find the earliest date in the filtered 2012-2018 dataset to act as the baseline time.
    # [VN] Tìm ngày sớm nhất trong tập dữ liệu 2012-2018 đã lọc để làm mốc thời gian cơ sở.
    start_date = df_2012_2018['Date'].min()

    # [EN] Calculate the number of days elapsed since the start date for each row in the filtered dataset.
    # [VN] Tính số ngày đã trôi qua kể từ ngày bắt đầu cho mỗi hàng trong tập dữ liệu đã lọc.
    df_2012_2018['Days_Since'] = (df_2012_2018['Date'] - start_date).dt.days

    # [EN] Perform Theil-Sen robust linear regression on the entire 2012-2018 period using the calculated days.
    # [VN] Thực hiện hồi quy tuyến tính mạnh mẽ Theil-Sen trên toàn bộ giai đoạn 2012-2018 bằng cách sử dụng số ngày đã tính toán.
    res = theilslopes(df_2012_2018['Linear_Trend'], df_2012_2018['Days_Since'])

    # [EN] Extract the computed slope from the Theil-Sen regression results.
    # [VN] Trích xuất độ dốc đã tính toán từ kết quả hồi quy Theil-Sen.
    slope = res.slope
    
    # [EN] Log the final calculated slope from the Theil-Sen robust fitter.
    # [VN] Ghi nhật ký độ dốc đã tính toán cuối cùng từ bộ tạo khớp mạnh Theil-Sen.
    write_report(f"Calculated Theil-Sen fitting slope: {slope:,.2f}")

    # [EN] Define the precise endpoint date for the adjustment translation logic.
    # [VN] Định nghĩa ngày điểm cuối chính xác cho logic tịnh tiến điều chỉnh.
    end_of_2022 = pd.to_datetime('2022-12-31')
    
    # [EN] Calculate the exact number of days between start_date and the end of 2022 baseline.
    # [VN] Tính số ngày chính xác giữa ngày bắt đầu (start_date) và đường cơ sở cuối năm 2022.
    days_to_end_2022 = (end_of_2022 - start_date).days
    
    # [EN] Calculate the mathematically adjusted intercept ensuring the trend line touches 0 at end of 2022.
    # [VN] Tính toán giao điểm đã điều chỉnh về mặt toán học để đảm bảo đường xu hướng chạm 0 vào cuối năm 2022.
    new_intercept = -slope * days_to_end_2022

    # [EN] Create a boolean mask covering exactly dates prior to and including 2024-07-01.
    # [VN] Tạo một mặt nạ boolean bao trùm chính xác các ngày trước và bao gồm 2024-07-01.
    mask = submission_df['Date'] <= '2024-07-01'
    
    # [EN] Compute day differentials specifically for the target submission window relative to start_date.
    # [VN] Tính chênh lệch ngày đặc biệt cho cửa sổ nộp bài mục tiêu liên quan đến start_date.
    sub_days_since = (submission_df.loc[mask, 'Date'] - start_date).dt.days
    
    # [EN] Compute extrapolated trend impact per day using the newly translated intercept and computed slope.
    # [VN] Tính toán tác động của xu hướng ngoại suy mỗi ngày bằng cách sử dụng giao điểm mới được tịnh tiến và độ dốc đã tính toán.
    predictions_linear = new_intercept + slope * sub_days_since

    # [EN] Add the extrapolated linear trend shift onto the ML model's baseline Revenue prediction.
    # [VN] Cộng thêm dịch chuyển xu hướng tuyến tính ngoại suy vào dự đoán Doanh thu cơ sở của mô hình Học máy (ML).
    submission_df.loc[mask, 'Revenue'] += predictions_linear
    
    # [EN] Assure once again that augmented revenues do not cross into negative realms.
    # [VN] Đảm bảo một lần nữa rằng doanh thu đã tăng cường không chuyển sang ngưỡng âm.
    submission_df['Revenue'] = np.maximum(submission_df['Revenue'], 0)
    
    # [EN] Log successful completion of Theil-Sen application.
    # [VN] Ghi nhật ký hoàn thành thành công việc áp dụng Theil-Sen.
    write_report("Successfully applied Theil-Sen linear adjustment to final predictions.")
    
except Exception as e:
    # [EN] Fallback error logging if Theil-Sen manipulation breaks.
    # [VN] Ghi nhật ký lỗi dự phòng nếu thao tác Theil-Sen bị hỏng.
    write_report(f"Failed to apply Theil-Sen linear adjustment. Error: {e}")

# [EN] Round off the final computed Revenue vector to exactly 2 decimal places.
# [VN] Làm tròn vectơ Doanh thu cuối cùng được tính toán thành chính xác 2 chữ số thập phân.
submission_df['Revenue'] = np.round(submission_df['Revenue'], 2)

# [EN] 4. Compute historical generic Cost Of Goods Sold ratio handling division by zero using NaNs.
# [VN] 4. Tính toán tỷ lệ Giá vốn hàng bán (COGS) chung lịch sử, xử lý phép chia cho 0 bằng NaN.
avg_cogs_ratio = (sales['COGS'] / sales['Revenue'].replace(0, np.nan)).mean()

# [EN] Log the final computed historical COGS multiplier ratio.
# [VN] Ghi nhật ký tỷ lệ hệ số nhân COGS lịch sử đã tính toán cuối cùng.
write_report(f"Calculated historical average COGS to Revenue ratio: {avg_cogs_ratio:.4f}")

# [EN] Generate submission COGS by applying the historical ratio multiplier across final predicted Revenue.
# [VN] Tạo COGS nộp bài bằng cách áp dụng hệ số nhân tỷ lệ lịch sử qua Doanh thu dự đoán cuối cùng.
submission_df['COGS'] = submission_df['Revenue'] * avg_cogs_ratio

# [EN] Round the COGS calculations nicely to 2 decimal places.
# [VN] Làm tròn các phép tính COGS một cách gọn gàng thành 2 chữ số thập phân.
submission_df['COGS'] = np.round(submission_df['COGS'], 2)

# [EN] 5. Select specifically only Date, Revenue, and COGS columns formatted for ultimate output.
# [VN] 5. Đặc biệt chỉ chọn các cột Date, Revenue và COGS được định dạng cho đầu ra cuối cùng.
final_submission = submission_df[['Date', 'Revenue', 'COGS']]

# [EN] Render DataFrame cleanly out to a universally accessible comma-separated file without index column.
# [VN] Xuất DataFrame một cách gọn gàng ra tệp phân tách bằng dấu phẩy có thể truy cập toàn cầu không có cột chỉ mục.
final_submission.to_csv('official_submission.csv', index=False)

# [EN] Log the absolute end marker acknowledging complete file generation.
# [VN] Ghi nhật ký mốc kết thúc tuyệt đối xác nhận việc tạo tệp hoàn tất.
write_report(f"Successfully generated official_submission.csv spanning 2023-01-01 to 2024-07-01.")