# Amazon-Monitoring
Kaggle Contest
Chip (Image) Data Format

The chips for this competition were derived from Planet's full-frame analytic scene products using our 4-band satellites in sun-synchronous orbit (SSO) and International Space Station (ISS) orbit. The set of chips for this competition use the GeoTiff format and each contain four bands of data: red, green, blue, and near infrared. The specific spectral response of the satellites can be found in the Planet documentation. Each of these channels is in 16-bit digital number format, and meets the specification of the Planet four band analytic ortho scene product.

For purposes of the competition we have stripped out all of the geotiff information regarding the chip footprint and ground control points (GCPs). The imagery has a ground-sample distance (GSD) of 3.7m and an orthorectified pixel size of 3m. The data comes from Planet's Flock 2 satellites in both sun-synchronous and ISS orbits and was collected between January 1, 2016 and February 1, 2017. All of the scenes come from the Amazon basin which includes Brazil, Peru, Uruguay, Colombia, Venezuela, Guyana, Bolivia, and Ecuador (see map below).

We have also included a set of JPG chips for reference and practice. These chips were processed using the Planet visual product processor and then saved as jpg chips. These chips are provided as a reference to the scene content, but we expect that the additional information in the tif chips will be more fruitful for the competition.

![alt text] https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/Amazonriverbasin_basemap.png

Above: A map of the Amazon basin.

Labeling Process and Data Quality
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/chipdesc.jpg

To assemble this data set we set out with an initial specification of the phenomena we wished to find and include in the final data set. From that initial specification we created a "wish list" of scenes where we included a ballpark number of scenes required to get a sufficient number of chips to demonstrate the phenomena. This initial set of scenes was painstakingly collected by our Berlin team using Planet Explorer. All told this initial set of scenes numbered approximately 1600 and covered a land area of thirty million hectares.

This initial set of scenes was then processed using a custom product processor to create the jpg and 4-band tif chips. Any chip that did not have a full and complete four band product was omitted. This initial set of over 150,000 chips was then divided into two sets, a "hard" and an "easy" set. The easy set contained scenes that the Berlin team identified as having easier-to-identify labels like primary rainforest, agriculture, habitation, roads, water, and cloud conditions. The harder set of data was derived from scenes where the Berlin team had selected for shifting cultivation, slash and burn agriculture, blow down, mining, and other phenomenon.

The chips were labeled using the Crowd Flower platform and a mixture of crowd-sourced labor and our Berlin and San Francisco teams. While the utmost care was taken to get a large and well-labeled dataset, we are aware that not all of the labels in our dataset are correct. Governments around the world retain a large number of highly trained analysts to review images and even they can't always agree on what is present in a given satellite image.

Moreover, the commonly prescribed approach for labeling data in the GIS community is to use actual ground truth data to label scenes, which is both costly and time consuming. With this in mind we do believe our data has a reasonably high signal to noise ratio and is sufficient for training. Given the ease and expediency of crowd labeling, we believe that a large, relatively inexpensive and rapidly labeled dataset is better than a small, more definitive but less diverse dataset. We are interested to see how competitors handle any inaccuracies.

Class Labels
The class labels for this task were chosen in collaboration with Planet's Impact team and represent a reasonable subset of phenomena of interest in the Amazon basin. The labels can broadly be broken into three groups: atmospheric conditions, common land cover/land use phenomena, and rare land cover/land use phenomena. Each chip will have one and potentially more than one atmospheric label and zero or more common and rare labels. Chips that are labeled as cloudy should have no other labels, but there may be labeling errors. Sample chips with labels

![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/chips.jpg


Above: Sample chips and their labels.

As discussed in the data collection portion of this document, the chip labels are inherently noisy due to the labeling process and ambiguity of features, and scenes may either omit class labels or have incorrect class labels. Part of the challenge of this competition is to figure out how to work with noisy data.

Cloud Cover Labels

Clouds are a major challenge for passive satellite imaging, and daily cloud cover and rain showers in the Amazon basin can significantly complicate monitoring in the area. For this reason we have chosen to include a cloud cover label for each chip. These labels closely mirror what one would see in a local weather forecast: clear, partly cloudy, cloudy, and haze. For our purposes haze is defined as any chip where atmospheric clouds are visible but they are not so opaque as to obscure the ground. Clear scenes show no evidence of clouds, and partly cloudy scenes can show opaque cloud cover over any portion of the image. Cloudy images have 90% of the chip obscured by opaque cloud cover.

Examples of Cloudy Scenes

![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/cloudy_1.jpg
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/cloudy_1.jpg

Cloudy Scene enter image description here

Examples of Partly Cloudy Scenes
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/pc1.jpg
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/pc2.jpg
Partly Cloudy Scene Partly Cloudy Scene

Examples of Hazy Scenes
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/haze1.jpg
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/haze2.jpg

Partly Cloudy Scene Partly Cloudy Scene

More Common Labels

The common labels in this data set are rainforest, agriculture, rivers, towns/cities, and roads. Examples of each class are given below.

Primary Rain Forest

The overwhelming majority of the data set is labeled as "primary", which is shorthand for primary rainforest, or what is known colloquially as virgin forest. Generally speaking, the "primary" label was used for any area that exhibited dense tree cover.This Mongobay article gives a concise description of the difference between primary and secondary rainforest, but distinguishing between the two is difficult solely using satellite imagery. This is particularly true in older "secondary" forests. Primary Rainforest
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/primary.jpg
Above: Approximately 25,000 acres of untouched primary rainforest.

Water (Rivers & Lakes)

Rivers, reservoirs, and oxbow lakes are important features of the Amazon basin, and we used the water tag as a catch-all term for these features. Rivers in the Amazon basin often change course and serve as highways deep into the forest. The changing course of these rivers creates new habitat but can also strand endangered Amazon River Dolphins. River
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/river.jpg
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/river2.jpg
Above: A larger and slower river with significant sand bars. The brown color comes from significant silt deposits. River

Above: A small tributary joins a larger river system. The deep brown color of the river is noticeable near the bright sand bars.

Habitation

The habitation class label was used for chips that appeared to contain human homes or buildings. This includes anything from dense urban centers to rural villages along the banks of rivers. Small, single-dwelling habitations are often difficult to spot but usually appear as clumps of a few pixels that are bright white. Habitation
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/habitation1.jpg
Above: A larger city in the Amazon basin. Habitation
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/habitation2.jpg
Above: A large city.

Agriculture

Commercial agriculture, while an important industry, is also a major driver of deforestation in the Amazon. For the purposes of this dataset, agriculture is considered to be any land cleared of trees that is being used for agriculture or range land.

More reading on agriculture in the Amazon:

Sugarcane in Bolivia
Papaya cultivation destroying Peruvian Rainforest
Harvests in Rio Grande do Sul
Agriculture 1
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/agg1.jpg
Above: An agricultural area that showing the end state of "fishbone" deforestation. Agriculture 2
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/agg2.jpg
Above: A newer agricultural area showing "fishbone" deforestation.

Road

Roads are important for transportation in the Amazon but they also serve as drivers of deforestation. In particular, "fishbone" deforestation often follows new road construction, while smaller logging roads drive selective logging operations. For our data, all types of roads are labeled with a single "road" label. Some rivers look very similar to smaller logging roads, and consequently there may be some noise in this label. Analysis of the image using the near infrared band may prove useful in disambiguating the two classes.

More information: - Roads in the Amazon - NASA article on Fishbone Deforestation
Road 1
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/road.jpg
Above: classic "Fishbone" deforestation following a road. Road 2
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/road2.jpg
Above: roads snake out of a small town in the Amazon.

Cultivation

Shifting cultivation is a subset of agriculture that is very easy to see from space, and occurs in rural areas where individuals and families maintain farm plots for subsistence. This article by MongaBay by MongaBay gives a detailed overview of the practice. This type of agriculture is often found near smaller villages along major rivers, and at the outskirts of agricultural areas. It typically relies on non-mechanized labor, and covers relatively small areas. cultivation
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/cultivation.jpg
Above: A zoomed-in area showing cultivation (right side of river) cultivation
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/cultivation2.jpg
Above: A zoomed-in area showing cultivation and some selective logging. Dark areas indicate recent slash/burn activity

Bare Ground

Bare ground is a catch-all term used for naturally occuring tree free areas that aren't the result of human activity. Some of these areas occur naturally in the Amazon, while others may be the result from the source scenes containing small regions of biome much similar to the pantanal or cerrado. bare ground
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/bare.jpg
Above: a naturally occuring bare area in the cerrado. bare ground
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/bare2.jpg
Above: a naturally occuring bare area in the cerrado.

Less Common Labels

Slash and Burn

Slash-and-burn agriculture can be considered to be a subset of the shifting cultivation label and is used for areas that demonstrate recent burn events. This is to say that the shifting cultivation patches appear to have dark brown or black areas consistent with recent burning.This NASA Earth Observatory article gives a good primer on the practice as does this wikipedia article. Above: ground view of slash and burn agriculture. By Alzenir Ferreira de Souza slash burn
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/slashburn1.jpg
Above: A zoomed-in view of an area with shifting cultivation with evidence of a recent fire. slash burn
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/slashburn2.jpg
Above: A zoomed-in view of an area with shifting cultivation and evidence of a recent fire.

Selective Logging

The selective logging label is used to cover the practice of selectively removing high value tree species from the rainforest (such as teak and mahogany). From space this appears as winding dirt roads adjacent to bare brown patches in otherwise primary rain forest. This Mongabay Article covers the details of this process. Global Forest Watch is another great resource for learning about deforestation and logging. logging
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/logging.jpg
Above: The brown lines on the right of this scene are a logging road. Note the small brown dots in the area around the road. logging
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/logging1.jpg
Above: A zoomed image of logging roads and selective logging. logging
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/logging2.jpg
Above: A zoomed image of logging roads and selective logging.

Blooming

Blooming is a natural phenomenon found in the Amazon where particular species of flowering trees bloom, fruit, and flower at the same time to maximize the chances of cross pollination. These trees are quite large and these events can be seen from space. Planet recently captured a similar event in Panama. bloom
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/bloom.jpg
Above: a zoomed and contrast enhanced of a bloom event in the Amazon basin. The red arrows point to a few specific trees. The canopies of these trees can be over 30m across (~100ft).

Conventional Mining

There are a number of large conventional mines in the Amazon basin and the number is steadily growning. This label is used to classify large-scale legal mining operations.

mine
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/mine1.jpg
Above: A conventional mine in the Amazon.

"Artisinal" Mining

Artisinal mining is a catch-all term for small scale mining operations. Throughout the Amazon, especially at the foothills of the Andes, gold deposits lace the deep, clay soils. Artisanal miners, sometimes working illegally in land designated for conservation, slash through the forest and excavate deep pits near rivers. They pump a mud-water slurry into the river banks, blasting them away so that they can be processed further with mercury - which is used to separate out the gold. The denuded moonscape left behind takes centuries to recover.

Illegal and artisanal mines in Peru
Images of artisanal mining in Peru
MAAP Amazon Report #36
MAAP Amazon Report #49
Global Forest Watch article on Mining artisanal mine
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/artmine1.jpg
Above: A zoomed image of an artisanal mine in Peru. artisanal mine
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/artmine2.jpg
Above: A zoomed image of an artisanal mine in Peru.

Blow Down

Blow down, also called windthrow, is a naturally occurring phenomenon in the Amazon. Briefly, blow down events occur during microbursts where cold dry air from the Andes settles on top of warm moist air in the rainforest. The colder air punches a hole in the moist warm layer, and sinks down with incredible force and high speed (in excess of 100MPH). These high winds topple the larger rainforest trees, and the resulting open areas are visible from space. The open areas do not stay visible for along as plants in the understory rush in to take advantage of the sunlight.

MAAP #55: Blow Down Report in Peru Detailed
MAAP #54: Blow Down Report in Peru
National Geographic Article on Blow Down
Nature article on the size and frequency of blow down events. blow down
![alt text]https://kaggle2.blob.core.windows.net/competitions/kaggle/6322/media/blowdown.jpg
Above: A recent blow down event in the Amazon circled in red. Note the light green of the forest understory and the pattern of tree loss.
