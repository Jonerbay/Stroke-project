from autogluon.tabular import TabularDataset, TabularPredictor

data = TabularDataset('./dataset.csv')
train_data = data.sample(frac=0.8)
test_data = data.drop(train_data.index)

predictor = TabularPredictor('Death', eval_metric='balanced_accuracy').fit(data, time_limit=120, presets='best_quality')
leaderboard = predictor.leaderboard(test_data, silent=True)
results = predictor.fit_summary()

print(leaderboard[['model', 'score_val']])

