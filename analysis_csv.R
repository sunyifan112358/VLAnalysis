pdf(file = "kmean.pdf")

data <- read.csv('data.csv', header = TRUE);
data <- subset(data, select = c(c1.money, c1.welfare, c2.money, c2.welfare,
            c3.money, c3.welfare));
print(data);

data.normalized <- sapply(data, function(x) (x-min(x))/(max(x)-min(x)));
print(data.normalized);

cl <- kmeans(data.normalized, 3, iter.max = 100);
plot(data$c1.money, data$c1.welfare, col = cl$cluster);
plot(data$c2.money, data$c2.welfare, col = cl$cluster);
plot(data$c3.money, data$c3.welfare, col = cl$cluster);

hc <- hclust(dist(data.normalized));
plot(hc)




