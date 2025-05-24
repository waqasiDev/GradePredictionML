import pandas as pd

def generate_total_scores(csv_path: str) -> pd.DataFrame:
    """
    Load student answer data and compute total score for each student.

    Args:
        csv_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: A DataFrame with Student_Id and Total Score columns.
    """
    # Load data
    df = pd.read_csv(csv_path)

    # Check necessary column
    if "Student_Id" not in df.columns or "Assigned Points" not in df.columns:
        raise ValueError("CSV must contain 'Student_Id' and 'Assigned Points' columns.")

    # Group by Student_Id and sum points
    student_scores = df.groupby("Student_Id")["Assigned Points"].sum().reset_index()
    student_scores.columns = ["Student_Id", "Total Score"]

    return student_scores


# Example usage
if __name__ == "__main__":
    csv_file = "data/processed/updated_data_with_points.csv"
    scores_df = generate_total_scores(csv_file)
    print(scores_df.head())


    scores_df.to_csv("data/processed/student_total_scores.csv", index=False)
