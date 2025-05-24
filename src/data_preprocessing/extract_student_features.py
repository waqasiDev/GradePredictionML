import pandas as pd

def extract_student_features(csv_path: str, output_path: str = "data/processed/student_features_with_scores.csv") -> pd.DataFrame:
    # Load the original cleaned data
    df = pd.read_csv(csv_path)

    # --- Student-Level Feature Engineering ---
    student_features = df.groupby("Student_Id").agg(
        total_answers=("Answer", "count"),
        answered_questions=("Answer", lambda x: x.notnull().sum()),
        unanswered_questions=("Answer", lambda x: x.isnull().sum()),
        avg_points=("Assigned Points", "mean"),
        max_points=("Assigned Points", "max"),
        min_points=("Assigned Points", "min"),
        std_points=("Assigned Points", "std")
    ).reset_index()

    # --- Difficulty-based counts ---
    difficulty_counts = df.pivot_table(
        index="Student_Id", 
        columns="Difficulty", 
        values="Question", 
        aggfunc="count", 
        fill_value=0
    ).reset_index()

    # --- Difficulty-based average scores ---
    difficulty_scores = df.pivot_table(
        index="Student_Id", 
        columns="Difficulty", 
        values="Assigned Points", 
        aggfunc="mean", 
        fill_value=0
    ).reset_index()

    # --- Total Score (Target) ---
    student_scores = df.groupby("Student_Id")["Assigned Points"].sum().reset_index()
    student_scores.columns = ["Student_Id", "Total Score"]

    # --- Merge All ---
    features = student_features.merge(difficulty_counts, on="Student_Id", suffixes=('', '_count'))
    features = features.merge(difficulty_scores, on="Student_Id", suffixes=('', '_avg_score'))
    final_df = features.merge(student_scores, on="Student_Id")

    # --- Save to CSV ---
    final_df.to_csv(output_path, index=False)
    print(f"Saved student feature dataset to: {output_path}")

    return final_df


# Example usage
if __name__ == "__main__":
    input_csv = "data/processed/updated_data_with_points.csv"
    extract_student_features(input_csv)
