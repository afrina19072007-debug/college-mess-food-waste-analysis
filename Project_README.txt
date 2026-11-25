# College Mess Food Waste Analysis (Python + Excel)

## Project status
This is a beginner-friendly portfolio project starter. The included CSV is **synthetic sample data**, not real data from a college mess. Replace it with permission-based, anonymized measurements if you collect real observations.

## Objective
Analyze meal-wise and daily food waste to identify patterns and suggest practical waste-reduction steps.

## Tools
- Python
- pandas
- matplotlib
- Microsoft Excel (optional, for reviewing the CSV and summary tables)

## Dataset fields
- `date`: sample date
- `meal`: Breakfast, Lunch, Snacks, or Dinner
- `students_served`: approximate number served
- `food_prepared_kg`: food prepared in kilograms
- `food_waste_kg`: food wasted in kilograms
- `waste_percent`: waste as a percentage of prepared food

## How to run
1. Install Python 3.10+.
2. Open a terminal in this project folder.
3. Install dependencies:
   `python -m pip install -r requirements.txt`
4. Run:
   `python analyze_food_waste.py`
5. Find summary CSVs and charts in `outputs/`.

## Important interpretation note
The results are generated from synthetic sample data for demonstrating the workflow. Do not present sample-data findings as actual campus findings. If using this in a resume or interview, state clearly that it is a personal data-analysis project and explain which parts you completed and what AI assistance you used.

## Possible future improvements
- Add actual anonymized data collected with permission.
- Compare weekday vs weekend waste.
- Add a simple Excel dashboard.
- Build a Streamlit dashboard after learning the basics.
