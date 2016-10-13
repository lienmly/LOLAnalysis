## Import data
dat_10min <- read.csv("features_10.csv", header=TRUE)
summary(dat_10min)
observationNum <- nrow(dat_10min)

## Run test
minute10.glm <- glm(winner ~ goldDif + creepDif + killDif + assistDif + dragonDif, data = dat_10min, family = "binomial")
summary(minute10.glm)

## Import data
dat_20min <- read.csv("features_20.csv", header=TRUE)
summary(dat_20min)
observationNum <- nrow(dat_20min)

## Run test
minute20.glm <- glm(winner ~ goldDif + creepDif + killDif + assistDif + dragonDif, data = dat_20min, family = "binomial")
summary(minute20.glm)

## Import data
dat_30min <- read.csv("features_30.csv", header=TRUE)
summary(dat_30min)
observationNum <- nrow(dat_30min)

## Run test
minute30.glm <- glm(winner ~ goldDif + creepDif + killDif + assistDif + dragonDif, data = dat_30min, family = "binomial")
summary(minute30.glm)

## Study more for 20 min 
confint(minute20.glm)
confint.default(minute20.glm)
# wald.test(b = coef(minute20.glm), Sigma = vcov(minute20.glm), Terms = 1:5)

## odds ratios only
exp(coef(minute20.glm))

## odds ratios and 95% CI
exp(cbind(OR = coef(minute20.glm), confint(minute20.glm)))

png("dragon30.png", width=4, height=4, units="in", res=300)
plot(dat_30min$dragonDif,dat_30min$winner,main = "Dragon Diff at 30")
dev.off()
## predicte probabilities 
#predict_20 <- with(dat_20min, data.frame(gre = mean(gre), gpa = mean(gpa), rank = factor(1:4)))

## view data frame
#newdata1
curve(predict(minute30.glm, data.frame(goldDif=x), type="response"), add=TRUE) 

## Load in training and test data
training_20 <- read.csv("C:/Users/lienm/OneDrive/Courses/Independent Study - N. Sturtevant/Week 9/5-16-16/Training Data/training_20.csv")
test_20 <- read.csv("C:/Users/lienm/OneDrive/Courses/Independent Study - N. Sturtevant/Week 9/5-16-16/Test Data/test_20.csv")



trainedMinute20.glm <- glm(winner ~ goldDif + creepDif + killDif + assistDif + dragonDif, data = training_20, family = "binomial")

test_20$prediction <- predict(trainedMinute20.glm, test_20, type="response")
test_20$predictionBinary <- round(test_20$prediction)
cor(test_20$winner, test_20$prediction)
cor(test_20$winner, test_20$predictionBinary)

plot(main="GoldDif vs Winning Prediction", x=test_20$goldDif, y=test_20$prediction, xlab="Gold Difference", ylab="Winning Prediction", col=hsv(test_20$winner/3,1,1))
plot(main="CreepDif vs Winning Prediction", x=test_20$creepDif, y=test_20$prediction, xlab="Creep Difference", ylab="Winning Prediction", col=hsv(test_20$winner/3,1,1))
plot(main="KillDif vs Winning Prediction", x=test_20$killDif, y=test_20$prediction, xlab="Kill Difference", ylab="Winning Prediction", col=hsv(test_20$winner/3,1,1))
plot(main="AssistDif vs Winning Prediction", x=test_20$assistDif, y=test_20$prediction, xlab="Assist Difference", ylab="Winning Prediction", col=hsv(test_20$winner/3,1,1))
plot(main="DragonDif vs Winning Prediction", x=test_20$dragonDif, y=test_20$prediction, xlab="Dragon Difference", ylab="Winning Prediction", col=hsv(test_20$winner/3,1,1))

cor(test_20$killDif, test_20$goldDif)
cor(test_20$prediction, test_20$dragonDif)
cor(test_20$prediction, test_20$dragonDif)

## Correlation graph 

library(dplyr)
selectedFeatures = 
  select(dat_20min,
         goldDif, 
         creepDif,
         killDif,
         assistDif,
         dragonDif)

library(PerformanceAnalytics)
chart.Correlation(selectedFeatures, 
                  method="spearman",
                  histogram=TRUE,
                  pch=16)

## PCA 
# log transform 
log.20 <- log(dat_20min[, 3:7])

# apply PCA - scale. = TRUE is highly 
# advisable, but default is FALSE. 
dat20.pca <- prcomp(log.20,
                 center = TRUE,
                 scale. = TRUE) 
