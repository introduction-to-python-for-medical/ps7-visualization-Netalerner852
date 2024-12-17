data = fetch_openml(name='diabetes', version=1, as_frame=True)
features = list(df.columns)
selected_features = [features[2], features[4], features[5], features[7], features[0]]

reference_feature = selected_features[0] 
y = df[reference_feature]

fig, axs = plt.subplots(1, len(selected_features), figsize=(20, 3))

for ax, f in zip(axs, selected_features):
  ax.scatter(df[f], y)
  ax.set_xlabel(f)

reference_feature = selected_features[0]  
comparison_feature = selected_features[2] 

plt.figure(figsize=(10, 6))
plt.scatter(df[reference_feature], df[comparison_feature], alpha=0.6)
plt.xlabel(reference_feature)
plt.ylabel(comparison_feature)

plt.savefig('correlation_plot.png')

plt.show()

