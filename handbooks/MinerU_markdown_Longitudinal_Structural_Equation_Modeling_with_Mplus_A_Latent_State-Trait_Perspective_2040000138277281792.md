# Longitudinal

# Structural Equation

# Modeling with

# Mplus

# A Latent State-Trait Perspective

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/8ec074fa71bf411692e50ff8ec2b42dc8cc693dc07b0dc82ae6411077411abe0.jpg)


CHRISTIAN GEISER 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/6d8712bf4ad9565c1c5115c42026af118ce868d30f9d3b642c8844c6275dd1b1.jpg)


# GUILFORD PRESS

Longitudinal Structural Equation Modeling with Mplus 

# Methodology in the Social Sciences

David A. Kenny, Founding Editor 

Todd D. Little, Series Editor 

www.guilford.com/MSS 

This series provides applied researchers and students with analysis and research design books that emphasize the use of methods to answer research questions. Rather than emphasizing statistical theory, each volume in the series illustrates when a technique should (and should not) be used and how the output from available software programs should (and should not) be interpreted. Common pitfalls as well as areas of further development are clearly articulated. 

# RECENT VOLUMES

PRINCIPLES AND PRACTICE OF STRUCTURAL EQUATION MODELING, 

Rex B. Kline 

HYPOTHESIS TESTING AND MODEL SELECTION IN THE SOCIAL SCIENCES 

David L. Weakliem 

REGRESSION ANALYSIS AND LINEAR MODELS: CONCEPTS, APPLICATIONS, 

AND IMPLEMENTATION 

Richard B. Darlington and Andrew F. Hayes 

GROWTH MODELING: STRUCTURAL EQUATION 

AND MULTILEVEL MODELING APPROACHES 

Kevin J. Grimm, Nilam Ram, and Ryne Estabrook 

PSYCHOMETRIC METHODS: THEORY INTO PRACTICE 

Larry R. Price 

INTRODUCTION TO MEDIATION, MODERATION, AND CONDITIONAL PROCESS ANALYSIS: 

A REGRESSION-BASED APPROACH, SECOND EDITION 

Andrew F. Hayes 

MEASUREMENT THEORY AND APPLICATIONS FOR THE SOCIAL SCIENCES 

Deborah L. Bandalos 

CONDUCTING PERSONAL NETWORK RESEARCH: A PRACTICAL GUIDE 

Christopher McCarty, Miranda J. Lubbers, Raffaele Vacca, and José Luis Molina 

QUASI-EXPERIMENTATION: A GUIDE TO DESIGN AND ANALYSIS 

Charles S. Reichardt 

THEORY CONSTRUCTION AND MODEL-BUILDING SKILLS: A PRACTICAL GUIDE 

FOR SOCIAL SCIENTISTS, SECOND EDITION 

James Jaccard and Jacob Jacoby 

LONGITUDINAL STRUCTURAL EQUATION MODELING WITH Mplus: 

A LATENT STATE–TRAIT PERSPECTIVE 

Christian Geiser 

COMPOSITE-BASED STRUCTURAL EQUATION MODELING: 

ANALYZING LATENT AND EMERGENT VARIABLES 

Jörg Henseler 

# Longitudinal Structural Equation Modeling with Mplus

A Latent State–Trait Perspective 

Christian Geiser 

Series Editor’s Note by Todd D. Little 

Copyright © 2021 The Guilford Press 

A Division of Guilford Publications, Inc. 

370 Seventh Avenue, Suite 1200, New York, NY 10001 

www.guilford.com 

All rights reserved 

No part of this book may be reproduced, translated, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, microfilming, recording, or otherwise, without written permission from the publisher. 

Printed in the United States of America 

This book is printed on acid-free paper. 

Last digit is print number: 9 8 7 6 5 4 3 2 1 

Library of Congress Cataloging-in-Publication Data 

Names: Geiser, Christian, author. 

Title: Longitudinal structural equation modeling with Mplus : a latent state–trait perspective / Christian Geiser. 

Description: New York: The Guilford Press, 2021. | Series: Methodology in the social sciences | Includes bibliographical references and index. 

Identifiers: LCCN 2020021879 | ISBN 9781462544240 (hardcover) | ISBN 9781462538782 (paperback) 

Subjects: LCSH: Structural equation modeling. | Longitudinal method. | Mp1us. 

Classifcation: LCC QA278.3 .G45 2020 | DDC 001.4/22028553—dc23 

LC record available at https://lccn.loc.gov/2020027819 

# Series Editor’s Note

Writing an introduction to a book on longitudinal structural equation modeling is a bit like preaching to the choir. Like Christian Geiser, I have been a student of longitudinal models because of the powerful information that these models can convey. Geiser highlights the advantages of the latent variable approach to longitudinal models, including correcting for measurement error, establishing measurement equivalence, informing causal inference because of the temporal separation of the repeated measurements, and the like. Geiser focuses on the use of Mplus (see statmodel.com) as the software platform, with numerous annotated scripts located in the online support pages for his book (www.guilford. com/Geiser2-materials) and detailed scripting examples organized in boxes that clearly detail both input syntax and output results. 

As I wrote in the introduction to Chip Reichardt’s book Quasi-Experimentation, I like the word “verisimilitude”—the truth-like value of a study’s results. With longitudinal data we can achieve a high level of verisimilitude around causal inference and direction of effects. Geiser covers a broad array of traditional longitudinal models and the latent state–trait framework that he learned about from a couple of pillars in the state–trait longitudinal modeling arena, Michael Eid and Rolf Steyer. The latent state–trait theory and its recent revision provide a different viewpoint for thinking about growth and change in longitudinal research. I’m a big fan of different perspectives because they broaden and enhance how we think and theorize about change processes. Geiser’s book gives this perspective an authoritative and complete treatment, and situates other 

longitudinal models (e.g., autoregressive, change score, and growth curve models) in the context of the latent state–trait theory. 

Chapters are consistently organized and build from one to the next in a clear sequence, with end-of-chapter summaries that highlight the key takeaway messages. In later chapters, Geiser addresses the critical process of model selection (see also James Jaccard & Jacob Jacoby, 2020), handling missing data in longitudinal research, and guidelines for disseminating results in research publications. 

Pedagogically, Geiser isolates and emphasizes key topics, formulas, input scripts, and output samples in the form of boxes. These boxes are particularly well crafted and useful because they heighten focus on these critical points. A thorough glossary of Greek symbols, mathematical coefficients and variables symbols, and commonly used acronyms is included. I’m confident you’ll find this book a critical resource to complement your library of longitudinal modeling guides. As always, enjoy! 

Todd D. Littl e 

At home 

Lubbock, Texas 

# Preface

Human beings experience changes in their attitudes, feelings, personality traits, cognitive abilities, intelligence, etc., across time. Social science researchers are frequently interested in studying such changes and relating them to other variables (or to changes in other variables). Moreover, investigators often try to disentangle causes and effects. For example, does the frequent use of violent computer games cause aggressive behavior in children? Or does aggressive behavior cause children to play violent games more often? Or are there one or more other variables (e.g., the presence of violent role models) that cause children to (1) exhibit aggressive behavior and (2) frequently use violent games? In order to meaningfully study change and causality, repeated observations from the same people at different times are required. Even though longitudinal designs do not per se allow for causal inferences, specific longitudinal experimental and quasiexperimental designs make such inferences more plausible than cross-sectional (single-time-point) designs. 

In addition to experiencing long-term developmental or other, more permanent changes in certain attributes (e.g., changes in cognitive abilities from childhood to adulthood), human beings are also prone to more short-term situational influences. That is, many attitudes and emotions show substantial dayto-day (or even within-day) variability around a fairly stable habitual or “trait” level. Determining whether a social science construct is a “state” or a “trait” and studying the importance of situational influences and potential person $\times$ situation interactions are additional goals that researchers pursue through longitudinal studies. 

One important problem in empirical social science studies in general is the omnipresence of measurement error. Measurements in the social sciences typically have less than perfect reliabilities. Measurement error is a particularly important issue in longitudinal studies, in which researchers are interested in measuring “true” change and variability rather than observing differences in individuals’ scores that may simply be due to random noise. Researchers therefore employ statistical methods that allow them to separate true individual differences (“true score variance”) from variability that must be attributed to measurement error. Latent variable models are well suited for this purpose. Latent variables in appropriate statistical measurement models are by definition free of random measurement error. This makes it possible to isolate true variability and true changes from variation over time that are merely due to measurement error. The present book therefore takes a latent variable modeling approach to longitudinal data analysis. 

Even though longitudinal designs are popular and frequently used in empirical research, researchers are often unsure about how to approach the data-analytic (statistical) part of longitudinal studies. The main reason for this uncertainty is that the statistical analysis of longitudinal data is quite complex. Part of the complexity arises from the fact that many different types of statistical models have been proposed for the analysis of longitudinal data (e.g., autoregressive models, change score models, growth curve models, state–trait models), and many substantive researchers are uncertain about which statistical model they should apply to their research questions and how different types of models are related and/or differ from one another. In addition, modern longitudinal statistical models, many of which are based on confirmatory factor analysis (CFA) and latent variable structural equation modeling (SEM), allow researchers to examine both the covariance and mean structure in their data. This makes it possible to study both, average (mean) changes in a construct as well as the stability (or instability) of interindividual differences across time, but it also adds complexities to the specification and analysis of the models. Particularly the covariance structure in longitudinal data (measured variable variances and covariances) is often complex due to the presence of multiple systematic and unsystematic effects (e.g., trait effects, situation effects, autoregressive effects, individual differences in change, method effects, measurement error). This makes the modeling of longitudinal data challenging, especially when multiple indicators (multiple items, tests, or questionnaire scales) are used as indicators of a construct at multiple time points and/or when multiple distinct constructs are considered simultaneously. 

In multiple-indicator data, researchers have to specify an appropriate longitudinal measurement model that fits their data well, in addition to selecting a 

structural (latent variable) model that properly reflects the longitudinal process observed in the data. This is often challenging due to the presence of indicatorspecific (method) effects. Another complication in longitudinal data is that measurement equivalence across time needs to be established. The measurement equivalence assumption can be understood as an “apples and oranges” problem. Only when measures maintain the same links (i.e., factor loadings and intercepts) to the underlying latent constructs that they are supposed to measure across time, are comparisons of, for example, latent variable means between different time points interpretable and meaningful. Measurement equivalence is thus a prerequisite for a meaningful analysis of changes across time. This assumption can be properly tested only with multiple-indicator data. 

In this book, I provide a comprehensive overview of longitudinal CFA/SEM models and their application in the software Mplus (Muthén & Muthén, 1998– 2017). I base my presentation of all models on a general measurement theoretical framework for longitudinal data analysis (latent state–trait theory). Using a well-developed measurement theoretical framework as the basis for formulating latent variable statistical models has the advantage that all latent variables and their associated parameters (e.g., their means, variances, factor loadings, and regression coefficients) in the resulting longitudinal models are well defined and have a clear interpretation. Using the latent state–trait approach also facilitates a comparison of the different models and makes it easier to show the links between different models. 

After introducing the concepts of latent state–trait theory in Chapter 1, I begin my presentation of various longitudinal models in Chapter 2 with rather simple CFA models that use (1) only a single indicator (measured variable) per measurement occasion and (2) just one latent factor. In Chapter 3, I describe models for single-indicator designs that use more than one latent factor. Chapters 4 and 5 deal with multiple-indicator designs in which a construct is repeatedly measured with at least two indicators. In Chapter 4, the issue of measurement equivalence and how it can be tested is addressed in detail. In Chapter 5, I present various specialized models for multiple-indicator data. In Chapter 6, I provide an introduction to the analysis of intensive longitudinal data using the dynamic SEM framework in Mplus. Chapter 7 deals with missing data and its handling in longitudinal studies. In Chapter 8, I provide recommendations for model selection and guidelines for how to report the results of a longitudinal structural equation analysis. 

In my presentation of specific models, I use both equations and path diagrams. In the path diagrams, I follow conventions of the reticular analysis modeling (RAM) approach (McArdle, 1980) to include both the covariance and mean structure, as both are relevant in longitudinal data analysis and are 

included in the Mplus software applications. Example Mplus applications of all models are discussed in the text with the relevant data sets, annotated input, and output files available as online supplemental materials (see the box at the end of the table of contents). 

In another special approach that I take in this book, I contrast models for measuring state variability processes (classical latent state–trait models) with models for measuring more long-lasting trait changes. In addition, I discuss hybrid approaches that allow researchers to model both state variability and trait changes simultaneously. 

Writing this book would not have been possible without the support of a number of people and institutions. First of all, without the support of my family, I could not have written this book. Second, without my doctoral advisor, Michael Eid, I would have never learned about latent state–trait theory and how it can be used as a general measurement theoretical framework for defining a large variety of longitudinal models. I thank Rolf Steyer for inviting me to participate in the work that led to the revised version of latent state–trait theory that is discussed in this book (my contribution to this development was very minor, but I learned a lot from discussions with Rolf and his student Axel Mayer). The Psychology Department and College of Education and Human Services at Utah State University (USU) have provided tremendous support for my work over the past 7 years. I wrote the first version of this book during my 2018–2019 sabbatical leave, which was generously granted by USU. Without USU’s highly supportive environment for faculty researchers, a book project like this one would have been much more difficult to complete. Finally, I would like to thank C. Deborah Laughton at The Guilford Press, who provided tremendous support, highly useful feedback, and constructive criticism, as well as positive energy, all of which greatly facilitated the completion of the final version of this book. 

# Brief Contents

List of Abbreviations xix 

Guide to Statistical Symbols xxi 

1 ·	 A Measurement Theoretical Framework 1 for Longitudinal Data: Introduction to Latent State–Trait Theory 

2 ·	 Single-Factor Longitudinal Models for Single-Indicator Data 16 

3 ·	 Multifactor Longitudinal Models for Single-Indicator Data 45 

4 ·	 Latent State Models and Measurement 113 Equivalence Testing in Longitudinal Studies 

5 ·	 Multiple-Indicator Longitudinal Models 155 

6 ·	 Modeling Intensive Longitudinal Data 231 

7 ·	 Missing Data Handling 279 

8 ·	 How to Choose between Models and Report the Results 307 

References 323 

Author Index 329 

Subject Index 332 

About the Author 344 

# Extended Contents

# List of Abbreviations

xix 

# Guide to Statistical Symbols

xxi 

# 1 ·	 A Measurement Theoretical Framework for Longitudinal Data: Introduction to Latent State–Trait Theory

1.1 Introduction / 1 

1.2 Latent State–Trait Theory / 3 

1.2.1 Introduction / 3 

1.2.2 Basic Idea / 3 

1.2.3 Random Experiment / 5 

1.2.4 Variables in LST‑R Theory / 5 

BOX 1.1. Key Concepts and Definitions in CTT / 7 

1.2.5 Properties / 10 

1.2.6 Coefficients / 11 

BOX 1.2. Properties of the Latent Variables in LST-R Theory / 12 

1.3 Chapter Summary / 14 

1.4 Recommended Readings / 15 

# 2 ·	 Single‑Factor Longitudinal Models for Single-­ Indicator Data 16

2.1 Introduction / 16 

2.2 The Random Intercept Model / 17 

2.2.1 Introduction / 17 

2.2.2 Model Description / 17 

BOX 2.1. Available Information, Model Degrees of Freedom, and Model Identification in Single-Indicator Longitudinal Designs / 19 

BOX 2.2. Defining the Random Intercept Model Based on LST-R Theory / 20 

2.2.3 Variance Decomposition and Reliability Coefficient / 21 

2.2.4 Mplus Application / 22 

BOX 2.3. Model Fit Assessment and Model Comparisons / 24 

2.2.5 Summary / 26 

2.3 The Random and Fixed Intercepts Model / 28 

2.3.1 Introduction / 28 

2.3.2 Model Description / 28 

BOX 2.4. Means of Linear Combinations / 28 

BOX 2.5. Defining the Random and Fixed Intercepts Model Based on LST-R Theory / 31 

2.3.3 Variance Decomposition and Reliability Coefficient / 32 

2.3.4 Mplus Application / 32 

2.3.5 Summary / 34 

2.4 The $\xi$ -Congeneric Model / 34 

2.4.1 Introduction / 34 

2.4.2 Model Description / 35 

BOX 2.6. Defining the ξ-Congeneric Model Based on LST Theory / 37 

2.4.3 Variance Decomposition and Reliability Coefficient / 38 

2.4.4 Mplus Application / 38 

BOX 2.7. The MODEL CONSTRAINT and MODEL TEST Options in Mplus / 40 

2.4.5 Summary / 43 

2.5 Chapter Summary / 43 

2.6 Recommended Reading / 44 

Note / 44 

# 3 ·	 Multifactor Longitudinal Models for Single‑Indicator Data

3.1 Introduction / 45 

3.2 The Simplex Model / 45 

3.2.1 Introduction / 45 

3.2.2 Model Description / 46 

BOX 3.1. Defining the Simplex Model Based on LST-R Theory / 48 

BOX 3.2. Should a Researcher Constrain State Residual or Measurement Error Variances in the Simplex Model? / 51 

3.2.3 Variance Decomposition and Coefficients / 51 

3.2.4 Assessing Stability and Change in the Simplex Model / 53 

BOX 3.3. Endogenous versus Exogenous Variables in Structural Equation Models and Mplus / 54 

3.2.5 Mplus Application / 56 

BOX 3.4. Specifying the Simplex Model with Equal State Residual Factor Variances / 57 

BOX 3.5. Direct versus Indirect (Mediated) Variable Effects in the Simplex Model / 61 

3.2.6 Summary / 62 

3.3 The Latent Change Score Model / 62 

3.3.1 Introduction / 62 

3.3.2 Model Description / 63 

3.3.3 Variance Decomposition and Coefficients / 64 

3.3.4 Mplus Application / 65 

3.3.5 Summary / 68 

3.4 The Trait–State–Error Model / 69 

3.4.1 Introduction / 69 

3.4.2 Model Description / 69 

BOX 3.6. Defining the TSE Model Based on LST-R Theory / 72 

3.4.3 Variance Decomposition and Coefficients / 75 

BOX 3.7. The Mean Structure in the TSE Model / 76 

3.4.4 Mplus Application / 79 

BOX 3.8. Estimation Problems and Bias in the TSE Model / 83 

3.4.5 Computing the Con(τt), TCon(τt), SCon(τt), and $O s p ( \tau _ { t } )$ Coefficients in Mplus / 85 

3.4.6 Summary / 86 

3.5 Latent Growth Curve Models / 88 

3.5.1 Introduction / 88 

3.5.2 The Linear LGC Model / 88 

BOX 3.9. Defining the Linear LGC Model Based on LST-R Theory / 91 

3.5.3 The LGC Model with Unspecified Growth Pattern / 97 

BOX 3.10. Defining the LGC Model with Unspecified Growth Pattern Using the Concepts of LST-R Theory / 99 

3.6 Chapter Summary / 105 

BOX 3.11. Using Ordered Categorical Observed Variables as Indicators / 109 

3.7 Recommended Readings / 110 

Notes / 110 

# 4 ·	 Latent State Models and Measurement Equivalence Testing in Longitudinal Studies

4.1 Introduction / 113 

4.2 The Latent State Model / 114 

4.2.1 Introduction / 114 

4.2.2 Model Description / 114 

4.2.3 Scale Setting / 116 

BOX 4.1. Relationships Between the LS and CTT Models / 116 

BOX 4.2. Available Information and Model Degrees of Freedom in Multiple-Indicator Longitudinal Designs / 117 

BOX 4.3. Alternative Methods of Defining the Scale of Latent State Variables / 120 

4.2.4 Model Definition Based on LST‑R Theory / 120 

4.2.5 Variance Decomposition and Reliability Coefficient / 120 

BOX 4.4. Defining the LS Model Based on LST-R Theory / 121 

4.2.6 Testing ME across Time / 122 

BOX 4.5. Levels of ME According to Widaman and Reise (1997) / 123 

BOX 4.6. Nested Models and Chi-Square Difference Testing / 124 

4.2.7 Other Features of the LS Model / 125 

4.2.8 Mplus Application / 126 

BOX 4.7. Different Ways to Specify and Analyze the Mean Structure in the LS Model / 128 

4.2.9 Summary / 134 

4.3 The LS Model with Indicator-Specific Residual Factors / 136 

4.3.1 Introduction / 136 

4.3.2 Model Description / 136 

BOX 4.8. Indicator-Specific Effects in Longitudinal Data / 137 

BOX 4.9. Defining the LS-IS Model Based on LST-R Theory / 140 

4.3.3 Variance Decomposition and Coefficients / 142 

BOX 4.10. Correlated Errors: An Alternative Way to Model Indicator Specificity in Longitudinal Data / 144 

4.3.4 Mplus Application / 145 

BOX 4.11. Providing User-Defined Starting Values in Mplus / 147 

4.3.5 Summary / 151 

4.4 Chapter Summary / 151 

4.5 Recommended Readings / 153 

Notes / 153 

# 5 ·	 Multiple‑Indicator Longitudinal Models

5.1 Introduction / 155 

5.2 Latent State Change Models / 156 

5.2.1 Introduction / 156 

5.2.2 Model Description / 157 

5.2.3 Variance Decomposition and Coefficients / 159 

5.2.4 Mplus Application / 160 

5.2.5 Summary / 160 

5.3 The Latent Autoregressive/Cross-Lagged States Model / 161 

5.3.1 Introduction / 161 

5.3.2 Model Description / 162 

BOX 5.1. Defining the LAS Model Based on LST-R Theory / 164 

5.3.3 Variance Decomposition and Coefficients / 164 

5.3.4 Other Features of the Model / 165 

5.3.5 Multiconstruct Extension / 165 

5.3.6 Mplus Application / 167 

5.3.7 Summary / 170 

5.4 Latent State–Trait Models / 171 

5.4.1 Introduction / 171 

5.4.2 The Singletrait–Multistate Model / 172 

BOX 5.2. Defining the STMS Model Based on LST-R Theory / 175 

BOX 5.3. Some Guidelines for the Interpretation of the Con, Osp, and Rel Coefficients / 177 

BOX 5.4. Specifying an STMS Model as a Bifactor Model / 179 

BOX 5.5. STMS Models without versus with Autoregressive Effects / 185 

5.4.3 The STMS Model with Indicator‑Specific Residual Factors / 186 

BOX 5.6. Defining the STMS-IS Model Based on LST-R Theory / 188 

5.4.4 The Multitrait–Multistate Model / 192 

BOX 5.7. Defining the MTMS Model Based on LST-R Theory / 194 

BOX 5.8. The MTMS Model with Autoregression / 200 

5.5 Latent Trait-Change Models / 202 

5.5.1 Introduction / 202 

5.5.2 The LST Trait‑Change Model / 204 

BOX 5.9. Defining the LST-TC Model Based on LST-R Theory / 207 

BOX 5.10. Alternative Equivalent Ways to Specify the LST-TC Model / 209 

5.5.3 Multiple‑Indicator Latent Growth Curve Models / 212 

BOX 5.11. Defining the Linear ISG Model Based on LST-R Theory / 216 

5.6 Chapter Summary / 223 

5.6.1 Advantages of Multiple‑Indicator Models / 223 

5.6.2 Limitations of Multiple‑Indicator Models / 228 

5.7 Recommended Readings / 229 

Notes / 230 

# 6 ·	 Modeling Intensive Longitudinal Data

231 

6.1 Introduction / 231 

6.2 Special Features of Intensive Longitudinal Data / 232 

6.2.1 Introduction / 232 

6.2.2 Wide‑ versus Long‑Format Data / 232 

6.2.3 Imbalanced Time Points / 234 

6.2.4 Autoregressive Effects / 235 

6.3 Specifying Longitudinal SEMs for Intensive Longitudinal Data / 235 

6.3.1 Introduction / 235 

6.3.2 The Random Intercept Model as a Multilevel Model / 235 

BOX 6.1. Wide-to-Long Data Transformation of Data in Mplus / 238 

6.3.3 The Linear Growth Model as a Multilevel Model / 243 

6.3.4 The Multitrait–Multistate Model as a Multilevel Model / 247 

6.3.5 The Indicator‑Specific Growth Model as a Multilevel Model / 252 

6.3.6 Modeling Autoregressive Effects Using DSEM / 257 

6.4 Chapter Summary / 276 

6.5 Recommended Readings / 277 

# 7 ·	 Missing Data Handling

279 

7.1 Introduction / 279 

7.2 Missing Data Mechanisms / 280 

7.2.1 Missing Completely at Random / 281 

7.2.2 Missing at Random / 282 

7.2.3 Missing Not at Random / 283 

7.3 ML Missing Data Handling / 285 

7.3.1 Introduction / 285 

7.3.2 ML Missing Data Analysis in Mplus / 286 

7.3.3 Summary / 290 

7.4 Multiple Imputation / 290 

7.4.1 Introduction / 290 

7.4.2 MI in Mplus / 291 

7.4.3 Summary / 296 

7.5 Planned Missing Data Designs / 296 

7.5.1 Introduction / 296 

7.5.2 Analysis of Planned Missing Data and Simulations in Mplus / 297 

7.6 Chapter Summary / 303 

7.7 Recommended Readings / 305 

Note / 306 

# 8 ·	 How to Choose between Models and Report the Results 307

8.1 Model Selection / 307 

8.2 Reporting Results / 310 

8.2.1 General Recommendations / 310 

8.2.2 Methods Section / 311 

8.2.3 Results Section / 315 

8.3. Chapter Summary / 320 

8.4 Recommended Readings / 320 

Notes / 321 

# References 323

# Author Index 329

# Subject Index 332

# About the Author 344

The companion website www.guilford.com/geiser2-materials features datasets, annotated syntax files, output for all of the examples, as well as color versions of Figures 6.6A, 6.6B, and 6.8. 

# List of Abbreviations

AIC $=$ Akaike’s information criterion 

ACL $=$ Autoregressive/cross-lagged 

BIC $=$ Bayesian information criterion 

CFA $=$ Confirmatory factor analysis 

CFI $=$ Comparative fit index 

CTT $=$ Classical test theory 

CU $=$ Correlated uniqueness 

DSEM $=$ Dynamic structural equation modeling 

EMA $=$ Ecological momentary assessment 

FIML $=$ Full information maximum likelihood 

FMI $=$ Fraction of missing information; also referred to as $\boldsymbol { \gamma } _ { 0 }$ 

IC $=$ Information criteria 

ICC $=$ Intraclass correlation coefficient 

ISG $=$ Indicator-specific growth 

LACS $=$ Latent autoregressive/cross-lagged states 

LAS $=$ Latent autoregressive states 

LGC $=$ Latent growth curve 

LGCMs $=$ Latent growth curve models 

LS $=$ Latent state 

LSC $=$ Latent state change 

LS-IS $=$ Latent state with indicator-specific factors 

LST $=$ Latent state–trait 

LST-R $=$ Latent state–trait revised 

LST-TC $=$ Latent state–trait trait change 

LTC $=$ Latent trait change 

MAR $=$ Missing at random 

MCAR $=$ Missing completely at random 

MCMC $=$ Markov chain Monte Carlo 

MNAR $=$ Missing not at random 

ME $=$ Measurement equivalence 

MI $=$ Multiple imputation 

MI-LGC $=$ Multiple-indicator latent growth curve 

ML $=$ Maximum likelihood 

MTMM $=$ Multitrait–multimethod 

MTMS $=$ Multitrait–multistate 

PSR $=$ Potential scale reduction 

RAM $=$ Reticular analysis modeling 

RMSEA $=$ Root mean square error of approximation 

SEM $=$ Structural equation modeling 

SRMR $=$ Standardized root mean square residual 

STMS $=$ Singletrait–multistate 

STMS-IS $=$ Singletrait–multistate with indicator-specific factors 

SWB $=$ Subjective well-being 

TLI $=$ Tucker–Lewis index 

TSE $=$ Trait–state error 

WLSMV $=$ Mean- and variance-adjusted weighted least squares estimation of the model parameters 

# Guide to Statistical Symbols

# GREEK SYMBOLS GUIDE

α $=$ Greek letter alpha; used to denote additive constants (intercepts) 

$\beta$ $=$ Greek letter beta; used to denote regression coefficients 

γ $=$ Greek letter gamma; used to denote regression coefficients and factor loadings; $\boldsymbol { \gamma } _ { 0 }$ is also used to indicate the FMI 

δ $=$ Greek letter delta; used to denote regression coefficients and factor loadings 

∆ $=$ Greek capital letter delta; used to denote a difference 

ε $=$ Greek letter epsilon; used to denote measurement error variables 

ζ $=$ Greek letter zeta; used to denote state residual variables and factors 

λ $=$ Greek letter lambda; used to denote factor loadings 

ξ $=$ Greek letter xi; used to denote latent trait variables and factors 

ς $=$ Greek letter final sigma; used to denote latent residual variables 

τ $=$ Greek letter tau; used to denote true score variables in CTT and LS variables or factors in LST theory 

ϕ $=$ Greek letter phi; used to denote correlations among latent variables 

ω $=$ Greek letter omega; used to denote latent residual variables 

# MATHEMATICAL COEFFICIENTS, INDICES, SYMBOLS, AND VARIABLES

<table><tr><td>c</td><td>= Index for a specific construct</td></tr><tr><td>CCon</td><td>= Common consistency</td></tr><tr><td>Con</td><td>= (Total) consistency</td></tr><tr><td>Cov</td><td>= Covariance</td></tr><tr><td>Corr</td><td>= Correlation; also abbreviated as r</td></tr><tr><td>CV</td><td>= Convergent validity</td></tr><tr><td>d</td><td>= Cohen&#x27;s d (standardized effect size measure for mean differences)</td></tr><tr><td>df</td><td>= Degrees of freedom</td></tr><tr><td>e</td><td>= Index for a specific construct</td></tr><tr><td>E</td><td>= Expectation (mean)</td></tr><tr><td>E(.|.)</td><td>= Conditional expectation (regression)</td></tr><tr><td>i</td><td>= Index for a specific indicator (e.g., Test/Measure/Item)</td></tr><tr><td>ICC</td><td>= Intraclass correlation coefficient</td></tr><tr><td>IS</td><td>= Indicator specificity</td></tr><tr><td>ISi</td><td>= Indicator-specific residual factor for indicator i</td></tr><tr><td>j</td><td>= Index for a specific indicator (e.g., Test/Measure/Item)</td></tr><tr><td>m</td><td>= Index for the last (or total number of) indicator(s)</td></tr><tr><td>M</td><td>= Mean</td></tr><tr><td>n</td><td>= Index for the last (or total number of) time point(s)/measurement occasion(s); also used to indicate the number of individuals in a subsample or subgroup</td></tr><tr><td>N</td><td>= Total sample size (number of individuals in the entire sample, including all subsamples/subgroups)</td></tr><tr><td>o</td><td>= Index for the last (or total number of) constructs</td></tr><tr><td>Ot</td><td>= Latent occasion residual variable at Time t</td></tr><tr><td>Osp</td><td>= Occasion specificity</td></tr><tr><td>p</td><td>= Probability (p-value); also used as an index to denote a specific time period in the LST-TC model</td></tr><tr><td>q</td><td>= Index for a specific time period in the LST-TC model</td></tr></table>

r $=$ Correlation coefficient; also used as an index to denote the last (or total number of) time period(s) in the LST-TC model 

Rel $=$ Reliability 

s $=$ Index for a specific time point (measurement occasion) 

$S _ { t }$ $=$ A specific value (situation) on the theoretical situation variable $S _ { t }$ in LST-R theory 

$S _ { t }$ $=$ Theoretical situation variable at Time t in LST-R theory 

SCon $=$ Situation consistency 

SD $=$ Standard deviation 

SE $=$ Standard error 

t $=$ Index for a specific time point (measurement occasion) 

TCon $=$ Trait consistency 

$u _ { t }$ $=$ A specific value (person) on the observational unit (person) variable $U _ { t }$ in LST-R theory 

$U _ { t }$ $=$ Observational unit (person) variable at Time t in LST-R theory 

UCon $=$ Unique consistency 

Var $=$ Variance 

Var(R) $=$ Common latent residual variance 

$Y _ { i t }$ $=$ Measured (observed) variable pertaining to Test/Measure/Item i at Time t 

z $=$ Standardized score or test statistic that follows a standard normal $( z )$ distribution with a mean of 0 and a standard deviation of 1 

# 1

# A Measurement Theoretical Framework for Longitudinal Data Introduction to Latent State–Trait Theory

# 1.1 INTRODUCTION

In this book, I introduce and discuss longitudinal statistical models with latent variables from a measurement theoretical perspective. Why is this useful? At least five reasons come to mind. First, there is no quantitative longitudinal data analysis without measurement. Before we can analyze repeated measures data, we have to collect the data. Collecting data typically means taking measurements from people or animals in some form. In longitudinal studies, we repeatedly measure, for example, individuals’ self-report questionnaire item responses, test scores, or physiological parameters—or we might collect data from external observers. Hence, longitudinal analysis is fundamentally linked to issues of measurement. Measurement theories help us formalize what happens when we take measurements and formulate statistical measurement models that we can apply to the empirical data. 

Second, measurements in the social sciences are typically not free of random measurement error. That is, reliability estimates for most variables in the social sciences are smaller than 1.0, indicating less than perfectly precise measurements. Measurement error leads to bias in statistical estimates (e.g., correlations and regression coefficients) and can lower statistical power. Measurement theory addresses the measurement error problem and allows us to formulate measurement models that separate true score (i.e., error-free) variance from 

measurement error variance in measured variables. Measurement models also make it possible to quantify the degree of (un)reliability of our measurements and to correct for unreliability by using latent variables that are by definition free of random measurement error. 

Correcting for measurement error is of particular importance in longitudinal data analysis because measurement error can lead to distortions such as artificial regression to the mean and unreliable change scores. Hence, there is a need for appropriate longitudinal measurement models that correct for measurement error to reduce bias in parameter estimates. All longitudinal models that I present in subsequent chapters account for measurement error and allow estimating the reliability of the repeated measures. 

Third, most modern longitudinal methods (and all methods described in this book) use latent variables to represent individual differences at a given moment in time as well as individual differences in change over time. What are latent variables? How can they be unambiguously defined mathematically so that we know how to interpret them correctly? Measurement theories provide clear answers to these questions. Hence, measurement theories also help us clarify what exactly the latent variables in our longitudinal measurement models represent and how they should be properly interpreted. I provide definitions of latent variables that play a key role in longitudinal models later on in this chapter when I introduce the concepts of latent state–trait theory. 

Fourth, one complication in longitudinal data is that measurement equivalence across time needs to be established in order to meaningfully interpret change scores. The measurement equivalence assumption can be understood as an “apples and oranges” problem. Only when measures maintain the same links (i.e., factor loadings and intercepts) to the underlying latent variables that they are supposed to measure across time are comparisons of, for example, latent variable means between different time points interpretable and meaningful. Measurement equivalence is thus a prerequisite for a meaningful analysis of changes across time. As the term measurement equivalence suggests, this assumption obviously has its foundations in measurement theory. Introducing longitudinal models based on measurement theory thus facilitates our understanding and proper application of the concept of measurement equivalence. I deal with the issue of measurement equivalence in detail in Chapter 4. 

Fifth, researchers conducting longitudinal studies frequently encounter socalled variable-specific or method effects. This means that measured variables frequently contain unique aspects that they do not share with other indicators of the same construct. Such method- or indicator-specific variance components can lead to complex patterns of covariances across time and can cause misfit in longitudinal models that do not include method factors. Measurement theory allows us to define method factors in a clear way so as to properly model such 

variable-specific effects. I present longitudinal models with method factors and other ways to deal with method effects in Chapters 4 and 5. 

In the next section, I provide an introduction to latent state–trait theory, which represents a comprehensive measurement theoretical framework for longitudinal analyses. All statistical models presented in this book can be formulated based on the concepts of this theory. 

# 1.2 LATENT STATE–TRAIT THEORY

# 1.2.1 Introduction

Latent state–trait (LST) theory (Steyer, Ferring, & Schmitt, 1992; Steyer, Mayer, Geiser, & Cole, 2015; Steyer, Schmitt, & Eid, 1999) is a longitudinal measurement theory that allows us to separate true individual differences from individual differences due to random measurement error. LST theory also provides us with clear mathematical foundations and unambiguous definitions of state, trait, and state residual latent variables that allow researchers to measure these components in longitudinal data. LST theory helps us clarify what measurement equivalence means and why it is useful to establish measurement equivalence for specific model parameters in longitudinal models. Moreover, based on the concepts of LST theory, researchers can formulate models with method factors that have a clear meaning and interpretation. 

LST theory was first presented in the late 1980s and early 1990s (e.g., Steyer, Majcen, Schwenkmezger, & Buchner, 1989). The original theory used a rather rigid trait concept. This concept assumed that a trait variable depended only on person characteristics. Previous experiences or situations were not allowed to have an influence on traits over time. The trait concept in LST theory has since been revised to allow for a more dynamic view of persons. In the revised version of LST theory, which is referred to as latent stait–trait revised (LST-R) theory (Steyer et al., 2015), traits can change over time due to the previous situational influences and/or experiences of individuals. 

In this book, I present the basic concepts of LST-R theory as described in Steyer et al. (2015). Nonetheless, many features of the original LST theory remain unchanged, and most of the longitudinal statistical models described in the subsequent chapters of this book can be formulated based on either classical or LST-R theory. 

# 1.2.2 Basic Idea

The basic idea of both classical and revised LST theory is that measurements in the social sciences do not take place in a situational vacuum. Rather than 

measuring just person characteristics (“traits”), part of the measurement usually reflects situational influences and/or person $\times$ situation interactions. For example, mood measurements tend to be influenced not only by individuals’ habitual mood levels, but also by external (situational) influences. Moreover, individuals with higher positive trait mood may react more or less strongly to “daily hassles” than individuals with lower habitual mood levels, which would indicate the presence of a person $\times$ situation interaction effect. 

The concept of measuring “persons-in-situations” rather than just persons is in contrast to classical test theory (CTT) and other “trait” theories (e.g., the Rasch model in item response theory), which do not explicitly account for situational influences on measurements. LST theory can therefore be understood as an extension of CTT. LST theory assumes that individuals’ measured scores can be a function of trait, situational/interactional, and random measurement error components (and that true scores can be a function of trait and situational/interactional components). In contrast, CTT considers only person (trait) and error effects (see Box 1.1 on page 7). Models of CTT can thus be seen as special cases of LST models that are, strictly speaking, appropriate only when measurements contain no situational or interactional components. This may be (approximately) the case for rather stable personality traits such as intelligence. 

In classical LST theory, the “person” was conceptualized as a static entity. That is, the person him- or herself was not expected to undergo changes between different time points due to experiences or previous situational influences (although models of trait changes could also be formulated within the old theory; see, e.g., Eid & Hoffman, 1998). This appeared to be a rather unrealistic feature of classical LST theory, as individuals obviously make experiences and encounter (more or less critical) life events that may change the person to a smaller or larger degree. 

LST-R theory was developed to address this limitation of classical LST theory. A new feature in LST-R theory is that person effects (“traits”) themselves can also be subject to changes over time due to experiences that a person makes between two or more measurement occasions and/or due to previous situations that change subsequent trait scores. For example, a person may experience a school shooting in between two measurements of his or her attitude toward gun control. Such an experience could lead to permanent modifications of the person’s attitude toward gun control (i.e., the person’s trait) and other psychological traits. 

Next, I describe the fundamental concepts of LST-R theory. I begin with the random experiment that describes formally what happens when we collect longitudinal data. Subsequently, I show how latent state, trait, state residual, and measurement error variables are defined in LST theory and identify the properties these variables have that follow directly from their definitions. These 

latent variables play a key role in all longitudinal models described in all subsequent chapters, so an understanding of their definition, meaning, and properties is crucial. 

# 1.2.3 Random Experiment

Let the indices t, s, and n $( t , s = 0 , \ldots , n )$ refer to the tth, sth, and nth time point (measurement occasion), respectively, where n denotes the last measurement occasion (or total number of time points). Then, the random experiment considered in LST-R theory can be described by the following five steps (for more details, see Steyer et al., 2015): 

1. A person (generally, an “observational unit” $u _ { 0 } )$ is sampled from a set of persons at Time $t = 0$ , that is, before his or her behavior is recorded for the first time. 

2. The person is making experiences $e _ { 1 }$ in the time period before his or her behavior is observed (“measured”) for the first time at Time $t = 1$ (see Step 4). 

3. The person $\boldsymbol { u } _ { 1 } = ( u _ { 0 } , e _ { 1 } )$ is in situation $s _ { 1 }$ when his or her behavior is recorded for the first time at Time $t = 1$ (see Step 4). 

4. Observations $o _ { 1 }$ of the person’s behavior are made at Time $t = 1$ (i.e., measurements are taken, e.g., through self-report questionnaires, tests, or external observers). 

5. Steps 2 through 4 are repeated for times $t = 2 , \ldots , n$ $t = 2$ 

These five steps have several important implications. First, measurements of individuals do not take place in a situational vacuum. Instead, they can be influenced by the situations st that are present at a given measurement occasion t. Second, not only situations, but also persons can change over time. Person changes can be due to (1) experiences that a person makes in between measurement occasions, (2) situational influences at previous measurement occasions, and/or (3) the observations themselves (e.g., filling out a questionnaire on attitude toward gun control could by itself influence a person’s attitude toward gun control). 

# 1.2.4 Variables in LST‑R Theory

Repeated measurements of multiple individuals result in observed variables (indicators, items, measured variables), which are indicated as $Y _ { i t }$ . The indices i, j, and m (i, $j = 1$ , . . . , m) denote the ith, jth, and mth observed variable, 

respectively. This means that we may assess multiple indicators of the same construct (e.g., multiple items). For example, $Y _ { i t }$ and $Y _ { j t }$ may represent measured variables representing the scores on two different items or subscales measuring attitude toward gun control at the same time point t. The index m refers to the last measured variable in a set of variables or, in other words, to the total number of measured variables. (In Chapters 2 and 3, I describe longitudinal models for a single repeatedly measured variable, whereas Chapters 4 and 5 deal with models for multiple indicators.) 

In addition to the observed variables $Y _ { i t } ,$ LST theory also considers person and situation variables. The values of the person variables $U _ { t }$ are the persons $u _ { t }$ . In contrast to the original LST theory, there are multiple person variables in LST-R theory, one for each time point t. This reflects the fact that individuals can change across time. The values of the situation variables $S _ { t }$ are the situations $S _ { t }$ that occur at a given time point t. The situation concept in LST theory is rather broad. Situations can be defined by, for example, psychological, physical, social, societal, or biological conditions as well as by a combination between those conditions. Examples of situations are (1) being in a bad mood, (2) having a migraine, (3) being alone versus at a party, (4) experiencing a civil war, or (5) being pregnant. 

The situation variables are theoretical in nature and do not have to be observed in empirical studies. This means that the specific situations themselves do not have to be known to the researcher in order to separate situational effects from person (trait) and measurement error effects through LST analysis. However, specific research questions about the impact of specific situations would require the situations to be explicitly observed or even manipulated; however, for the usual purposes of LST analyses, this is not necessary. (This point will become clearer later on when I describe actual models of LST theory.) 

Based on the observed variables $Y _ { i t } .$ as well as the theoretical person and situation variables $U _ { t }$ and $S _ { t } ,$ we can define the fundamental latent variables of LST-R theory. The definition of latent variables in LST-R theory is based on the concept of hypothetical intraindividual score distributions. This is analogous to how CTT defines true score variables (see Box 1.1 for details). In CTT, individuals’ true scores (the values of the true score variable for a given measure) are defined as the means (“expectations”) of intraindividual score distributions across a large number of (hypothetical) administrations of the same test or other measure. 

For example, if a person could be asked about his or her attitude toward gun control many times with the same questionnaire (assuming that the person shows no true changes in attitude as well as no memory, fatigue, learning, or other systematic effects that change his or her true attitude), then that person’s 

# BOX 1.1. Key Concepts and Definitions in CTT

CTT considers only person, but not situation, effects. As a consequence, a true score variable $\tau _ { \mathrm { i } }$ is defined as the conditional expectation of an observed variable $Y _ { i }$ given the person variable $U$ only: 

$$
\tau_ {i} \equiv E (Y _ {i} \mid U)
$$

Note that none of the variables in the above equation carries a subscript $t$ for time, given that CTT does not consider different situations or the fact that persons could change across time. The values of the true score variable $\tau _ { \mathrm { i } }$ are the intraindividual (person- specific) means of a hypothetical intraindividual distribution of test scores. Such an intraindividual score distribution is not typically observed in practice but is useful to consider in order to understand what a true score is according to CTT. Measurement error variables in CTT are defined as the difference between an observed variable and its corresponding true score variable: 

$$
\varepsilon_ {i} \equiv Y _ {i} - \tau_ {i}
$$

Based on the definition of the measurement error variable $\varepsilon _ { \mathrm { i } }$ , we can decompose a measured variable into a true score variable and a measurement error variable in CTT: 

$$
Y _ {i} = \tau_ {i} + \varepsilon_ {i}
$$

$\tau _ { \mathrm { i } }$ and $\varepsilon _ { i }$ are by definition uncorrelated in CTT, so that the variance of a measured variable can be decomposed additively: 

$$
V a r (Y _ {i}) = V a r (\tau_ {i}) + V a r (\varepsilon_ {i})
$$

An important coefficient in CTT is the reliability coefficient $R e l ( Y _ { i } )$ , which allows quantifying measurement precision: 

$$
\begin{array}{l} R e l (Y _ {i}) = V a r (\tau_ {i}) / V a r (Y _ {i}) \\ = 1 - \left[ \operatorname {V a r} \left(\varepsilon_ {i}\right) / \operatorname {V a r} \left(Y _ {i}\right) \right] \\ \end{array}
$$

The $R e l ( Y _ { i } )$ coefficient varies between 0 and 1, with values close to 1 indicating high measurement precision. 

true score could be estimated as the mean of the resulting intraindividual score distribution. Deviations from the intraindividual average indicate measurement error. Even though this scenario is unrealistic and not practical and merely represents a “thought experiment,” it is useful to consider because it allows us to clearly define the latent variables that play a role in our longitudinal measurements (including measurement error). 

The same basic idea of defining latent variable scores as the means of intraindividual score distributions is used in LST-R theory. However, in contrast to CTT, LST-R theory considers more than just a single score distribution. This is because according to LST-R theory, both persons and situations can change across time. Therefore, separate intraindividual score distributions are considered for each measurement occasion. 

In LST-R theory, a latent state variable $\tau _ { i t }$ is defined as the conditional expectation of an observed variable $Y _ { i t }$ given the person and situation variables at Time t: 

$$
\tau_ {i t} \equiv E (Y _ {i t} \mid U _ {t}, S _ {t})
$$

where the $\equiv$ symbol indicates a definition and $E ( \mathbf { \theta } , | \mathbf { \theta } , \mathbf { \alpha } )$ is a conditional expectation. The values of the latent state variable $\tau _ { i t }$ are given by 

$$
\tau_ {i t} \left(u _ {t}\right) \equiv E \left(Y _ {i t} \mid U _ {t} = u _ {t}, S _ {t} = s _ {t}\right)
$$

In other words, a person’s latent state score at Time $t$ is equal to that person’s (hypothetical) intraindividual mean in situation $S _ { t } .$ . A measurement error variable $\varepsilon$ is defined as a difference score variable: 

$$
\varepsilon_ {i t} \equiv Y _ {i t} - \tau_ {i t}
$$

Hence, a person’s error score is the difference between that person’s measured score and latent state score. The definition is analogous to CTT except that the latent state variable considers both persons and situations, whereas the true score variable in CTT considers person effects only. 

A latent trait variable $\xi _ { i t }$ is defined as the conditional expectation of $Y _ { i t }$ given the person variable at Time $t$ only: 

$$
\xi_ {i t} \equiv E (Y _ {i t} \mid U _ {t})
$$

The values of $\xi _ { i t }$ are thus analogous to the true scores in CTT (which also consider person effects only), except that the person variable $U _ { t }$ in LST-R theory 

is time-specific and thus allows person characteristics to change between time points (e.g., due to experiences or previous situations). This can be seen from the fact that the person variable $U _ { t }$ has a subscript t and can thus vary between measurement occasions. The person variable in CTT has no such subscript. 

Finally, a latent state residual variable is defined as a difference score variable between state and trait latent variables: 

$$
\zeta_ {i t} \equiv \tau_ {i t} - \xi_ {i t}
$$

The latent state residual scores thus characterize deviations of the state scores from the trait scores. They reflect systematic situation and/or person $\times$ situation interaction effects (i.e., effects that are neither pure person effects nor effects of measurement error). In other words, whenever a person’s latent state score differs from his or her latent trait score, this indicates the presence of a situational or person $\times$ situation interaction effect. 

In summary, we obtain the following decomposition of the latent state variables $\tau _ { i t }$ and measured variables $Y _ { i t }$ in LST-R theory: 

$$
\begin{array}{l} \tau_ {i t} = \zeta_ {i t} + \zeta_ {i t} \\ Y _ {i t} = \tau_ {i t} + \varepsilon_ {i t} \\ = \zeta_ {i t} + \zeta_ {i t} + \varepsilon_ {i t} \\ \end{array}
$$

In words, a latent state is the sum of trait (person) effects and state residual (situation and/or person $\times$ situation interaction effects). A measured variable is the sum of trait, state residual, and measurement error effects. 

Figure 1.1 illustrates the basic LST-R decomposition in a path diagram. For simplicity, the diagram shows a single measured variable that is assessed on four measurement occasions. (Given that only a single measured variable is considered, I dropped the index i for the indicator in the figure.) In the path diagram, single-headed paths indicate a directional relationship with the implicit coefficient (“loading”) being fixed to 1.0 for all paths. Double-headed arrows pointing to the same variable represent variance parameters. Double-headed arrows between different variables would represent covariance parameters but are not shown in the figure to avoid clutter. (In Box 1.2, I discuss which covariances are equal to zero by definition in LST-R theory.) The triangle in the figure symbolizes a constant value of 1.0 that adds the mean structure (expectations E) to the model. According to LST-R theory, the mean structure originates from the latent trait variables; the latent state residual and measurement error variables have means of zero by definition (see Box 1.2). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/d536d45e796f95b82c417d4ab94d432a4fb82875b4f3daa11ba138475ea1dcb0.jpg)



FIGURE 1.1. Path diagram illustrating the basic variable decomposition in LST-R theory. $Y _ { t } =$ measured variable at Time t; $\xi _ { t } =$ trait variable; $\tau _ { t } =$ latent state variable; $\zeta _ { t }$ $=$ latent state residual variable; $\varepsilon _ { t } =$ measurement error variable. Covariances between variables are not shown in the figure to avoid clutter.


We can see that according to LST-R theory, each measured variable has its own (measure- and time-specific) latent trait, state, state residual, and measurement error component with associated unknown mean, variance, and covariance parameters. Obviously, the basic LST-R decomposition leads to many more free parameters than can be mathematically identified. However, various mathematically identified and testable statistical models (as described in Chapters 2 and 3) can be derived from the basic LST-R decomposition by making different homogeneity assumptions about the latent variables and/or assumptions about stability and change in the latent variables across time. For example, a model with a single-trait factor (the so-called random intercept model; see Chapter 2, Section 2.2) can be obtained by making the assumptions that (1) all trait variables in Figure 1.1 are identical and (2) all state residual variables are equal to zero. 

# 1.2.5 Properties

The definitions of latent variables that I have presented rest on the rather unrestrictive assumption that the observed variables have positive and finite 

variances. This assumption should be fulfilled in virtually all practical social science applications. The above definitions have implications for the means, variances, and covariances of the observed and latent variables. Importantly, these implications follow without making any additional assumptions. Key implications are summarized in Box 1.2. 

# 1.2.6 Coefficients

Based on the properties described in Box 1.2, coefficients can be defined that allow us to quantify the degree of consistency (trait effects), occasion specificity (situation and person $\times$ situation interaction effects), and reliability (precision) in our measurements. The consistency coefficient $C o n ( Y _ { i t } )$ reflects the proportion of observed variable variance that is due to trait (person-specific) effects: 

$$
C o n (Y _ {i t}) = \operatorname {V a r} (\xi_ {i t}) / \operatorname {V a r} (Y _ {i t})
$$

$C o n ( Y _ { i t } )$ varies between 0 and 1, with higher values indicating that a measure reflects more trait influences. 

The occasion-specificity coefficient $O s p ( Y _ { i t } )$ reflects the proportion of observed variable variance that is due to situation and/or person $\times$ situation interaction effects: 

$$
O s p (Y _ {i t}) = \operatorname {V a r} (\zeta_ {i t}) / \operatorname {V a r} (Y _ {i t})
$$

$O s p ( Y _ { i t } )$ also varies between 0 and 1, with higher values indicating that a measure reflects more situational and/or person $\times$ situation interaction influences. 

The reliability coefficient $R e l ( Y _ { i t } )$ reflects the total proportion of true score variance in an observed variable and is equal to the sum of consistency plus occasion specificity: 

$$
\begin{array}{l} \operatorname {R e l} \left(Y _ {i t}\right) = \operatorname {V a r} \left(\tau_ {i t}\right) / \operatorname {V a r} \left(Y _ {i t}\right) \\ = \left[ \operatorname {V a r} \left(\xi_ {\mathrm {i t}}\right) + \operatorname {V a r} \left(\zeta_ {\mathrm {i t}}\right) \right] / \operatorname {V a r} \left(Y _ {\mathrm {i t}}\right) \\ = \left[ \operatorname {V a r} \left(\xi_ {i t}\right) + \operatorname {V a r} \left(\zeta_ {i t}\right) \right] / \left[ \operatorname {V a r} \left(\xi_ {i t}\right) + \operatorname {V a r} \left(\zeta_ {i t}\right) + \operatorname {V a r} \left(\varepsilon_ {i t}\right) \right] \\ = 1 - \left[ \operatorname {V a r} \left(\varepsilon_ {i t}\right) / \operatorname {V a r} \left(Y _ {i t}\right) \right] \\ = C o n \left(Y _ {i t}\right) + O s p \left(Y _ {i t}\right) \\ \end{array}
$$

The reliability coefficient thus has the same meaning as it does in CTT: It quantifies the proportion of measured score variability that is due to systematic sources of variability $\zeta _ { i t }$ and $\zeta _ { i t } ^ { } )$ rather than unsystematic measurement error $( \varepsilon _ { i t } )$ . 

# BOX 1.2. Properties of the Latent Variables in LST-R Theory

One important advantage of explicitly defining latent variables as conditional expectations of measured variables is that we now know exactly what the latent variables represent. Another advantage of this approach is that certain properties of the latent variables follow directly from their definitions—“directly” here meaning “without making further assumptions.” In this box, I describe some of the most important properties that follow from the definitions of the latent variables described in the text without any additional assumptions. 

Being defined as residual variables, the means (expectations E) of the measurement error variables and latent state residual variables are always equal to zero: 

$$
E (\varepsilon_ {i t}) = E (\zeta_ {i t}) = 0
$$

This property tells us that we need not (and should not) estimate means for the error and state residual latent variables in practical applications of LST-R models. Doing so would not be in line with how these variables are defined in LST-R theory. 

Measurement error variables are uncorrelated with state residual variables ( $C o v =$ covariance): 

$$
C o v (\varepsilon_ {i t}, \zeta_ {j s}) = 0
$$

Measurement error variables pertaining to different time points are uncorrelated: 

$$
C o v \left(\varepsilon_ {i t}, \varepsilon_ {j s}\right) = 0 \text {f o r} t \neq s
$$

Notice that this holds true for error variables pertaining to either the same measure or different measures. Of importance, this property means that models with correlated error variables for the same measure across time (which are often used in practice) are not in line with LST-R theory. In Chapters 4 and 5, I present models that account for indicator- specific effects without including correlated error variables. 

State residuals pertaining to different time points are uncorrelated: 

$$
C o v (\zeta_ {i t}, \zeta_ {j s}) = 0 \text {f o r} t \neq s
$$

For two time points s and t, where $s \leq t$ , measurement error variables are uncorrelated with latent state and latent trait variables: 

$$
C o v (\varepsilon_ {i t}, \tau_ {j s}) = C o v (\varepsilon_ {i t}, \xi_ {j s}) = 0 \mathrm {f o r} s \leq t
$$

For two time points s and t, where $s \leq t$ , state residual variables are uncorrelated with latent trait variables: 

$$
C o v (\zeta_ {i t}, \zeta_ {j s}) = 0 \text {f o r} s \leq t
$$

The last property means that state residuals cannot be correlated with present or previous traits. However, correlations between state residuals and future traits are allowed in LST-R theory. That is, situations can influence future trait scores. 

Overall, the covariance properties tell us that we need not (and should not) estimate the above covariances in empirical applications as this would jeopardize the meaning of the latent variables in our application. Another useful consequence of the above uncorrelatedness properties is that the variance decompositions for the measured and latent state variables are additive: 

$$
\begin{array}{l} V a r \left(Y _ {i t}\right) = V a r \left(\zeta_ {i t}\right) + V a r \left(\zeta_ {i t}\right) + V a r \left(\varepsilon_ {i t}\right) \\ V a r (\tau_ {i t}) = V a r (\xi_ {i t}) + V a r (\zeta_ {i t}) \\ \end{array}
$$

The additive variance decompositions allow for the definition of coefficients such as consistency, occasion specificity, and reliability that are of key interest in most LST-R analyses. These coefficients are described in detail in the text. 

The consistency and occasion- specificity coefficients can also be defined for the latent state variables, in which case the two coefficients quantify the proportion of trait and situation/interaction variance relative to total true score variance and add up to 1 for a given variable: 

$$
\begin{array}{l} C o n (\tau_ {i t}) = V a r (\xi_ {i t}) / V a r (\tau_ {i t}) \\ = V a r \left(\xi_ {i t}\right) / \left[ V a r \left(\xi_ {i t}\right) + V a r \left(\zeta_ {i t} ^ {\prime}\right) \right] \\ \end{array}
$$

$$
\begin{array}{l} O s p \left(\tau_ {i t}\right) = \operatorname {V a r} \left(\zeta_ {i t}\right) / \operatorname {V a r} \left(\tau_ {i t}\right) \\ = \operatorname {V a r} \left(\zeta_ {i t}\right) / \left[ \operatorname {V a r} \left(\xi_ {i t}\right) + \operatorname {V a r} \left(\zeta_ {i t}\right) \right] \\ = 1 - C o n (\tau_ {i t}) \\ \end{array}
$$

Defining the consistency and occasion- specificity coefficients for the latent state variables $\tau _ { i t }$ (rather than the measured variables $Y _ { i t } )$ makes it easier to see which proportion of the true score variance is due to traits versus situation/interaction effects because measurement error is excluded. When $C o n ( \tau _ { i t } ) > . 5$ , this indicates 

that a measure reflects more trait than situation/interaction variance. In contrast, when $O s p ( \tau _ { i t } ) > . 5$ , this indicates that a measure reflects more situation/ interaction variance than trait variance. 

# 1.3 CHAPTER SUMMARY

An important component in quantitative longitudinal studies is measurement: We observe behavior or record test or questionnaire scores for the same individuals on multiple measurement occasions. Measurement theories help us formalize what happens when we observe individuals’ behavior repeatedly, define latent variables based on conditional expectations of observed variables, and formulate statistical measurement models that we can apply to the empirical data to measure the latent variables of interest. Measurement models typically contain latent variables as well as variables representing errors of measurement. Most measurements in the social sciences are prone to random measurement error; measurement theories help us formalize the error concept and allow us to define latent variables that capture different components of true score variance. Based on explicit mathematical definitions, measurement theories clarify the meaning, interpretation, and properties of the latent variables that appear in our longitudinal statistical models. 

LST theory is a longitudinal measurement theory that specifically addresses (1) the measurement error problem and (2) the fact that social science measurements of persons do not take place in a situational vacuum. Whereas the original version of LST theory implied a rather static person concept, the newer LST-R theory accounts for the fact that persons themselves can change over time due to experiences, situations, and previous measurements. 

LST theory allows defining latent variables that reflect (1) persons-insituations (latent state variables), (2) persons only (latent trait variables), (3) situation and/or person $\times$ situation interactions (latent state residual variables), and (4) random measurement error. These variables have properties that follow directly from their definition. For example, trait, state residual, and measurement error variables are uncorrelated for a given variable at the same time point, which leads to an additive variance decomposition. Based on the additive variance decomposition, coefficients can be defined for quantifying consistency (trait effects), occasion specificity (situation and person $\times$ situation interaction effects), and reliability of longitudinal measurements. 

The basic concepts of LST-R theory presented in this chapter are useful in that they provide formalization and clear definitions of the relevant concepts and allow deriving basic properties. However, the basic LST-R decomposition 

as illustrated in Figure 1.1 does not lead to an identifiable longitudinal statistical model. In order to obtain statistical models that are mathematically identified and testable in practice, further assumptions have to be introduced. Those assumptions (or “restrictions”) lead to a reduction in the number of latent variables and unknown model parameters. In the following chapters, I show how identified statistical models can be obtained based on the concepts of LST-R theory. In Chapters 2 and 3, I focus on models for single-indicator longitudinal designs. Chapters 4 and 5 deal with more complex longitudinal LST-R models for multiple-indicator designs. 

# 1.4 RECOMMENDED READINGS



Steyer, R., Ferring, D., & Schmitt, M. (1992). States and traits in psychological assess‑ ment. European Journal of Psychological Assessment, 8, 79–98. 





Steyer, R., Mayer, A., Geiser, C., & Cole, D. A. (2015). A theory of states and traits— revised. Annual Review of Clinical Psychology, 11, 71–98. 



# 2

# Single‑Factor Longitudinal Models for Single-­ Indicator Data

# 2.1 INTRODUCTION

In Chapter 1, I introduced the basic concepts of latent state–trait revised (LST-R) theory. These concepts rested on a rather small and unrestrictive set of assumptions (e.g., positive and finite variances of observed variables). LST-R theory allows us to define latent state, trait, state residual, and measurement error variables based on conditional expectations of observed variables and to examine their properties. The definitions of the latent variables that I presented in Chapter 1 are useful because they provide us with latent variables that are relevant to longitudinal studies and make clear what the latent variables mean. 

On the other hand, the definitions by themselves do not result in identified and testable statistical models for longitudinal data analysis. This can be easily seen from the fact that according to LST-R theory, each observed variable at each time point is decomposed into its own trait, state residual, and measurement error variable. Our observed data do not contain enough information to identify all of the relevant latent variable means, variances, and covariances. Specific longitudinal measurement models introduce simplifying restrictions that reduce the number of latent variables as well as the number of parameters to be estimated. 

In this chapter, I introduce very simple longitudinal measurement models with just a single latent factor and a single indicator per measurement occasion. I show how longitudinal measurement models for a single repeatedly measured variable can be obtained by making assumptions, for example, about the 

homogeneity and (in)dependence of certain latent variables. These assumptions reduce the number of latent variables that need to be considered in a model. They also lead to (1) identified statistical models that can be estimated based on observed data and (2) testable restrictions that allow us to potentially falsify these assumptions based on tests of model fit. 

In this chapter as well as in Chapter 3, I focus on single-indicator data, that is, models for longitudinal designs that use only a single repeatedly measured observed variable $Y _ { t }$ for each construct at each time point t. Chapter 3 deals with single-indicator longitudinal models that use more than one latent factor. Many of the models discussed in Chapters 2 and 3 have counterparts for multipleindicator data, which I discuss in Chapter 5. 

# 2.2 THE RANDOM INTERCEPT MODEL

# 2.2.1 Introduction

The random intercept model is one of the simplest and most restrictive measurement models that can be fit to longitudinal data. It assumes that individuals’ trait scores do not change across time. Therefore, it is frequently used as a baseline model in longitudinal analyses. If the random intercept model shows a good fit to the data at hand, this may indicate that a construct did not change across time. In this case, more complex longitudinal models may not be needed. 

# 2.2.2 Model Description

The random intercept model for a single construct and four time points is depicted in Figure 2.1 as a path diagram. In the path diagram, the triangle represents a constant of 1.0 that serves to add the mean structure (means and constant intercepts) to the model. It can be seen that in this model, the repeatedly measured observed variable $Y _ { t }$ loads onto a single common trait factor $\xi .$ (I dropped the index i for the observed variable throughout this chapter, given that all models in this chapter assume only a single repeatedly measured observed variable.) All factor loadings are fixed to 1, and all measurement intercepts are fixed to zero. Hence, the model can be described by the following measurement equation: 

$$
Y _ {t} = \xi + \varepsilon_ {t}
$$

This model is called a random intercept model because there is no fixed intercept (i.e., additive constant) in the model equation. Instead, there is only a 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/ad45ae4acac47157b893052cd7a90f41ba8fef5064691d444a5f59f644833e5f.jpg)



FIGURE 2.1. Path diagram of the random intercept model for a single observed variable $Y _ { t }$ that is measured on four time points. $\xi =$ trait (random intercept) factor; $\varepsilon _ { t } =$ measurement error variable.


random intercept that is represented by the trait factor $\xi$ . The trait factor is considered a random intercept because its values can vary across individuals (fixed intercepts, in contrast, are constants that do not vary between individuals). 

The random intercept model estimates the following parameters: 

•	 the trait factor mean $E ( \xi )$ , 

•	 the trait factor variance $V a r ( \xi )$ , and 

•	 n measurement error variances $V a r ( \varepsilon _ { t } )$ , one for each for each time point $t = 1 .$ $t = 1 , \ldots , n .$ . 

Therefore, the model in general has $n + 2$ free model parameters, where n indicates the total number of measurement occasions. In our example, we have four measurement occasions $( n = 4 )$ . Therefore, our model has $4 + 2 = 6$ free parameters. 

In our example with four time points, we have 14 pieces of available information (four Y variances, four $Y _ { t }$ means, and six unique $Y _ { t }$ covariances). The random intercept model in our example therefore has $1 4 - 6 = 8$ degrees of freedom (df; for general information on how to calculate the number of pieces of available information and df for single-indicator longitudinal models, see Box 2.1). 

Readers familiar with classical test theory (CTT) models may find that the random intercept model resembles the model of tau equivalence in CTT, which 

# BOX 2.1. Available Information, Model Degrees of Freedom, and Model Identification in Single-Indicator Longitudinal Designs

What information is used to estimate unknown model parameters in singleindicator longitudinal structural equation models, and how are a model’s degrees of freedom $( d f )$ calculated? In single- indicator longitudinal designs, we only have one (repeatedly observed) measure $( m = 1 )$ ) but $n > 1$ time points. We can therefore draw on n repeatedly measured variables $Y _ { 1 }$ , . . . , $Y _ { n }$ . Each measured variable $Y _ { _ t }$ has a mean $E ( Y _ { t } )$ , a variance $V a r ( Y _ { t } )$ , and covariances $C o v ( Y _ { t } ,$ $Y _ { s } )$ , $t \neq s$ , with all other measured variables. The observed $Y _ { t }$ means, variances, and covariances provide the information that we use to estimate the unknown model parameters in all longitudinal structural equation models described in this book. In empirical applications, we can compute the means, variances, and covariances for all $Y _ { t }$ variables based on our sample data. 

In single- indicator designs, we have n observed $Y _ { t }$ variances, n observed $Y _ { t }$ means, and $0 . 5 \cdot ( n ^ { 2 } - n )$ observed unique $Y _ { t }$ covariances from which we can estimate unknown model parameters. In total, there are $1 . 5 \cdot n + 0 . 5 \cdot n ^ { 2 }$ pieces of available information in single- indicator longitudinal designs. With one measure and four time points, we have $1 . 5 \cdot 4 + 0 . 5 \cdot 1 6 = 1 4$ pieces of available information (four $Y _ { t }$ variances, four $Y _ { t }$ means, and six unique $Y _ { _ t }$ covariances). 

The degrees of freedom $( d f )$ of a model are calculated as the number of pieces of available information minus the number of free (unknown) model parameters. Models with negative $( < 0 )$ df are underidentified models (there is not enough information available to estimate all unknown parameters). For example, the random intercept model is underidentified when there is only a single time point $\left( n = 1 \right)$ ). Models in which $d f = 0$ may be just identified (“saturated”). Saturated models cannot be tested because they always fit perfectly. An example of a saturated model is the random and fixed intercepts model (described in Section 2.3) for $n = 2$ time points. Models with $d f > 0$ may be overidentified and contain testable restrictions. Only overidentified models can be empirically falsified (e.g., based on a chi- square test of model fit). For example, the random intercept model is overidentified for $n \geq 2$ time points. 

Unfortunately, $d f \geq 0$ is only a necessary, but not a sufficient, condition for model identification. That is, models with zero or positive $d f$ may still be underidentified. More information on the general issue of structural equation model identification can be found, for example, in Bollen (1989). 

# BOX 2.2. Defining the Random Intercept Model Based on LST‑R Theory

The random intercept model can be defined using concepts of LST-R theory in a similar way as the tau- equivalence model can be defined using concepts of CTT. Three assumptions are required: 

1. $\xi$ -equivalence: The latent trait variables for all time points are identical, such that $\boldsymbol { \xi } _ { t } = \boldsymbol { \xi } _ { s } = \boldsymbol { \xi }$ for all t, $s = 1$ , . . . , n. 

2. No situation or person $\times$ situation interaction influences: All latent state residual variables are zero, $\zeta _ { t } = \zeta _ { s } = 0$ for all t, $s = 1 , \ldots , n$ $s = 1$ . 

3. Linear independence of trait and error variables: $C o v ( \xi , \ : \varepsilon _ { t } ) = 0$ for all t $= 1$ , . . . , n. 

Assumption 1 implies that individuals’ trait scores do not change across time. Hence, there is perfect stability of latent trait scores in this model. Figure 2.2 illustrates the model- implied patterns of trait scores for three hypothetical individuals. It can be seen that each individual trajectory is flat, indicating the perfect intraindividual stability of trait scores for all individuals. In actual data, this pattern may be plausible (at least approximately) for rather stable personality constructs such as intelligence. 

Assumption 2 implies that measurements reflect only trait (person) aspects of a construct and random measurement error. From the perspective of LST-R theory, the model is restrictive because it assumes that there are no situational influences or person $\times$ situation interaction effects that could also have an impact on the measurements. Any intraindividual differences that occur in observed $Y _ { t }$ scores across time are solely due to measurement error according to this model. This implies that the model would only be suitable for perfectly stable trait-like constructs that are unaffected by situational effects (or measures that reflect only the trait aspects of a construct). 

Assumption 3 prohibits any correlations between measurement error variables and the common latent trait factor, which is a standard assumption made in most structural equation models (and the default in Mplus). Notice that we do not need to make the assumption of uncorrelated errors, $C o v ( \varepsilon _ { t } , \varepsilon _ { s } ) = 0$ for $t \neq s$ , because this property already follows by definition of the error variables in LST-R theory (see Chapter 1, Box 1.2). That is, in all LST-R models, measurement error variables pertaining to different time points are uncorrelated by definition. (In Mplus all error variables are uncorrelated by default.) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/43c68da9dcd77cd68595b29a5a10dfdfc6c351163e9f8ab19859b9c0dad4558a.jpg)



FIGURE 2.2. Illustration of possible model-implied trait scores in the random intercept model for three hypothetical individuals. It can be seen that the model implies perfect stability (no changes) in the trait scores for all individuals.


also represents a single-factor model with equal loadings and equal intercepts. This is not a coincidence as I show in Box 2.2, where I describe how the random intercept model can be derived based on the concepts of LST-R theory. Figure 2.2 shows the model-implied trajectories of the trait scores for three hypothetical individuals. We can see that the model implies perfect stability of individuals’ trait scores over time. 

Although very restrictive, the random intercept model serves at least three useful purposes in longitudinal studies. First, it can be seen as a baseline “no change” model. If this model fits well, no further analyses of trait changes are needed (assuming sufficient statistical power for tests of model fit). In contrast, if this model is rejected based on tests of model fit, this may indicate that further analyses of change may be useful. Second, the model may be appropriate for social science constructs that show a high degree of stability (i.e., mean and covariance stability) across time and are not prone to situational influences (e.g., intelligence). Third, for such stable constructs, the model allows researchers to estimate the reliability (measurement precision) of the observed scores. 

# 2.2.3 Variance Decomposition and Reliability Coefficient

In the random intercept model, the variance of each measured variable can be decomposed additively because trait and error variables are uncorrelated: 

$$
V a r (Y _ {t}) = V a r (\xi) + \mathrm {V a r} (\varepsilon_ {t})
$$

A coefficient can then be defined that quantifies the proportion of reliable (systematic) variability in a measured variable (as opposed to unsystematic measurement error variance). This coefficient is known from CTT as the reliability coefficient $R e l ( Y _ { t } )$ . In the random intercept model, the $R e l ( Y _ { t } )$ coefficient is given by 

$$
\begin{array}{l} R e l (Y _ {t}) = V a r (\xi) / V a r (Y _ {t}) \\ = \operatorname {V a r} (\xi) / \left[ \operatorname {V a r} (\xi) + \operatorname {V a r} \left(\varepsilon_ {t}\right) \right] \\ = 1 - \left\{\operatorname {V a r} \left(\varepsilon_ {t}\right) / \left[ \operatorname {V a r} (\xi) + \operatorname {V a r} \left(\varepsilon_ {t}\right) \right] \right\} \\ \end{array}
$$

The interpretation of the $R e l ( Y _ { t } )$ coefficient parallels the interpretation in CTT. Ranging between 0 and 1, values of $R e l ( Y _ { t } )$ closer to 1 indicate higher reliability. For example, a value of $R e l ( Y _ { t } ) = . 8$ indicates that $8 0 \%$ of the observed score variability reflect individual differences in true trait scores and the remaining $2 0 \%$ reflect variability due to random measurement error. When the standardized solution (STDYX) is requested, Mplus prints the $R e l ( Y _ { t } )$ coefficient under R-SQUARE Observed variable in the output. 

# 2.2.4 Mplus Application

Below I present an Mplus application of the random intercept model to a hypothetical data set from $N = 3 0 0$ individuals who took an intelligence test on four measurement occasions. Individuals’ IQ scores at each time point are represented by four observed variables $Y _ { 1 }$ through $Y _ { 4 }$ in the Mplus analysis. The random intercept model can be specified in Mplus using the following MODEL statement (the complete Mplus input and output files along with the example data sets can be found on the companion website [see the box at the end of the table of contents]). 

```txt
MODEL: KSI by Y1-Y4@1;  
[Y1-Y4@0];  
[KSI*]; 
```

The first line of code specifies that a single factor (latent variable) labeled KSI is measured by all four $Y _ { t }$ variables. All four factor loadings are fixed to 1, as indicated by the @1 statement. The second line of code [Y1-Y4@0]; sets all four intercepts to zero. (Mplus would by default freely estimate a constant intercept for each measured variable Y .) Fixing all loadings to unity and all intercepts to zero is a consequence of Assumption 1 ( $\xi$ -equivalence) above. According to the $\xi .$ -equivalence assumption, all four time-specific trait factors $\xi _ { t }$ are identical. 

Therefore, there are no additive constants (fixed intercepts) in the measurement equation $Y _ { t } = \xi + \varepsilon _ { t }$ . In addition, no differences in scaling are assumed between different trait variables $\xi _ { t }$ and $\xi _ { { t ^ { \prime } } } ,$ so that the implicit multiplicative coefficient is 1.0: $\boldsymbol { \xi } _ { t } = 1 \cdot \boldsymbol { \xi } _ { t ^ { \prime } } = 1 \cdot \boldsymbol { \xi } .$ Therefore, all factor loadings must be fixed to 1 in this model. (Mplus by default estimates all factor loadings freely except for the first observed variable listed in the BY statement.) 

The mean of the trait factor KSI is estimated by stating the latent variable name in brackets in the third line of code: $\left[ \mathbb { K } \mathbb { S } \mathbb { T } ^ { \star } \right] .$ ;. The KSI factor variance as well as the four measurement error variances are estimated by default in Mplus and thus do not have to be mentioned explicitly in the MODEL statement. 

```txt
OUTPUT: SAMPSTAT STDYX; 
```

As for most analyses in Mplus, it is useful to request that the sample (descriptive) statistics (SAMPSTAT) as well as the completely standardized solution (STDYX) be printed in the output in addition to the default output. Among other information, the standardized solution STDYX provides the reliability estimates $R e l ( Y _ { t } )$ as I show below. 

Below are selected goodness-of-fit statistics (for a detailed description of these statistics, see Box 2.3) that Mplus computed for the random intercept model: 

```txt
MODEL FIT INFORMATION  
Chi-Square Test of Model Fit  
Value 5.347  
Degrees of Freedom 8  
P-Value 0.7199  
RMSEA (Root Mean Square Error Of Approximation)  
Estimate 0.000  
90 Percent C.I. 0.000 0.050  
Probability RMSEA >= .05 0.948  
CFI/TLI  
CFI 1.000  
TLI 1.001  
SRMR (Standardized Root Mean Square Residual)  
Value 0.052 
```

The model shows an appropriate fit according to all indices. This is indicated by the large $p$ -value associated with the chi-square test of model fit $( p =$ .7199) as well as RMSEA equal to zero, small SRMR (0.052), and CFI/TLI of 1. An excellent fit is expected here, given that the model was correctly specified for 

# BOX 2.3. Model Fit Assessment and Model Comparisons

One advantage of all models presented in this book is that they can be tested against the observed data and therefore potentially be falsified in empirical research. Model goodness- of-fit assessment in longitudinal confirmatory factor analysis (CFA) and structural equation modeling (SEM) follow general principles that are the same as those for other types of CFA and SEM approaches. The basic idea of model fit assessment in CFA or SEM is that a model can only be correct if the covariance and mean structure in the population match the model- implied covariance and mean structure. A chi- square test of model fit is frequently used to test the null hypothesis that the data structure in the population is identical to the model- implied data structure. This null hypothesis of exact model fit can be rejected when the chi- square test returns a small $p$ -value (e.g., $p \leq . 0 5 $ . In other words, a small $p$ -value can lead to model rejection. 

The null hypothesis tested with the chi- square test is rather strict, requiring an exact fit of a given model in the population. Some researchers (e.g., Bollen, 1989) therefore view the null hypothesis as unrealistic for most social science applications. This is because models by definition represent simplifications of reality and are thus not expected to show a perfect fit. To examine and quantify “approximate” model fit, a number of fit indices have been developed that are also frequently reported in the literature. The most commonly used indices include the root mean square error of approximation (RMSEA; Steiger & Lind, 1980), comparative fit index (CFI; Bentler, 1990), and standardized root mean square residual (SRMR; Bentler, 1995; Jöreskog & Sörbom, 1981). The simultaneous consideration of multiple indices has been recommended, where RMSEA values close to .06, CFI values close to .95, and SRMR values close to .08 may indicate adequate approximate model fit (Hu & Bentler, 1999). In addition, for a given data set, different models can be compared based on information criteria (IC) such as the Bayesian information criterion (BIC). In such comparisons, models with lower BIC values are preferred. A detailed discussion of model goodness- of-fit indices for confirmatory factor and structural equation models can be found in Bollen and Long (1993), Hu and Bentler (1999), as well as Schermelleh- Engel, Moosbrugger, and Müller (2003). 

simulated data drawn from a known population model. Next, Mplus provides the maximum likelihood estimated unstandardized and standardized parameter estimates for the random intercept model: 

<table><tr><td colspan="6">MODEL RESULTS</td></tr><tr><td></td><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-TailedP-Value</td></tr><tr><td>KSI</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y1</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y2</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y3</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y4</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Means</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>KSI</td><td></td><td>100.279</td><td>0.850</td><td>118.027</td><td>0.000</td></tr><tr><td>Intercepts</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y1</td><td></td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y2</td><td></td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y3</td><td></td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y4</td><td></td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Variances</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>KSI</td><td></td><td>210.102</td><td>17.689</td><td>11.878</td><td>0.000</td></tr><tr><td>Residual Variances</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y1</td><td></td><td>26.103</td><td>2.847</td><td>9.168</td><td>0.000</td></tr><tr><td>Y2</td><td></td><td>30.085</td><td>3.141</td><td>9.579</td><td>0.000</td></tr><tr><td>Y3</td><td></td><td>25.683</td><td>2.812</td><td>9.133</td><td>0.000</td></tr><tr><td>Y4</td><td></td><td>22.365</td><td>2.578</td><td>8.675</td><td>0.000</td></tr><tr><td colspan="6">STANDARDIZED MODEL RESULTS (STDYX Standardization)</td></tr><tr><td></td><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-TailedP-Value</td></tr><tr><td>KSI</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y1</td><td></td><td>0.943</td><td>0.007</td><td>131.911</td><td>0.000</td></tr><tr><td>Y2</td><td></td><td>0.935</td><td>0.008</td><td>119.133</td><td>0.000</td></tr><tr><td>Y3</td><td></td><td>0.944</td><td>0.007</td><td>131.637</td><td>0.000</td></tr><tr><td>Y4</td><td></td><td>0.951</td><td>0.007</td><td>144.281</td><td>0.000</td></tr><tr><td>Means</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>KSI</td><td></td><td>6.918</td><td>0.297</td><td>23.289</td><td>0.000</td></tr><tr><td>Intercepts</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y1</td><td></td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y2</td><td></td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y3</td><td></td><td>0.000</td><td>0.109</td><td>8.046</td><td>0.000</td></tr><tr><td>Y4</td><td></td><td>0.000</td><td>0.013</td><td>7.679</td><td>0.000</td></tr><tr><td>Variances</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>KSI</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Residual Variances</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y1</td><td></td><td>0.111</td><td>0.013</td><td>8.194</td><td>0.000</td></tr><tr><td>Y2</td><td></td><td>0.125</td><td>0.015</td><td>8.530</td><td>0.000</td></tr><tr><td>Y3</td><td></td><td>0.109</td><td>0.014</td><td>8.046</td><td>0.000</td></tr><tr><td>Y4</td><td></td><td>0.096</td><td>0.013</td><td>7.679</td><td>0.000</td></tr></table>

<table><tr><td colspan="5">R-SQUARE</td></tr><tr><td>Observed</td><td></td><td></td><td></td><td>Two-Tailed</td></tr><tr><td>Variable</td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>P-Value</td></tr><tr><td>Y1</td><td>0.889</td><td>0.013</td><td>65.956</td><td>0.000</td></tr><tr><td>Y2</td><td>0.875</td><td>0.015</td><td>59.567</td><td>0.000</td></tr><tr><td>Y3</td><td>0.891</td><td>0.014</td><td>65.819</td><td>0.000</td></tr><tr><td>Y4</td><td>0.904</td><td>0.013</td><td>72.141</td><td>0.000</td></tr></table>

The unstandardized solution provides the estimates of the latent trait factor mean (100.279) and variance (210.102), as well as the estimates of the four freely estimated measurement error variances (printed under RESIDUAL VARI-ANCES, values ranging between 22.365 and 30.085). In this example, the measurement error variances are fairly small compared to the trait factor variance, indicating high reliability (measurement precision). The degree of reliability of the measures becomes clearer from the estimates provided in the standardized solution. 

In the standardized solution, we obtain estimates of the standardized factor loadings (range: .935 through .951). Notice that even though we fixed all factor loadings to unity, the standardized factor loadings differ from one (and from each other). This is because we allowed the measurement error variances to differ across time. As a consequence, the observed variable variances are not restricted to be equal by the model. If we had constrained the measurement error variances to be time-invariant, we would have also obtained equal standardized loadings in this model. 

The standardized loadings in the example output indicate that the measures $Y _ { t }$ are strongly correlated with the trait factor $\xi$ (all loadings are $>$ .93). Again, this indicates the high reliability of the measurements. The reliability estimates $R e l ( Y _ { t } )$ themselves are given by the squared standardized loadings in this model and can be found under R-SQUARE in the Mplus output [range: .875 $\leq R e l ( Y _ { t } ) \leq . 9 0 4$ ]. The trait factor $\xi$ thus accounts for $\geq 8 7 . 5 \%$ of the variability in the observed variables $Y _ { t }$ in this example. This shows that there is not much room for additional situational or person $\times$ situation interaction effects, implying that the assumption of a strongly trait-like construct is plausible. (If there is any systematic situational variance in this example, it would be a very small amount and would be confounded with measurement error variance.) 

# 2.2.5 Summary

The random intercept model implies both strict covariance and strict mean stability at the latent level. Any changes in measured scores $Y _ { t }$ are solely attributed to measurement error in this model. Situation-specific fluctuations in the true 

scores are not allowed. In the sense of LST-R theory, the model implies that the construct under study is perfectly trait-like and stable over time. 

The random intercept model is a useful baseline model for longitudinal data, because it allows testing the simple hypothesis that there have not been any true changes in a construct across time. Given sufficient statistical power, a well-fitting random intercept model may indicate that further analyses of change are not needed and that the construct is a stable trait for the time period and population under study. In this case, no further models may need to be examined. The researcher can use the random intercept model to estimate the reliabilities of the indicators and, if desired, link the trait factor to other external variables to study relationships with other constructs. 

The random intercept model is overidentified and implies a testable restriction already when there are only two time points. In this case, the model allows testing whether the two observed means are equal in the population, that is, whether $E ( Y _ { 1 } ) = E ( Y _ { 2 } )$ . For three or more time points, the random intercept model allows testing whether all variables have equal covariances (in addition to having equal means). 

In many practical social science applications, the random intercept model does not fit as well as in our example, and/or the standardized factor loadings are a lot smaller than the ones obtained here, resulting in seemingly low reliabilities of the observed variables. If the model does not fit, this may be an indication that trait changes did occur (which the model does not allow). If the standardized loadings and reliabilities are weaker than one would expect (e.g., based on known or typical reliabilities for the given measure), this might indicate that the measurement error variances are overestimated due to the presence of systematic situation or person $\times$ situation interaction effects (which the model also ignores). If systematic situation or person $\times$ situation interaction effects are present in a measure, the random intercept model confounds these effects with measurement error, leading to an inflation of the measurement error variance estimates and an underestimation of the indicator reliabilities $\cdot R ^ { 2 }$ values). 

Despite this misspecification, the random intercept model may show a decent fit to the data. Hence, model fit alone does not tell the researcher whether the random intercept model is reasonable in a given application. The standardized loadings and reliabilities as well as other parameter estimates should also be considered. 

The next two models address the first limitation of the random intercept model (no trait changes permitted) to some degree. The trait–state–error model discussed in Section 3.4 as well as the multiple-indicator LST models described in Chapter 5 address the second limitation (no situation and interaction effects permitted). 

# 2.3 THE RANDOM AND FIXED INTERCEPTS MODEL

# 2.3.1 Introduction

The random intercept model implies that there are no mean changes across time. This is because the model estimates only one common mean parameter $E ( \xi )$ . The fixed intercepts (additive constants) of the observed variables $Y _ { t }$ are all set to zero, and their loadings are set to 1. Therefore, the model implies mean stability across time. This assumption can be relaxed by adding fixed intercept parameters to the random intercept model. I call the resulting model the random and fixed intercepts model, as it contains both a random intercept (trait) factor and fixed intercepts (additive constants ${ \bf \delta q } _ { t }$ ). 

# 2.3.2 Model Description

The random and fixed intercepts model is depicted in Figure 2.3. Notice that the random intercept factor $\xi _ { 1 }$ now has an index for Time $t = 1$ . This is because 

# BOX 2.4. Means of Linear Combinations

The mean structure plays an important role in most longitudinal structural equation models, as researchers are often interested in mean differences between measurement occasions. In the general so- called congeneric measurement model that is often used in longitudinal confirmatory factor models, an observed variable Y is connected to a latent variable, say $\eta$ by an additive constant (intercept α) and a multiplicative constant (factor loading $\lambda$ ): 

$$
Y = \alpha + \lambda \cdot \eta + \varepsilon
$$

where ε indicates a measurement error (residual) variable. The mean (or expectation) $E ( . )$ of Y in the congeneric measurement model is given by 

$$
E (Y) = \alpha + \lambda \cdot E (\eta)
$$

because the mean of a constant (α) is equal to the constant itself and ε as a measurement error variable has a mean of zero. Therefore, when $\lambda = 1$ (as in, e.g., the tau- equivalent and tau- parallel measurement models of classical test theory), the mean of Y is equal to the mean of $\eta$ plus a constant α. When $E ( \eta ) = 0$ (i.e., when the latent variable is mean centered), the mean of Y is equal to α. The latter case is the default in Mplus 8 for conventional confirmatory factor and structural equation models (latent variable means are set to zero, and observed variable intercepts are estimated as the default). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/2b8991812f936afbfdf72102f13f3f7cae030a0da5cad1fe0a2f295534a9f763.jpg)



FIGURE 2.3. Path diagram of the random and fixed intercepts model for a single observed variable $Y _ { t }$ that is measured on four time points. $\xi _ { 1 } =$ trait factor at Time 1; $\varepsilon _ { t } =$ measurement error variable; $\mathtt { d } _ { t } =$ constant (fixed) intercept coefficient.


I (arbitrarily) chose Time 1 as the reference time point to make comparisons to. The constant of 1 in the triangle in Figure 2.3 adds both a mean to the reference trait factor $\xi _ { 1 }$ and constant intercepts ${ \mathfrak { a } } _ { \mathrm { i } }$ to all $Y _ { t }$ variables except $Y _ { 1 }$ . For $Y _ { 1 }$ , the intercept ${ \mathfrak { a } } _ { 1 }$ remains fixed at zero. This makes $Y _ { 1 }$ a so-called reference indicator and allows us to identify the trait factor mean $E ( \xi _ { 1 } )$ as the mean at Time 1 (the reference time point). This can be seen by applying algebraic rules for means of linear combinations (see Box 2.4). The means of the remaining observed variables $Y _ { 2 }$ , $Y _ { 3 }$ , and $Y _ { 4 }$ can now be different from the mean of $Y _ { 1 }$ because $Y _ { 2 }$ , $Y _ { 3 }$ , and $Y _ { 4 }$ have additional additive constants ${ \bf \delta q } _ { t }$ . These constants reflect the mean differences relative to $Y _ { 1 }$ . The model can be described by the following measurement equation: 

$$
Y _ {t} = \pmb {\alpha} _ {t} + \pmb {\xi} _ {1} + \varepsilon_ {t}, \mathrm {w h e r e} \pmb {\alpha} _ {1} = 0
$$

The choice of the reference variable for which the intercept remains fixed at zero is arbitrary from a mathematical point of view (different choices of the reference variable lead to the same model-implied covariance and mean structure and result in the same model fit). However, some choices may lead to more readily interpretable results than others. The choice should be based on which mean comparisons are most interesting to the researcher. Often, it will be useful to make comparisons relative to Time 1, which is what I show in the example presented later in this section. 

In summary, the random and fixed intercepts model estimates the following parameters: 

•	 the trait factor mean $E ( \xi _ { 1 } )$ , 

•	 the trait factor variance $V a r ( \xi _ { 1 } )$ , 

• $n - 1$ intercept constants $\mathsf { a } _ { { \boldsymbol { t } } ^ { \prime } }$ $\mathbf { \Omega } _ { t } , t = 1 , \dots , n$ $t = 1$ , and 

•	 n measurement error variances $V a r ( \varepsilon _ { t } )$ , one for each for each time point $t = 1 , \ldots , n .$ . 

Therefore, the model in general has $2 \cdot n + 1$ free model parameters. In our example with four time points, we thus have $2 \cdot 4 + 1 = 9$ free parameters to estimate. Given that we have 14 pieces of available information (four $Y _ { t }$ variances, four $Y _ { t }$ means, and six unique $Y _ { t }$ covariances), the model has $1 4 - 9 = 5$ df. In Box 2.5, I explain how the random and fixed intercepts model can be defined based on the concepts of LST-R theory. 

Figure 2.4 illustrates the types of trait-change patterns that the random and fixed intercepts model permits. It can be seen that the model allows for true changes in the trait scores across time, but the amount of change has to be the same for all individuals. Such strictly homogeneous change would be expected, for example, if an intervention or other event had the exact same effect on all 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/ba9bfab7b8d9b7a664a05cfb31dcee521a28b403f7fdf2c01e0b6d52f95da5e8.jpg)



FIGURE 2.4. Illustration of possible model-implied trait-change patterns in the random and fixed intercepts model for three hypothetical individuals. It can be seen that the model implies equal amounts of changes in the trait scores for all individuals. In this example, there is no change between Time 1 and Time 2 (i.e., $\mathfrak { a } _ { 2 } = 0 .$ ).


# BOX 2.5. Defining the Random and Fixed Intercepts Model Based on LST‑R Theory

From the perspective of LST-R theory, the random and fixed intercepts model can be defined by making a slight modification to Assumption 1 made for the random intercept only model presented in Box 2.2: 

1. Essential $\xi$ -equivalence: Without loss of generality, let $\xi _ { 1 }$ be the reference trait variable. The latent trait variables $\xi _ { t }$ for all other time points $t > 1$ differ from $\xi _ { 1 }$ only by an additive constant, such that $\boldsymbol { \xi } _ { t } = \mathbf { a } _ { t } + \boldsymbol { \xi } _ { 1 }$ for all $t = 1 , \ldots , n$ $t = 1$ , where ${ \bf \delta q } _ { t }$ denotes a real constant and ${ \mathfrak { a } } _ { 1 } = 0$ . 

2. No situation or person $\times$ situation interaction influences: All latent state residual variables are zero, $\zeta _ { t } = \zeta _ { s } = 0$ for all t, $s = 1 , \ldots , n$ $s = 1$ . 

Instead of assuming strict equivalence of the traits for different time points, we now only assume essential equivalence. That is, the trait variables are now allowed to differ but only by an additive constant. This implies that, although the trait (and observed variable) means can differ between time points, individuals’ trait scores are still perfectly correlated across time. The second assumption is analogous to the assumption made in the random intercept model (see Box 2.2). 

Notice that here we do not need to make an assumption regarding the uncorrelatedness of the trait factor $\xi _ { 1 }$ and the error variables $\varepsilon _ { t } .$ . This is because we chose the trait at Time 1 to serve as a “common” trait factor. According to LST-R theory, a trait variable is by definition uncorrelated with all error variables that are measured at either the same or future time points (see Chapter 1, Box 1.2). Hence, $\xi _ { 1 }$ is by definition uncorrelated with all $\mathcal { E } _ { t }$ in this model. However, an assumption about uncorrelated trait and error variables would have to be made if a trait variable other than $\xi _ { 1 }$ were chosen as reference to prohibit correlations of the trait variable with prior error variables. 

Note that the random and fixed intercepts model is equivalent to the model of essential tau equivalence in CTT that is frequently used in cross- sectional psychometric analyses. The essential tau- equivalence model of CTT assumes that a set of observed variables measure the same construct, but that they can differ in their difficulty (means). 

participants or if developmental paths were strictly homogeneous across individuals. Like the random intercept model, the random and fixed intercepts model implies that no situation or person $\times$ situation interaction effects are relevant to the given construct or reflected in the measure. 

# 2.3.3 Variance Decomposition and Reliability Coefficient

The variance decomposition and reliability coefficient in the random and fixed intercepts model are analogous to the random intercept model: 

$$
\begin{array}{l} V a r (Y _ {t}) = V a r (\xi_ {1}) + V a r (\varepsilon_ {t}) \\ R e l (Y _ {t}) = \operatorname {V a r} (\xi_ {1}) / \operatorname {V a r} (Y _ {t}) \\ = \operatorname {V a r} \left(\xi_ {1}\right) / \left[ \operatorname {V a r} \left(\xi_ {1}\right) + \operatorname {V a r} \left(\varepsilon_ {t}\right) \right] \\ = 1 - \left. \left\{\operatorname {V a r} \left(\varepsilon_ {t}\right) / \left[ \operatorname {V a r} \left(\xi_ {1}\right) + \operatorname {V a r} \left(\varepsilon_ {t}\right) \right] \right\} \right. \\ \end{array}
$$

The reliability coefficient has the same meaning and interpretation as in CTT as well as in the random intercept model. 

# 2.3.4 Mplus Application

Below I discuss an illustrative application of the random and fixed intercepts model in Mplus. I again refer to a fictitious data set from $N = 3 0 0$ individuals whose IQ scores were recorded on four measurement occasions and are represented by observed variables $Y _ { 1 }$ through $Y _ { 4 }$ . The random and fixed intercepts model can be specified in Mplus using the following commands: 

```txt
MODEL: KSI1 by Y1-Y4@1; [Y1@0 Y2-Y4*]; [KSI1*]; 
```

It can be seen that the only difference in the model specification relative to the random-intercept-only model is in the second line of code, which now only sets the first intercept (of $Y _ { 1 ^ { \prime } }$ ) to zero and estimates the remaining three intercepts (of $Y _ { 2 }$ , $Y _ { 3 }$ , and $Y _ { 4 } )$ . 

I focus on the unstandardized parameter output for the random and fixed intercepts model because the main new feature of this model lies in the possibility of studying mean differences between time points through estimation of the constant intercept parameters $\mathsf { a } _ { t }$ . (The standardized loadings and reliability estimates that are provided as part of the STDYX output are interpreted in the 

same way as for the random intercept model described in Section 2.2.) The unstandardized output for the random and fixed intercepts model provides the estimates of the latent trait factor mean and variance, observed variable constant intercepts ${ \bf \mathfrak { a } } _ { t }$ , and estimates of the measurement error variances (RESIDUAL VARIANCES). 

<table><tr><td colspan="6">MODEL RESULTS</td></tr><tr><td></td><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-Tailed P-Value</td></tr><tr><td colspan="6">KSI1 BY</td></tr><tr><td>Y1</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y2</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y3</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y4</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td colspan="6">Means</td></tr><tr><td>KSI1</td><td></td><td>100.107</td><td>0.887</td><td>112.830</td><td>0.000</td></tr><tr><td colspan="6">Intercepts</td></tr><tr><td>Y1</td><td></td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y2</td><td></td><td>-0.669</td><td>0.432</td><td>-1.546</td><td>0.122</td></tr><tr><td>Y3</td><td></td><td>-2.904</td><td>0.415</td><td>-6.994</td><td>0.000</td></tr><tr><td>Y4</td><td></td><td>-4.735</td><td>0.402</td><td>-11.787</td><td>0.000</td></tr><tr><td colspan="6">Variances</td></tr><tr><td>KSI1</td><td></td><td>210.102</td><td>17.688</td><td>11.878</td><td>0.000</td></tr><tr><td colspan="6">Residual Variances</td></tr><tr><td>Y1</td><td></td><td>26.056</td><td>2.843</td><td>9.164</td><td>0.000</td></tr><tr><td>Y2</td><td></td><td>30.050</td><td>3.137</td><td>9.578</td><td>0.000</td></tr><tr><td>Y3</td><td></td><td>25.682</td><td>2.812</td><td>9.135</td><td>0.000</td></tr><tr><td>Y4</td><td></td><td>22.357</td><td>2.577</td><td>8.676</td><td>0.000</td></tr></table>

The mean of the trait factor (100.107) in this model represents the trait mean at Time 1. The intercepts ${ \bf \mathfrak { a } } _ { t }$ for $Y _ { 2 }$ , $Y _ { 3 }$ , and $Y _ { 4 }$ indicate the trait mean differences relative to the Time-1 trait mean. The intercept for $Y _ { 2 }$ is estimated to be $- 0 . 6 6 9$ , indicating a smaller mean at Time 2 relative to Time 1. However, this mean difference is not statistically significant at the .05 level as indicated by the standard error and z test for this parameter, $S E = 0 . 4 3 2$ , $z = - 1 . 5 4 6$ , $p = . 1 2 2$ . In other words, the null hypothesis of equal means between Times 1 and 2 cannot be rejected for alpha = .05. In contrast, the estimated intercept for $Y _ { 3 }$ (–2.904) is negative and statistically significantly different from zero $\mathit { S E } = 0 . 4 1 5$ , $\mathcal { Z } =$ $- 6 . 9 9 4$ , $p < . 0 0 1 ,$ ). This indicates that there was a decline in IQ means between Time 1 and Time 3. The Time-4 intercept (–4.735) is also statistically significant $\mathit { S E } = 0 . 4 0 2$ , $z = - 1 1 . 7 8 7$ , $p < . 0 0 1 $ ), indicating that the same trend continues (there is a further decline in average IQ scores beyond Time 3). Overall, from Time 1 to Time 4, each individual showed a “loss” of close to 5 IQ points in this hypothetical study.1 

# 2.3.5 Summary

The random and fixed intercepts model can be seen as an extension of the random intercept model. By allowing for an additive constant ${ \sf { a } } _ { t } .$ , the random and fixed intercepts model relaxes the assumption of no mean changes across time made in the random intercept model. It still assumes that there are no individual differences in trait change over time and no situation or person $\times$ situation interaction effects. 

The random and fixed intercepts model is just identified when there are only two time points. In this case, the model is saturated and does not contain testable restrictions. For three or more time points, the model becomes overidentified and allows testing whether the covariances between all $Y _ { t }$ variables are equal in the population. 

The random and fixed intercepts model implies that the same true trait score differences that are reflected in the constant intercept parameters ${ \bf \delta q } _ { { t } }$ apply to every individual. This does not seem very realistic for most longitudinal studies (including a population-based study on intelligence in which one would expect that some individuals’ IQ scores change more than others’ and/or that some individuals show no changes at all). Thus, the random and fixed intercepts model is appropriate only when a researcher hypothesizes that all individuals’ trait scores changed by the same amount. The next model addresses the issue of interindividual differences in intraindividual changes to some extent. 

# 2.4 THE $\xi$ ‑CONGENERIC MODEL

# 2.4.1 Introduction

Figure 2.4 illustrated the rather restrictive change process implied by the random and fixed intercepts model. According to the model, all individuals changed by the exact same amount. Any additional changes in the observed scores would represent measurement error. This is fairly unrealistic in practice. Individuals often differ in how much they change (i.e., there are true interindividual differences in intraindividual change). The random and fixed intercepts model does not permit a change process in which some individuals’ true scores change more than those of other individuals. In the single-factor approach, this limitation can be addressed to some extent by relaxing another implicit constraint made in the two previous models. In this section, I describe a single-factor model that I refer to as the $\xi .$ -congeneric model. The $\xi .$ -congeneric model freely estimates not only constant intercepts but also factor loadings. 

# 2.4.2 Model Description

The $\xi .$ -congeneric model is depicted in Figure 2.5. It can be seen that, in addition to estimating additive constants (intercepts) ${ \bf \delta q } _ { t } ,$ the model also permits $Y _ { 2 }$ , $Y _ { 3 }$ , and $Y _ { 4 }$ to have freely estimated multiplicative constants (factor loadings) $\lambda _ { { } _ { t } }$ . $Y _ { 1 }$ again serves as a reference indicator with ${ \mathfrak { a } } _ { 1 } = 0$ and $\lambda _ { \mathrm { 1 } } = 1$ . Therefore, the scale and mean of the trait factor $\xi _ { 1 }$ are identified via the reference indicator $Y _ { 1 }$ . As a consequence of estimating both intercepts and loadings for $Y _ { 2 }$ , $Y _ { 3 }$ , and $Y _ { 4 } .$ , individuals’ trait scores at Times 2, 3, and 4 can differ from their $\xi _ { 1 }$ score by both an additive constant $\mathbf { \Pi } ( \mathfrak { a } _ { t } )$ and a multiplicative constant $( \lambda _ { t } )$ : 

$$
\boldsymbol {\xi} _ {t} = \boldsymbol {\alpha} _ {t} + \boldsymbol {\lambda} _ {t} \cdot \boldsymbol {\xi} _ {1}
$$

It is again arbitrary from a mathematical point of view which time point we select to serve as reference point. Here, for consistency, we again select Time 1, making $Y _ { 1 }$ the reference indicator. The model is described by the following measurement equation: 

$$
Y _ {t} = \alpha_ {t} + \lambda_ {t} \cdot \xi_ {1} + \varepsilon_ {t}, \mathrm {w h e r e} \alpha_ {1} = 0 \mathrm {a n d} \lambda_ {1} = 1
$$

The $\xi .$ -congeneric model parallels the model of tau-congeneric variables in CTT (Jöreskog, 1971a). The tau-congeneric model of CTT assumes that a 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/eb99ec04220e73e4ec9146ce69e35153958b39850c745c05453623d643735cd8.jpg)



FIGURE 2.5. Path diagram of the $\xi$ -congeneric model for a single observed variable $Y _ { t }$ that is measured on four time points. $\xi _ { 1 } =$ trait factor at Time 1; $\varepsilon _ { t } =$ measurement error variable; $\mathbf { \boldsymbol { a } } _ { t } =$ constant (fixed) intercept coefficient; $\lambda _ { { \scriptscriptstyle t } } =$ constant factor loading (slope) coefficient.


set of observed variables measure the same construct, but that they can differ in their difficulty (means) as well as in their discrimination (slope) and/or in scaling (the units of measurement can differ between variables). Given its close relationship to the tau-congeneric CTT model, I refer to the model as the $\xi$ -congeneric model. 

In summary, the $\xi .$ -congeneric model estimates the following parameters: 

•	 the trait factor mean $E ( \xi _ { 1 } )$ , 

•	 the trait factor variance $V a r ( \xi _ { 1 } )$ , 

• $n - 1$ intercept constants ${ \bf \mathfrak { a } } _ { t }$ $\iota _ { t } , t = 1 , \ldots , n$ , 

• $n - 1$ multiplicative constants $\lambda _ { { _ t } }$ , $t = 1 , \ldots , n$ , and 

•	 n measurement error variances $V a r ( \varepsilon _ { t } )$ , one for each for each time point $t = 1$ $t = 1 , \ldots , n$ . 

Therefore, the model in general has $3 n$ free model parameters. In our example with four time points, we thus have $3 \cdot 4 = 1 2$ free parameters to estimate. Given that we have 14 pieces of available information (four $Y _ { t }$ variances, four $Y _ { t }$ means, and six unique $Y _ { t }$ covariances), the model has $1 4 - 1 2 = 2$ df. In Box 2.6, I explain how the $\xi .$ -congeneric model can be defined based on the concepts of LST-R theory. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/add2157ca8719b07daacb760f17f5394808ddfce6f8c552bc11f0ec0dd2749fb.jpg)



FIGURE 2.6. Illustration of possible model-implied trait-change patterns in the $\xi$ -congeneric model for three hypothetical individuals. It can be seen that, although the model allows for individual differences in the amount of trait change, individuals’ trait scores remain perfectly correlated across time. In this example, there is no change between Time 1 and Time 2 (i.e., ${ \mathfrak { a } } _ { 2 } = 0$ and $\lambda _ { 2 } = 1$ ).


Figure 2.6 illustrates the types of change patterns that the $\xi .$ -congeneric model permits. Not surprisingly, the $\xi .$ -congeneric model also allows for true changes (i.e., changes in the trait scores) across time. In addition, the change patterns are less restrictive than in the random and fixed intercepts model because of the freely estimated factor loadings. Now individuals are allowed to differ from one another also in how much their trait scores change. However, there is still an important restriction in the $\xi .$ -congeneric model with regard to interindividual differences in change across time. That is, the trait scores remain perfectly correlated across time so that the rank order of individuals remains constant over time. 

# BOX 2.6. Defining the $\xi$ Congeneric Model Based on LST Theory

Using LST-R theory, we can define the $\xi$ -congeneric model by assuming that the trait variables for different time points are positive linear functions of one another.* This can be referred to as the assumption of $\xi$ -congenericity: 

1. $\xi$ -congenericity: Without loss of generality, let $\xi _ { 1 }$ be the reference trait variable. The latent trait variables $\xi _ { t }$ for all other time points $t > 1$ are positive linear functions of the reference trait variable $\xi _ { 1 }$ , such that $\boldsymbol { \xi } _ { t } =$ $\mathbf { a } _ { t } + \boldsymbol { \lambda } _ { t } \cdot \boldsymbol { \xi } _ { 1 }$ for all $t = 1 , \ldots , n$ , where ${ \bf \mathfrak { a } } _ { t }$ and $\lambda _ { { } _ { t } }$ denote real constants, ${ \mathfrak { a } } _ { 1 }$ $= 0$ , $\lambda _ { \mathrm { 1 } } = 1$ , and $\lambda _ { { \scriptscriptstyle t } } > 0$ . 

2. No situation or person $\times$ situation interaction influences: All latent state residual variables are zero, $\zeta _ { t } = \zeta _ { s } = 0$ for all t $, s = 1 , \ldots , n$ $s = 1$ . 

The trait variables are now allowed to differ from $\xi _ { 1 }$ not only by an additive constant $\mathbf { \Pi } ( \mathfrak { a } _ { t } )$ as under the assumption of essential $\xi .$ -equivalence, but also by a multiplicative constant $( \lambda _ { t } )$ . Nonetheless, individuals’ trait scores are still perfectly correlated across time even under the weaker assumption of $\xi .$ -congenericity, because the trait variables at different time points are still perfectly linearly related according to Assumption 1. The second assumption is the same as in the two previously discussed models. 

Again, we do not need to make an assumption about uncorrelated $\xi _ { 1 }$ and $\varepsilon _ { t } ,$ because $\xi _ { 1 }$ is by definition uncorrelated with all $\mathcal { E } _ { t }$ according to LST-R theory. (Such an assumption would have to be made if a trait variable other than $\xi _ { 1 }$ were selected as a reference trait.) 

# 2.4.3 Variance Decomposition and Reliability Coefficient

The variance decomposition in the $\xi .$ -congeneric model is given by 

$$
V a r (Y _ {t}) = \lambda_ {t} ^ {2} \cdot V a r (\xi_ {1}) + V a r (\varepsilon_ {t})
$$

Notice that the multiplicative constant (factor loading) $\lambda _ { { _ t } }$ now has to be taken into account. The $\xi$ -congeneric model also allows estimating indicator reliability at each time point: 

$$
\begin{array}{l} R e l (Y _ {t}) = \lambda_ {t} ^ {2} \cdot V a r (\xi_ {1}) / V a r (Y _ {t}) \\ = \lambda_ {t} ^ {2} \cdot \operatorname {V a r} \left(\xi_ {1}\right) / \left[ \lambda_ {t} ^ {2} \cdot \operatorname {V a r} \left(\xi_ {1}\right) + \operatorname {V a r} \left(\varepsilon_ {t}\right) \right] \\ = 1 - \left. \left\{\operatorname {V a r} \left(\varepsilon_ {t}\right) / \left[ \lambda_ {t} ^ {2} \cdot \operatorname {V a r} \left(\xi_ {1}\right) + \operatorname {V a r} \left(\varepsilon_ {t}\right) \right] \right\} \right. \\ \end{array}
$$

The reliability coefficient $R e l ( Y _ { t } )$ again has the same meaning and interpretation as in previously discussed models. 

# 2.4.4 Mplus Application

Below I describe a hypothetical application of the $\xi$ -congeneric model to $N =$ 300 individuals who provided IQ data on four measurement occasions. The model can be specified in Mplus by using the following commands: 

```txt
MODEL: KSI1 by Y1@1 Y2-Y4*; [Y1@0 Y2-Y4*]; [KSI1*]; 
```

Notice that the loadings for $Y _ { 2 }$ , $Y _ { 3 }$ , and $Y _ { 4 }$ in the BY statement are no longer fixed to unity. The output for the $\xi .$ -congeneric model provides the estimates of the factor loadings for $Y _ { 2 }$ , $Y _ { 3 }$ , and $Y _ { 4 } ,$ , latent trait factor mean and variance, observed variable fixed intercepts, and estimates of the measurement error variances: 

```txt
MODEL RESULTS Estimate S.E. Est./S.E. Two-Tailed P-Value KSI1 BY Y1 1.000 0.000 999.000 999.000 Y2 1.517 0.041 37.389 0.000 Y3 1.965 0.049 40.214 0.000 Y4 2.679 0.063 42.245 0.000 
```

<table><tr><td colspan="5">Means</td></tr><tr><td>KSI1</td><td>100.107</td><td>0.870</td><td>115.034</td><td>0.000</td></tr><tr><td colspan="5">Intercepts</td></tr><tr><td>Y1</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y2</td><td>-46.318</td><td>4.102</td><td>-11.290</td><td>0.000</td></tr><tr><td>Y3</td><td>-91.251</td><td>4.939</td><td>-18.474</td><td>0.000</td></tr><tr><td>Y4</td><td>-162.264</td><td>6.410</td><td>-25.316</td><td>0.000</td></tr><tr><td colspan="5">Variances</td></tr><tr><td>KSI1</td><td>200.144</td><td>18.450</td><td>10.848</td><td>0.000</td></tr><tr><td colspan="5">Residual Variances</td></tr><tr><td>Y1</td><td>27.053</td><td>2.453</td><td>11.027</td><td>0.000</td></tr><tr><td>Y2</td><td>34.831</td><td>3.516</td><td>9.905</td><td>0.000</td></tr><tr><td>Y3</td><td>35.856</td><td>4.317</td><td>8.305</td><td>0.000</td></tr><tr><td>Y4</td><td>42.155</td><td>6.708</td><td>6.284</td><td>0.000</td></tr></table>

The mean of the trait factor again represents the mean at Time 1 (100.107). The intercepts for $Y _ { 2 }$ , $Y _ { 3 }$ , and $Y _ { 4 }$ were all estimated to be negative. The intercepts in this model no longer directly indicate the mean difference relative to the Time-1 mean because the factor loadings (multiplicative constants) now also have to be taken into account when calculating the means from the model parameters—unless all loadings are estimated to be exactly 1.0 (see Box 2.4). The estimated loadings for Times 2, 3, and 4 in this example are all larger than 1.0, so that the mean differences cannot be directly inferred from the intercepts. However, using the formulas presented in Box 2.4, we can compute the means for Times 2, 3, and 4 in Mplus using the MODEL CONSTRAINT option (see Box 2.7 on pages 40–41 for details). For this purpose, we change the MODEL statement for the $\xi .$ -congeneric model in the Mplus input file as follows: 

```txt
MODEL: KSI1 by Y1@1  
Y2* (12)  
Y3* (13)  
Y4* (14);  
[Y1@0];  
[Y2-Y4*] (a2-a4);  
[KSI1*] (E1);  
MODEL CONSTRAINT:  
NEW(E2 E3 E4);  
E2 = a2 + 12*E1;  
E3 = a3 + 13*E1;  
E4 = a4 + 14*E1;  
MODEL TEST:  
E1 = E2;  
E2 = E3;  
E3 = E4; 
```

# BOX 2.7. The MODEL CONSTRAINT and MODEL TEST Options in Mplus

The Mplus MODEL CONSTRAINT statement is a special feature of the MODEL command that is useful when one wants to constrain parameters in complex ways or compute model parameters that are not directly estimated by Mplus, but that are functions of other model parameters that are directly estimated. An example is the $\xi$ -congeneric model, in which a mean is estimated for the first trait variable $( \xi _ { 1 } )$ but not for the remaining trait variables $( \xi _ { 1 } , \xi _ { 2 }$ , and $\xi _ { 3 } )$ . The remaining trait means at Times 2, 3, and 4 are functions of the $\xi _ { 1 }$ mean as well as the relevant factor loadings $\lambda _ { { _ t } }$ and intercepts ${ \bf \delta q } _ { t }$ (see Box 2.4 and text). When using MODEL CONSTRAINT to define new parameters, each relevant parameter in the conventional MODEL statement has to be given a label or a number by using parentheses. For example: 

```txt
MODEL:  
KSI1 by Y1@1  
Y2 (l2);  
[Y2] (a2);  
[KSI1] (E1); 
```

In this example, l2 is the label chosen for the factor loading $\lambda _ { 2 }$ pertaining to $Y _ { 2 }$ ; a2 is the label chosen for the $Y _ { 2 }$ constant intercept ${ \mathfrak { a } } _ { 2 }$ ; and E1 is the label for the $\xi _ { 1 }$ trait factor mean $E ( \xi _ { 1 } )$ . These parameters can now be used in MODEL CONSTRAINT to define “new” parameters or to implement complex constraints on existing or new parameters. For example, we can compute the mean of $\boldsymbol { \xi } _ { 2 }$ as a new parameter: 

MODELCONSTRAINT: NEW(E2); $\mathrm{E2} = \mathrm{a2} + 12^{*}\mathrm{E1};$ 

Here, E2 is the new parameter to be defined that refers to the mean of $\boldsymbol { \xi } _ { 2 }$ . According to the rule discussed in Box 2.4, E2 is equal to the intercept ${ \mathfrak { a } } _ { 2 }$ (labeled a2) plus the loading $\lambda _ { 2 }$ (labeled l2) times the mean of $\xi _ { 1 }$ (labeled E1). Notice that the * symbol refers to multiplication within the MODEL CON-STRAINT option in Mplus. 

The MODEL TEST option can be used within the MODEL command to test specific constraints on parameters using a Wald test statistic. For example, it can be tested whether two means are equal: 

```txt
MODEL TEST: E1 = E2; 
```

Mplus then provides a Wald test statistic for the null hypothesis that the two means are equal in the population as part of the MODEL FIT INFORMA-TION section in the output file: 

```txt
Wald Test of Parameter Constraints  
Value 78.023  
Degrees of Freedom 1  
P-Value 0.0000 
```

In this example, the Wald test statistic is significant $( p < . 0 0 1 )$ , indicating that the null hypothesis of equality of means can be rejected for alpha $= . 0 5$ . 

Notice that in the modified input, I labeled all estimated loadings (l2, l3, l4), intercepts (a2, a3, a4), and the Time-1 trait factor mean (E1) by putting the chosen labels in parentheses () behind the relevant parameter. Using these labels, I implemented the equations presented in Box 2.4 for the calculation of the Time 2, 3, and 4 trait means in the MODEL CONSTRAINT option. To do so, I first listed these means in the NEW statement (labeled E2, E3, and E4) to indicate that they are to be defined as new parameters. Subsequently, I defined each parameter. For example, the Time-2 mean was defined as E2 = a2 + $1 2 ^ { \star } \mathbb { E } 1$ , where the * symbol refers to multiplication. 

Finally, the MODEL TEST option allows us to compute a Wald test of equality of means (see Box 2.7). This test can be conducted for just one pair of means or for a larger number of mean comparisons. In this case, I requested an omnibus Wald test of the null hypothesis that all four means are equal in the population. As a consequence of adding the new parameters through MODEL CONSTRAINT, we obtain the means as additional parameters in the unstandardized parameter estimate list (MODEL RESULTS section): 

```txt
MODEL RESULTS
...
New/Additional Parameters
E2 105.587 1.285 82.143 0.000
E3 105.468 1.642 64.236 0.000
E4 105.901 2.220 47.706 0.000 
```

It can be seen that the Time 2, 3, and 4 means are each higher by about 5 IQ points compared to the Time-1 mean (which was estimated to be 100.107). The Wald test indicates at least one significant mean difference $( p < . 0 0 1 )$ : 

```txt
MODEL FIT INFORMATION   
Wald Test of Parameter Constraints Value 99.494 Degrees of Freedom 3 P-Value 0.0000 
```

Notice that the Wald test in our example has three degrees of freedom, as it simultaneously assesses all four means for equality (similar to an omnibus $F$ statistic in analysis of variance). The means for Times 2, 3, and 4 do not appear to differ much from one another. Single degree of freedom Wald tests with appropriate corrections for alpha error inflation (e.g., Bonferroni) can be used to carry out post-hoc pairwise comparisons of means (e.g., of Time 1 vs. Time 2). 

The fact that the unstandardized factor loadings increased over time in this example indicates that there was an increase in the true trait score variability across time. That is, true interindividual differences in intelligence increased. This can be seen by computing the variances of the trait variables at Times 2, 3, and 4, which are a function of the loadings and the initial $( \xi _ { 1 } )$ trait variance in this model: 

$$
V a r \left(\xi_ {2}\right) = \lambda_ {2} ^ {2} \cdot V a r \left(\xi_ {1}\right) = 1. 5 1 7 ^ {2} \cdot 2 0 0. 1 4 4 = 4 6 0. 5 8 9
$$

$$
V a r (\xi_ {3}) = \lambda_ {3} ^ {2} \cdot V a r (\xi_ {1}) = 1. 9 6 5 ^ {2} \cdot 2 0 0. 1 4 4 = 7 7 2. 8 0 1
$$

$$
V a r \left(\xi_ {4}\right) = \lambda_ {4} ^ {2} \cdot V a r \left(\xi_ {1}\right) = 2. 6 7 9 ^ {2} \cdot 2 0 0. 1 4 4 = 1, 4 3 6. 4 4 2
$$

This increase in the variances corresponds to an increase in the corresponding standard deviations such that $S D ( \xi _ { 1 } ) = 1 4 . 1 5$ , $S D ( \xi _ { 2 } ) = 2 1 . 4 6$ , $S D ( \xi _ { 3 } ) =$ 27.80, and $S D ( \xi _ { 4 } ) = 3 7 . 9 0$ . This shows that some individuals’ trait scores showed a larger increase than others’, which would not have been permitted in the two previously discussed single-factor models. Nonetheless, even the $\xi .$ -congeneric model implies that individuals’ trait scores remain perfectly correlated across time (the rank order of individuals does not change), which is a fairly restrictive assumption in many social science applications. 

In the standardized solution (not shown here, but part of the materials available from the companion website [see the box at the end of the table of contents]), we can again inspect the standardized factor loadings, which tell us something about the reliabilities of the measurements as well as the extent to which our measurements really reflect a trait-like construct. In this example, all standardized loadings are again strong, indicating high reliabilities and showing that the construct is rather trait-like. 

# 2.4.5 Summary

Among the three single-factor measurement models discussed, the $\xi .$ -congeneric model is the most general one. It estimates the largest number of free parameters and requires three time points to be just identified (saturated) and four or more time points to be overidentified with testable restrictions. The previous two models can be seen as special cases of the $\xi .$ -congeneric model: the random intercept model results when $\mathbf { \boldsymbol { a } } _ { t } = 0$ and $\lambda _ { t } = 1$ for all $t = 1$ , . . . , n. The random and fixed intercepts model results when only $\lambda _ { { \scriptscriptstyle t } } = 1$ for all $t = 1$ , . . . , n. All three models imply that constructs are trait-like. For such constructs, each model allows estimating the reliability of the measured variables at each time point. 

In contrast to the two previously discussed single-factor measurement models, the $\xi .$ -congeneric model allows for interindividual differences in trait changes across time through the multiplicative parameter $\lambda _ { { \scriptscriptstyle t } }$ . However, the $\xi$ -congeneric model remains rather restrictive with regard to interindividual differences in change across time. The model still requires the trait scores to remain perfectly correlated across time, implying a constant rank order of individuals across time. 

# 2.5 CHAPTER SUMMARY

In this chapter, I discussed three simple longitudinal models and their application in Mplus. All models have in common that they (1) are based on just a single repeatedly measured variable and (2) use only a single latent factor. 

Single-factor models offer a simple way of testing basic hypotheses about change processes. The single-factor random intercept model can be viewed as a baseline model for longitudinal studies, as it implies strict stability (no changes beyond what can be explained by random measurement error). The random and fixed intercepts model allows for changes in trait scores, but implies that those changes are strictly consistent across individuals (all people change by the same amount). The $\xi .$ -congeneric model allows for individual differences in the amount of trait changes but still assumes that individuals’ trait scores maintain the same rank order across time. 

The single-factor approaches have the advantage that they are mathematically identified already when there are fewer than four time points. Specifically, the random intercept model as well as the random and fixed intercepts models require only two measurement occasions ${ \mathit { n } } = 2 { \mathit { \check { \Psi } } }$ ) to be identified. The random intercept model is overidentified with $d f = 1$ for $n = 2$ time points, whereas 

the random and fixed intercepts model is just identified (saturated; $d f = 0 ,$ ) for $n = 2$ . This means that the random intercept model already contains one testable restriction (the restriction of equal means across time) for a design with just two measurement occasions. The $\xi .$ -congeneric model requires three measurement occasions to be just identified $( d f = 0 )$ ) and four or more measurement occasions to be overidentified with $d f > 0$ . 

All three single-factor models have some important limitations. As mentioned above, the change processes implied by the models may be too restrictive for many empirical phenomena. Furthermore, the definitions of the models based on LST theory showed that each of the models implies a strict trait-like nature of the construct under study. In other words, no situational influences or person $\times$ situation interactions are allowed in the models. As a consequence, the models cannot be used to examine the degree to which measures may reflect situation and/or person $\times$ situation interaction influences, and they tend to underestimate the reliabilities of less than perfectly trait-like measures. 

In the next chapter, I discuss models for single-indicator data that contain more than one latent variable. Models with multiple latent variables address some of the limitations of single-factor models. In particular, they allow for more flexibility in the modeling of individual differences in changes over time. Moreover, some multifactor models also allow for a separation of trait, state, and measurement error influences. 

# 2.6 RECOMMENDED READING

Duncan, T., Duncan, S., & Strycker, L. (2006). An introduction to latent variable growth curve modeling: Concepts, issues, and applications (2nd ed.). Mahwah, NJ: Erl‑ baum. 

# NOTE

1. In addition to tests of statistical significance, researchers should also consider measures of effect size (e.g., Kline, 2020). This is because $p$ -values in tests of significance are heavily influenced by sample size and contain no information about the practical significance of a given effect. In the hypothetical example, depending on the time interval, a raw mean difference of close to 5 IQ points over the course of a study may be seen as a rather large effect. 

# 3

# Multifactor Longitudinal Models for Single‑Indicator Data

# 3.1 INTRODUCTION

In Chapter 2, I discussed three longitudinal models for single-indicator data. Each of these models used only a single latent factor to account for the observed covariance and mean structure. As a consequence, these models were fairly restrictive with regard to their assumptions about the strictly trait-like nature of constructs and the model-implied change processes. More flexible models are obtained by introducing more than one latent factor. In this chapter, I present various models for single-indicator data that use more than one latent factor. I begin with the so-called simplex model. 

# 3.2 THE SIMPLEX MODEL

# 3.2.1 Introduction

All single-factor models described in Chapter 2 make fairly restrictive assumptions about changes over time in that they imply perfectly correlated trait variables over time. Thus, these models cannot properly represent typically occurring change patterns in the social sciences in which the rank order of individuals changes across time. The simplex model (Guttman, 1954; Jöreskog, 1970, 1979a, 1979b; see Figure 3.1) is a multifactor longitudinal model that permits rank-order changes in the true scores across time for single-indicator data. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/679f220d7399086a01e8081f9449f377cd1850122864a403af507b350e3576ed.jpg)



FIGURE 3.1. Path diagram of the simplex model for a single observed variable $Y _ { t }$ that is measured on four time points. $\tau _ { t } =$ latent state variable; $\varepsilon _ { t } =$ measurement error variable; $\boldsymbol { \beta } _ { 0 t } =$ constant regression intercept coefficient; $\beta _ { 1 t } =$ constant autoregressive slope coefficient; $\zeta _ { t } =$ latent residual variable. Parameter restrictions necessary for model identification are discussed in the text.


# 3.2.2 Model Description

In the simplex model, a latent state variable $\tau _ { t }$ is specified at each time point in addition to a measurement error variable $\varepsilon _ { t } .$ . Adjacent latent state variables are connected through bivariate linear regressions. These regression paths are frequently referred to as first-order autoregressive effects because they represent regressions of a variable on itself at the immediately preceding measurement occasion. The autoregressive path coefficients $\beta _ { 1 t }$ are latent regression slope coefficients that measure the expected increase or decrease in $\tau _ { t }$ for a one-unit change in $\tau _ { t - 1 }$ . 

The simplex model can be described by the following measurement and structural (latent variable) equations: 

Measurement equation: $Y _ { t } = \tau _ { t } + \varepsilon _ { t }$ for t = 1, . . . , n 

Structural equation: $\tau _ { t } = \mathsf { \beta } _ { 0 t } + \mathsf { \beta } _ { 1 t } \cdot \tau _ { t - 1 } + \zeta _ { t }$ for t = 2, . . . , n 

The measurement equation is identical to the basic decomposition of observed variables in latent strait–trait (LST) theory that I discussed in Chapter 

1 (except that here I omitted the index i for the measure, given that the simplex model considers only one measure at each time point). The structural equation describes a first-order autoregressive process on the level of the latent state variables $\tau _ { t }$ . It can be seen that for $t \geq 2$ , all latent state variables $\tau _ { t }$ are regressed on the latent state variable $\tau _ { t - 1 }$ from the immediately preceding time point. In the structural equation, $\beta _ { 0 t }$ indicates a constant latent intercept, $\beta _ { 1 t }$ is a constant latent path (regression slope) coefficient, and $\zeta _ { t }$ denotes the latent state residual variable that pertains to Time t. The state residual variable $\zeta _ { t }$ by definition has a mean of zero that is uncorrelated with the regressor $\tau _ { t - 1 }$ . In Box 3.1, I explain in detail how the simplex model can be defined based on the concepts of revised LST theory (LST-R theory) and why the latent regression residual variables $\zeta _ { t }$ are identical to the latent state residual variables in LST-R theory. 

To be identified, the simplex model requires at least four time points. Moreover, the model requires that either the error variances $V a r ( \varepsilon _ { t } )$ or the state residual variances $V a r ( \zeta )$ be set equal across time.1 In addition, for the model to be identified, the autoregressive coefficients $\beta _ { 1 t }$ have to be different from zero.2 

Assuming that all latent state residual variances $V a r ( \zeta )$ [but not the measurement error variances $V a r ( \varepsilon _ { t } ) ]$ are set equal across time, we obtain $V a r ( \zeta _ { t } ) =$ $V a r ( \zeta _ { s } ) = V a r ( \zeta )$ for all time points t, $s = 2$ , . . . , n. Under this assumption, the simplex model includes the following parameters: 

•	 the state factor mean $E ( \tau _ { 1 } )$ at Time 1, 

•	 the state factor variance $V a r ( \tau _ { 1 } )$ at Time 1, 

•	 one state residual factor variance Var $( \zeta )$ for all t, $s = 2 , \ldots , n .$ 

• $n - 1$ latent intercept constants $\beta _ { 0 t } ,$ 

• $n - 1$ latent path (regression slope) constants $\beta _ { \mathrm { 1 } t } ,$ and 

•	 n measurement error variances $V a r ( \varepsilon _ { t } )$ , one for each time point $t = 1 , \ldots .$ , n. 

Therefore, the model with equal state residual factor variances and freely estimated measurement error variances has $3 n + 1$ free model parameters, where n again indicates the total number of measurement occasions. In our example with four time points, we thus have $3 \cdot 4 + 1 = 1 3$ free parameters to estimate. Given that we have 14 pieces of available information (four $Y _ { t }$ variances, four $Y _ { t }$ means, and six unique $Y _ { t }$ covariances), the model has $1 4 - 1 3 = 1$ df. 

If a researcher instead chooses to set the measurement error variances $V a r ( \varepsilon _ { t } )$ equal across time and to freely estimate all state residual factor variances 

# BOX 3.1. Defining the Simplex Model Based on LST‑R Theory

According to LST-R theory, each measured variable can be decomposed into trait, state residual, and measurement error components (see Chapter 1): 

$$
\begin{array}{l} Y _ {t} = \tau_ {t} + \varepsilon_ {t} \\ = \xi_ {t} + \zeta_ {t} + \varepsilon_ {t} \text {f o r a l l} t = 1, \dots , n \\ \end{array}
$$

In LST-R theory, by definition, latent state residual variables are uncorrelated with trait variables that are measured at the same time point, that is, $C o v ( \zeta _ { t } , \xi _ { t } ) = 0$ for all $t = 1$ , . . . , n (compare Chapter 1, Box 1.2). However, LST-R theory allows for the possibility that state residual latent variables influence future traits; that is, the covariances $C o v ( \zeta _ { t } , \xi _ { s } )$ are not necessarily zero for $t =$ 1, . . . , s, . . . , n and $t < s$ . From a substantive perspective, this is in line with a dynamic trait concept, which assumes that current situations and/or person $\times$ situation interactions may influence future trait scores in addition to the influence of previous traits (see Chapter 1 for a more detailed discussion of this issue). 

The simplex model can be formulated within LST-R theory by applying this dynamic trait concept. I begin with the basic LST-R decomposition of a state variable $\tau _ { t }$ into trait $\xi _ { t }$ plus state residual $\zeta _ { t }$ (see Chapter 1): 

$$
\tau_ {t} = \xi_ {t} + \zeta_ {t}
$$

This decomposition holds for all time points $t = 1$ , . . . , n. 

The simplex model implies that for $t \geq 2$ , the trait variables $\xi _ { { t } }$ are also decomposed. Specifically, for $t \geq 2$ , the trait variables are assumed to be linear functions of (1) the immediately preceding trait variable $\xi _ { ( t - 1 ) }$ and (2) the immediately preceding state residual variable $\zeta _ { ( t - 1 ) }$ such that 

$$
\xi_ {t} = \beta_ {0 t} + \beta_ {1 t} \cdot \xi_ {(t - 1)} + \beta_ {1 t} \cdot \zeta_ {(t - 1)} \text {f o r a l l} t = 2, \dots , n
$$

where $\beta _ { 0 t }$ and $\beta _ { 1 t }$ denote real constants and $\beta _ { 1 t } \neq 0$ 

Notice that the multiplicative constant $\beta _ { 1 t }$ is the same for both $\xi _ { ( t - 1 ) }$ and $\zeta _ { ( t - 1 ) }$ . The simplex model thus implies that the influence of the previous trait is equally large as the influence of the previous state residual. Further, notice that unlike the unrestrictive basic LST-R decomposition $[ \tau _ { t } = \xi _ { t } + \zeta _ { t } ]$ , the decomposition of the trait variables $\xi _ { t }$ in the simplex model represents a restrictive assumption (namely, that subsequent traits are perfectly determined by a linear function of the immediately preceding traits and state residuals). 

To illustrate the implicit decomposition of trait variables in the simplex 

model, consider Time 2, for which we obtain the following decomposition of the trait variable: 

$$
\xi_ {2} = \beta_ {0 2} + \beta_ {1 2} \cdot \xi_ {1} + \beta_ {1 2} \cdot \zeta_ {1}
$$

By replacing $\boldsymbol { \xi } _ { 2 }$ with $\beta _ { 0 2 } + \beta _ { 1 2 } \cdot \zeta _ { 1 } + \beta _ { 1 2 } \cdot \zeta _ { 1 }$ in the basic LST-R equation for $\tau _ { 2 }$ , we obtain 

$$
\begin{array}{l} \tau_ {2} = \zeta_ {2} + \zeta_ {2} \\ = \beta_ {0 2} + \beta_ {1 2} \cdot \xi_ {1} + \beta_ {1 2} \cdot \zeta_ {1} + \zeta_ {2} \\ = \beta_ {0 2} + \beta_ {1 2} \cdot (\xi_ {1} + \zeta_ {1}) + \zeta_ {2} \\ = \beta_ {0 2} + \beta_ {1 2} \cdot \tau_ {1} + \zeta_ {2} \\ \end{array}
$$

For Time 3, we obtain the following equations: 

$$
\xi_ {3} = \beta_ {0 3} + \beta_ {1 3} \cdot \xi_ {2} + \beta_ {1 3} \cdot \zeta_ {2}
$$

such that 

$$
\begin{array}{l} \tau_ {3} = \zeta_ {3} + \zeta_ {3} \\ = \beta_ {0 3} + \beta_ {1 3} \cdot \xi_ {2} + \beta_ {1 3} \cdot \zeta_ {2} + \zeta_ {3} \\ = \beta_ {0 3} + \beta_ {1 3} \cdot (\zeta_ {2} + \zeta_ {2}) + \zeta_ {3} \\ = \beta_ {0 3} + \beta_ {1 3} \cdot \tau_ {2} + \zeta_ {3} \\ \end{array}
$$

The equations for subsequent time points are analogous. 

The above derivations show a number of interesting features of the simplex model. First, it becomes clear that the simplex regression residual variables $\zeta _ { t }$ are equal to the state residual variables as defined in LST-R theory. Therefore, these variables have a clear meaning and interpretation. They represent situation and/or person $\times$ situation interaction effects on a given time point t. That is, the state residual variables $\zeta _ { t }$ represent influences that are unique to a given time point and that cannot be explained by previous trait influences or previous situational and/or person $\times$ situation interaction influences pertaining to the same construct. 

The second interesting feature of the simplex model is that it is in line with the fundamental idea of LST-R theory, according to which traits are dynamic and can be influenced by previous situations and experiences. In concordance with this idea, the simplex model allows for an influence of both previous trait variables and previous state residual variables on individuals’ present and future trait scores. Conceptually, this makes sense for many social science phenomena: 

Individuals remain to some extent stable over time (there is an ongoing “trait” influence), but individuals also respond to events and experiences that they encounter and those experiences may alter their subsequent trait scores (i.e., situations may change a person). Even the trait scores at Time 1 have an (indirect) influence on all subsequent trait scores $\xi _ { t }$ (for $t > 2 )$ ) in the model, as can be shown, for example, for the Time-3 trait variable: 

$$
\begin{array}{l} \xi_ {3} = \beta_ {0 3} + \beta_ {1 3} \cdot \xi_ {2} + \beta_ {1 3} \cdot \zeta_ {2} \\ = \beta_ {0 3} + \beta_ {1 3} \cdot \left(\beta_ {0 2} + \beta_ {1 2} \cdot \xi_ {1} + \beta_ {1 2} \cdot \zeta_ {1}\right) + \beta_ {1 3} \cdot \zeta_ {2} \\ = \beta_ {0 3} + \beta_ {1 3} \cdot \beta_ {0 2} + \beta_ {1 3} \cdot \beta_ {1 2} \cdot \xi_ {1} + \beta_ {1 3} \cdot \beta_ {1 2} \cdot \zeta_ {1} + \beta_ {1 3} \cdot \zeta_ {2} \\ \end{array}
$$

It can be seen that the Time-3 trait $( \xi _ { 3 } )$ is in part a function of the Time-1 trait $( \xi _ { 1 } )$ , where the product $\beta _ { 1 3 } \cdot \beta _ { 1 2 }$ quantifies the indirect effect of $\xi _ { 1 }$ on $\xi _ { 3 }$ . Moreover, both previous situations and/or person $\times$ situation interactions (as represented by $\zeta _ { 1 }$ and $\zeta _ { 2 }$ ) have a (direct or indirect) influence on $\xi _ { 3 }$ . The (indirect) effect of $\zeta _ { 1 }$ again equals the product ${ \beta } _ { 1 3 } \cdot { \beta } _ { 1 2 }$ , whereas the (direct) effect of $\zeta _ { 2 }$ equals $\beta _ { 1 3 }$ . In Box 3.5, I discuss the estimation of direct and indirect (“mediated”) effects in the simplex model in more detail. 

Notice that we do not have to make additional assumptions regarding the linear independence of latent and measurement error variables in the simplex model because, according to LST-R theory, $C o v ( \varepsilon _ { t } , \zeta _ { s } ) = 0$ generally and $C o v ( \varepsilon _ { t } ,$ $\tau _ { s } ) = 0$ for $s \leq t$ (see Chapter 1, Box 1.2). 

$V a r ( \zeta )$ , we obtain $V a r ( \varepsilon _ { t } ) = V a r ( \varepsilon _ { s } ) = V a r ( \varepsilon )$ for all time points t, $s = 1$ , . . . , n. Under this condition, the following parameters are estimated: 

•	 the state factor mean $E ( \tau _ { 1 } )$ at Time 1, 

•	 the state factor variance $V a r ( \tau _ { 1 } )$ at Time 1, 

• $n - 1$ state residual factor variances Var $( \zeta _ { t } )$ , 

• $n - 1$ latent intercept constants $\beta _ { 0 t } .$ 

• $n - 1$ latent path (regression slope) constants $\beta _ { \mathrm { 1 } t } ,$ and 

•	 one measurement error variance Var(ε) for all $t = 1$ $t = 1 , \ldots , n .$ 

The simplex model version with equal measurement error variances and free state residual factor variances thus has only 3n free model parameters, whereas the previous model version with equal state residual factor variances had $3 n + 1$ parameters. This is because there are only $n - 1$ potential state residual variance parameters in the simplex model but n measurement error 

# BOX 3.2. Should a Researcher Constrain State Residual or Measurement Error Variances in the Simplex Model?

From a substantive perspective, both assumptions (equal state residual variances vs. equal measurement error variances) could be violated in empirical applications. For example, the proportion of state variability that can be explained by the previous state could change across time, for example, due to a construct becoming increasingly stable across time. Or the amount of state residual variance may differ due to different time intervals between measurement occasions. If a researcher expects a shift in the amount of explained state factor variance theoretically, based on prior research, or due to unequally spaced time points, he or she should avoid setting the state residual factor variances equal across time as this may cause bias in other parameter estimates. In contrast, if researchers are expecting changes in the amount of measurement error variance (unreliability) of their measures (e.g., due to a Socratic effect), then they should avoid constraining the measurement error variances to be equal across time. 

What if a researcher has to expect both changes in the amount of state residual factor variance (situational influences) and measurement error variance (unreliability)? This scenario is not at all implausible in empirical research. The simplex model does not offer an easy solution to this problem due to its fairly tight identification constraints. An extension of the simplex model that uses multiple indicators per measurement occasion (discussed in Chapter 5 in this volume) addresses this limitation (among others). 

variances. Therefore, setting all measurement error variances equal saves one additional parameter. 

In our four-wave example, the simplex model with free state residual variances and equal measurement error variances has 12 parameters and $1 4 - 1 2 =$ 2 df. In Box 3.2, I provide some guidelines on how to choose between the two model versions with equal state residual factor variances versus equal measurement error variances. 

# 3.2.3 Variance Decomposition and Coefficients

In the simplex model, the variances of the measured and latent state variables can be decomposed as follows: 

$$
V a r \left(Y _ {t}\right) = V a r \left(\tau_ {t}\right) + V a r \left(\varepsilon_ {t}\right)
$$

$$
V a r \left(\tau_ {t}\right) = \beta_ {1 t} ^ {2} \cdot V a r \left(\tau_ {t - 1}\right) + V a r \left(\zeta_ {t}\right) \text {f o r} t \geq 2
$$

In analogy to the previously discussed single-factor models, the simplex model allows researchers to estimate the reliability $R e l ( Y _ { t } )$ of the observed scores at each time point by computing the ratio of systematic variance to total observed variance: 

$$
\begin{array}{l} R e l \left(Y _ {t}\right) = V a r \left(\tau_ {t}\right) / V a r \left(Y _ {t}\right) \\ = \operatorname {V a r} \left(\tau_ {t}\right) / \left[ \operatorname {V a r} \left(\tau_ {t}\right) + \operatorname {V a r} \left(\varepsilon_ {t}\right) \right] \\ = 1 - \left\{\operatorname {V a r} \left(\varepsilon_ {t}\right) / \left[ \operatorname {V a r} \left(\tau_ {t}\right) + \operatorname {V a r} \left(\varepsilon_ {t}\right) \right] \right\} \\ \end{array}
$$

The reliability coefficient $R e l ( Y _ { t } )$ has the same meaning and interpretation as in the previously discussed models. When the standardized solution (STDYX) is requested, Mplus prints the $R e l ( Y _ { t } )$ coefficient under R-SQUARE Observed variable in the output. 

In contrast to the single-factor models, the simplex model allows us to define two additional coefficients for quantifying stability and variability across time. For $t \geq 2$ , the consistency coefficient $C o n ( \tau _ { t } )$ is defined as follows: 

$$
\begin{array}{l} C o n \left(\boldsymbol {\tau} _ {t}\right) = \beta_ {1 t} ^ {2} \cdot \operatorname {V a r} \left(\boldsymbol {\tau} _ {t - 1}\right) / \operatorname {V a r} \left(\boldsymbol {\tau} _ {t}\right) \\ = \beta_ {1 t} ^ {2} \cdot \operatorname {V a r} \left(\tau_ {t - 1}\right) / \left[ \beta_ {1 t} ^ {2} \cdot \operatorname {V a r} \left(\tau_ {t - 1}\right) + \operatorname {V a r} \left(\zeta_ {t}\right) \right] \\ = 1 - \left. \left. \operatorname {V a r} \left(\zeta_ {t}\right) / \left[ \beta_ {l t} ^ {2} \cdot \operatorname {V a r} \left(\tau_ {t - 1}\right) + \operatorname {V a r} \left(\zeta_ {t}\right) \right] \right\} \right. \\ \end{array}
$$

$C o n ( \tau _ { t } )$ ranges between 0 and 1 and indicates the proportion of variability in latent state scores that is due to previous trait and/or state residual influences. For example, a value of $C o n ( \tau _ { t } ) = . 8$ means that $8 0 \%$ of the variability in $\tau _ { t }$ scores is due to previous trait, situational, and/or person $\times$ situation interaction influences. The $C o n ( \tau _ { t } )$ coefficient thus indicates the degree of stability in state scores across time. When the standardized solution (STDYX) is requested, Mplus prints the $C o n ( \tau _ { t } )$ coefficient under R-SQUARE Latent variable in the output. 

The occasion-specificity coefficient $O s p ( \tau _ { t } )$ indicates the proportion of variability in the latent state scores that is due to situation and/or person $\times$ situation interaction effects at Time t and is defined for $t \geq 2$ as follows: 

$$
\begin{array}{l} O s p \left(\tau_ {t}\right) = V a r \left(\zeta_ {t}\right) / V a r \left(\tau_ {t}\right) \\ = \operatorname {V a r} \left(\zeta_ {t}\right) / \left[ \beta_ {1 t} ^ {2} \cdot \operatorname {V a r} \left(\tau_ {t - 1}\right) + \operatorname {V a r} \left(\zeta_ {t}\right) \right] \\ = 1 - \operatorname {C o n} (\tau_ {t}) \\ \end{array}
$$

For example, a value of $O s p ( \tau _ { t } ) = . 2$ means that $2 0 \%$ of the variability in $\tau _ { t }$ scores is due to situational and/or person $\times$ situation interaction influences at Time t 

rather than previous trait or previous situational and/or previous person $\times$ situation interaction influences. The $O s p ( \tau _ { t } )$ coefficient thus indicates the degree of variability in state scores across time. In the Mplus standardized (STDYX) solution for the simplex model, the $O s p ( \tau _ { t } )$ coefficient is given as the standardized residual variance for $\tau _ { t }$ under Residual Variances. 

Notice that the simplex model does not allow separating previous trait $( \xi )$ from previous state residual $( \zeta )$ influences. In Section 3.4 as well as in Chapter 5, I discuss models that allow disentangling these components. 

# 3.2.4 Assessing Stability and Change in the Simplex Model

The simplex model is intuitively appealing because it reflects the idea that previous behavior is often the best predictor of subsequent behavior. At the same time, latent state scores do not have to be perfectly correlated across time. Therefore, the model allows the possibility that some individuals change more than others and/or that changes occur in different directions (some individuals show increases, whereas others show decreases in their scores). The model is thus less restrictive than the previously described single-factor models. 

The simplex model allows examining the stability and change in behavior at both the mean and covariance level. To illustrate how stability and change are represented in the model, it is useful to consider several extreme situations. For example, perfect mean and covariance stability would be indicated in the model if simultaneously $\beta _ { 0 t } = 0$ , $\boldsymbol { \beta } _ { 1 t } = 1$ , and $V a r ( \zeta _ { t } ) = 0$ . In this case, $\tau _ { t }$ and $\tau _ { t - 1 }$ are identical—individuals’ true scores remained perfectly stable between the two time points. If this is the case for all time points, then the model reduces to the random intercept model described in Section 2.2 in Chapter 2. One could then claim that a construct is perfectly stable across time, that is, perfectly “trait-like.” 

Another special case occurs when $\boldsymbol { \beta } _ { 1 t } = 1$ and $V a r ( \zeta _ { t } ) = 0$ , but $\beta _ { 0 t } \neq 0$ . In this case, all individuals changed by the same amount $( \boldsymbol { \beta } _ { 0 t } )$ between two adjacent time points. This case reflects perfect covariance stability but no mean stability between two adjacent time points. If this occurs for all time points, then the model is equivalent to the random and fixed intercepts model described in Section 2.3 in Chapter 2, with the $\beta _ { 0 t }$ parameters reflecting the fixed intercepts. When $V a r ( \zeta _ { t } ) = 0$ , but $\boldsymbol { \beta } _ { 0 t } \neq 0$ and $\boldsymbol { \beta } _ { 1 t } \neq 1$ for all time points, the model is equivalent to the $\xi .$ -congeneric model described in Section 2.4. These scenarios illustrate that the single-factor models described in Chapter 2, Sections 2.2–2.4 can be viewed as special cases of the simplex model. 

Another interesting special case in the simplex model is seen when $\boldsymbol { \beta } _ { 1 t } =$ 1 and $V a r ( \zeta _ { t } ) > 0$ . In this case, there is less than perfect covariance stability between Time $t$ and Time $t - 1$ (because the residual variance is not zero). Given 

# BOX 3.3. Endogenous versus Exogenous Variables in Structural Equation Models and Mplus

In structural equation models, a distinction is made between endogenous and exogenous variables. Endogenous variables are dependent variables. They appear on the left-hand side of a measurement or structural (regression) equation. Exogenous variables only appear on the right-hand side of regression equations. That is, exogenous variables serve as explanatory variables only. As an example, consider the structural equation for the latent state variable at the second measurement occasion $( t = 2 )$ ) in the simplex model: 

$$
\tau_ {2} = \beta_ {0 2} + \beta_ {1 2} \cdot \tau_ {1} + \zeta_ {2}
$$

In this equation, the state variable $\tau _ { 2 }$ is an endogenous variable because it appears on the left-hand side of the equation and is predicted by $\tau _ { 1 }$ . $\tau _ { 1 }$ is the only exogenous state variable in the entire model, as it is not explained by any other state variable in the model $\stackrel { \prime } { \tau _ { 1 } }$ never appears on the left-hand side of a structural equation unless covariates are added to the model to predict $\tau _ { 1 ^ { \prime } }$ ). Other exogenous variables in the simplex model are the residuals $\mathcal { E } _ { t }$ and $\zeta _ { t }$ . The observed variables $Y _ { t }$ are endogenous because they appear on the left-hand side of the measurement equation $Y _ { t } = \tau _ { t } + \varepsilon _ { t }$ . 

Endogenous variables have intercepts, regression slope coefficients, residual variances, and potentially residual covariances as associated model parameters. Exogenous variables have means, variances, and covariances as associated parameters. This means that, for example, Mplus does not estimate a mean or a variance parameter for an endogenous variable such as $\tau _ { 2 }$ in the simplex model. However, the means and variances of endogenous variables can be computed based on other estimated model parameters. For example, by applying algebraic rules for means of linear combinations (see Box 2.4), the mean of $\tau _ { 2 }$ can be computed as 

$$
E (\tau_ {2}) = \beta_ {0 2} + \beta_ {1 2} \cdot E (\tau_ {1})
$$

because the means of all latent state residual variables $\zeta _ { t }$ are zero by definition in LST-R theory. 

Mplus recognizes the nature of variables (endogenous vs. exogenous) based on the structure of the specified model (ON and BY statements). If a variable appears on the left-hand side of at least one ON statement (structural regression or path coefficient) or on the right-hand side of at least one BY statement (factor loading), the variable is recognized as an endogenous (outcome) variable by Mplus. If a variable does not appear on the left-hand side of any ON statement 

in the model and also does not appear on the right-hand side of any BY statement in the model, the variable is recognized as an exogenous (purely independent) variable. Given that Mplus determines the nature of a variable (endogenous vs. exogenous) based on the model structure, the Mplus syntax does not contain separate symbols for means (exogenous variables) versus intercepts (endogenous variables) or for variances (exogenous variables) versus residual variances (endogenous variables). When a variable $X$ is exogenous, the mean of $X$ is referred to by specifying the variable name in brackets: [X];. The variance of exogenous variable $X$ is referred to by using just the variable name (without brackets): $\mathrm { x } ;$ . 

For an endogenous variable Y, the statement [Y]; refers to the Y intercept, and the statement Y; refers to the Y residual variance. For two exogenous variables $X _ { 1 }$ and $X _ { 2 }$ , the statement X1 with X2; refers to the covariance (correlation in the standardized solution) between $X _ { 1 }$ and $X _ { 2 }$ . For two endogenous variables $Y _ { 1 }$ and $Y _ { 2 }$ , the statement Y1 with Y2; refers to the covariance (residual correlation in the standardized solution) between the residual variables associated with $Y _ { 1 }$ and $Y _ { 2 }$ . 

that $\boldsymbol { \beta } _ { 1 t } = 1$ , $\beta _ { 0 t }$ can be interpreted as the mean difference between the two time points in this scenario, which is convenient. A researcher may thus test whether the constraint $\boldsymbol { \beta } _ { 1 t } = 1$ is tenable for all time points. If it is, then the estimated $\beta _ { 0 t }$ parameters directly reflect the mean differences relative to the preceding time point. The standard errors pertaining to $\beta _ { 0 t }$ can then be used to test whether there are statistically significant mean differences relative to the previous time point. 

In general, however, mean differences between two time points are not directly reflected in the $\beta _ { 0 t }$ parameter in the simplex model (i.e., unless $\beta _ { 1 t } =$ 1, $\beta _ { 0 t }$ does not directly reflect the mean difference between two time points). Nonetheless, by using the following “trick,” mean differences can still be examined in the simplex model even when $\boldsymbol { \beta } _ { 1 t } \neq 1$ . 

The mean of a given latent state variable $\tau _ { t } ,$ $t > 1$ , is not a parameter in the model because the latent state variables at all time points except Time 1 are endogenous (dependent) variables. Endogenous variables do not have means as parameters in a structural equation model (see Box 3.3 for details). Nevertheless, the means of all $\tau _ { t }$ variables for $t > 1$ can be computed based on other estimated model parameters using the following equation: 

$$
E (\tau_ {t}) = \beta_ {0 t} + \beta_ {1 t} \cdot E (\tau_ {t - 1})
$$

Based on this equation, the mean $E ( \tau _ { t } )$ can be defined as a “new” parameter in Mplus and set equal to $E ( \tau _ { t - 1 } )$ to test for differences in means. This can be accomplished by using the MODEL CONSTRAINT and MODEL TEST procedures in Mplus (see Box 2.7 on pages 40–41). 

# 3.2.5 Mplus Application

Below is the complete MODEL command for the simplex model including the MODEL CONSTRAINT and MODEL TEST procedures, again using hypothetical data from $N = 3 0 0$ individuals and their IQ scores obtained on four measurement occasions. (For this example, I generated data with equal measurement error variances across time. Box 3.4 on page 57 illustrates the Mplus code that would be used for the specification with equal state residual factor variances and freely estimated measurement error variances.) 

```txt
MODEL:  
TAU1 by Y1@1;  
TAU2 by Y2@1;  
TAU3 by Y3@1;  
TAU4 by Y4@1;  
TAU2 on TAU1 (beta12);  
TAU3 on TAU2 (beta13);  
TAU4 on TAU3 (beta14);  
[Y1-Y4@0];  
[TAU1] (E1);  
[TAU2] (beta02);  
[TAU3] (beta03);  
[TAU4] (beta04);  
Y1-Y4 (errvar);  
MODEL CONSTRAINT:  
NEW(E2 E3 E4);  
E2 = beta02 + beta12*E1;  
E3 = beta03 + beta13*E2;  
E4 = beta04 + beta14*E3;  
MODEL TEST:  
E1 = E2;  
E1 = E3;  
E1 = E4; 
```

In the above MODEL command, I specified the four latent state variables TAU with all loadings fixed at 1, as is implied by the simplex measurement equation. I connected the TAU variables through an autoregressive process by using ON statements. The corresponding autoregressive slope coefficients were given labels in parentheses (beta02, beta03, beta04), so that I could refer to those parameters later on in the MODEL CONSTRAINT option. I fixed all 

measurement intercepts to zero in this model by specifying [Y1-Y4@0];. This is because there are no additive constants in the simplex measurement equation $Y _ { t } = \tau _ { t } + \varepsilon _ { t }$ . Mplus, however, would by default estimate such additive constants, so that we have to set them to zero explicitly. 

The remaining freely estimated parameters in the simplex model are the mean of the first state variable $E ( \tau _ { 1 } )$ [TAU1], the three latent intercept constants $\beta _ { 0 2 }$ [TAU2], $\beta _ { 0 3 }$ [TAU3], and $\beta _ { 0 4 }$ [TAU4]; and the (time- invariant) 

# BOX 3.4. Specifying the Simplex Model with Equal State Residual Factor Variances

As explained in the text, another way to identify the simplex model is by setting the state residual factor variances equal across time rather than the measurement error variances. Below is the relevant Mplus MODEL statement (without the MODEL CONSTRAINT and MODEL TEST subcommands, which remain the same) for the version of the simplex model that constrains the state residual factor variances to be equal across time: 

```txt
MODEL:  
TAU1 by Y1@1;  
TAU2 by Y2@1;  
TAU3 by Y3@1;  
TAU4 by Y4@1;  
TAU2 on TAU1 (beta12);  
TAU3 on TAU2 (beta13);  
TAU4 on TAU3 (beta14);  
[Y1-Y4@0];  
[TAU1] (E1);  
[TAU2] (beta02);  
[TAU3] (beta03);  
[TAU4] (beta04);  
TAU2-TAU4 (resvar); 
```

Only the last line of code has changed in the MODEL command. Instead of setting the measurement error variances equal across time, the state residual factor variances are now set equal by specifying TAU2-TAU4 (resvar);. Because the variables TAU2 through TAU4 are endogenous variables in the model (each of them appears on the left hand side of an ON statement in the MODEL command; see Box 3.3 for details), the statement TAU2-TAU4 (resvar); refers to the residual variances $V a r ( \zeta )$ pertaining to these latent variables. The measurement error variances are freely estimated by default in Mplus. The MODEL CONSTRAINT and MODEL TEST options can be used in the same way as for the model version described in the text. 

measurement error variance Var(ε), Y1-Y4;. The mean of the first state variable $E ( \tau _ { \mathrm { l } } )$ was given the label(E1) to use this parameter in the MODEL CON-STRAINT option, and the measurement error variances for Times 1 through 4 were given the label (errvar) to set them equal across time. 

Subsequently, I used the MODEL CONSTRAINT option to define the means at Times 2, 3, and 4 as “new” parameters based on model parameters labeled in the regular MODEL command. This is analogous to the procedure shown for the $\xi$ -congeneric model in Section 2.4 in Chapter 2. In addition, I again used the MODEL TEST option to test the null hypothesis that all four means are equal in the population using an omnibus Wald statistic. Alternatively, the means can be constrained to be equal as part of the MODEL CONSTRAINT procedure, and the overall fit of this constrained model can be tested against a model version that leaves the means unconstrained. Below I show how means can be constrained to be equal using the MODEL CONSTRAINT option: 

```txt
MODELCONSTRAINT:  
0 = E1 - E2;  
0 = E1 - E3;  
0 = E1 - E4; 
```

Given that the restricted version is nested within the model with unconstrained (freely estimated) means, the two models can be compared via a chisquare difference test. In our example, the unconstrained model (with freely estimated means) yields a chi-square value of $\chi ^ { 2 } ( 2 ) = 3 . 0 2$ , $p = . 2 2$ . The constrained model (with all means set equal) yields a much higher chi-square value of $\chi ^ { 2 } ( 5 ) = 1 4 2 . 7 4 9$ , $p < . 0 0 1$ . The difference in chi-square values between the constrained and the unconstrained model is $\chi _ { \Delta } ^ { 2 } \left( 3 \right) = 1 3 9 . 7 2 9$ , $p < . 0 0 1$ , indicating that the null hypothesis of complete mean stability can be rejected for alpha $= . 0 5$ . 

The Mplus unstandardized parameter estimates for the simplex model with equal measurement error variables and freely estimated means are given below: 

<table><tr><td colspan="6">MODEL RESULTS</td></tr><tr><td></td><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-Tailed P-Value</td></tr><tr><td>TAU1</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y1</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>TAU2</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y2</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>TAU3</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y3</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>TAU4</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y4</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td colspan="6">TAU2 ON</td></tr><tr><td>TAU1</td><td>1.054</td><td>0.050</td><td>21.130</td><td>0.000</td><td></td></tr><tr><td colspan="6">TAU3 ON</td></tr><tr><td>TAU2</td><td>1.045</td><td>0.042</td><td>25.001</td><td>0.000</td><td></td></tr><tr><td colspan="6">TAU4 ON</td></tr><tr><td>TAU3</td><td>1.002</td><td>0.037</td><td>27.425</td><td>0.000</td><td></td></tr><tr><td colspan="6">Means</td></tr><tr><td>TAU1</td><td>100.109</td><td>0.880</td><td>113.805</td><td>0.000</td><td></td></tr><tr><td colspan="6">Intercepts</td></tr><tr><td>Y1</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td><td></td></tr><tr><td>Y2</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td><td></td></tr><tr><td>Y3</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td><td></td></tr><tr><td>Y4</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td><td></td></tr><tr><td>TAU2</td><td>-5.942</td><td>5.026</td><td>-1.182</td><td>0.237</td><td></td></tr><tr><td>TAU3</td><td>-7.762</td><td>4.205</td><td>-1.846</td><td>0.065</td><td></td></tr><tr><td>TAU4</td><td>-4.954</td><td>3.565</td><td>-1.389</td><td>0.165</td><td></td></tr><tr><td colspan="6">Variances</td></tr><tr><td>TAU1</td><td>195.124</td><td>19.480</td><td>10.017</td><td>0.000</td><td></td></tr><tr><td colspan="6">Residual Variances</td></tr><tr><td>Y1</td><td>37.013</td><td>4.496</td><td>8.232</td><td>0.000</td><td></td></tr><tr><td>Y2</td><td>37.013</td><td>4.496</td><td>8.232</td><td>0.000</td><td></td></tr><tr><td>Y3</td><td>37.013</td><td>4.496</td><td>8.232</td><td>0.000</td><td></td></tr><tr><td>Y4</td><td>37.013</td><td>4.496</td><td>8.232</td><td>0.000</td><td></td></tr><tr><td>TAU2</td><td>20.830</td><td>9.582</td><td>2.174</td><td>0.030</td><td></td></tr><tr><td>TAU3</td><td>30.007</td><td>7.631</td><td>3.932</td><td>0.000</td><td></td></tr><tr><td>TAU4</td><td>25.073</td><td>9.476</td><td>2.646</td><td>0.008</td><td></td></tr><tr><td colspan="6">New/Additional Parameters</td></tr><tr><td>E2</td><td>99.550</td><td>0.957</td><td>104.068</td><td>0.000</td><td></td></tr><tr><td>E3</td><td>96.295</td><td>1.043</td><td>92.303</td><td>0.000</td><td></td></tr><tr><td>E4</td><td>91.548</td><td>1.084</td><td>84.416</td><td>0.000</td><td></td></tr></table>

In this example, the mean of the latent state variable at Time 1 was estimated to be 100.109 IQ points, with a variance of 195.124 $\langle S D = 1 3 . 9 7$ IQ points). The autoregressive slope parameters $\beta _ { 1 t }$ in this example were all estimated to be close to 1.0. The intercepts $\beta _ { 0 t }$ were all negative. 

The latent state means for the endogenous state factors at Times 2, 3, and 4 are not part of the regular model output but are provided under NEW/ADDI-TIONAL PARAMETERS, given that we defined them using the MODEL CON-STRAINT option. The mean at Time 2 is very similar to the mean at Time 1. The means at Time 3 and Time 4 are smaller. 

Recall that the chi-square difference test indicated that at least two means may differ from one another. The Wald statistic confirms this result: 

<table><tr><td colspan="2">Wald Test of Parameter Constraints</td></tr><tr><td>Value</td><td>175.070</td></tr><tr><td>Degrees of Freedom</td><td>3</td></tr><tr><td>P-Value</td><td>0.0000</td></tr></table>

The Wald statistic and chi-square difference test are omnibus tests that only tell us whether at least two means differ significantly (similar to an omnibus $F$ test in analysis of variance). To examine which differences between means are statistically significant, the model can be reestimated with specific contrasts using the MODEL TEST option (e.g., testing only E1 = E2). When multiple comparisons are performed, an adjustment for type-1 error inflation (e.g., a Bonferroni correction) should be employed similarly to what one would do in analysis of variance. 

Below are selected standardized parameter estimates for the simplex model: 

<table><tr><td colspan="6">STANDARDIZED MODEL RESULTS (STDYX Standardization)</td></tr><tr><td></td><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-TailedP-Value</td></tr><tr><td>TAU1</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y1</td><td></td><td>0.917</td><td>0.013</td><td>72.035</td><td>0.000</td></tr><tr><td>TAU2</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y2</td><td></td><td>0.930</td><td>0.010</td><td>89.461</td><td>0.000</td></tr><tr><td>TAU3</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y3</td><td></td><td>0.942</td><td>0.009</td><td>108.998</td><td>0.000</td></tr><tr><td>TAU4</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y4</td><td></td><td>0.946</td><td>0.008</td><td>116.592</td><td>0.000</td></tr><tr><td>TAU2</td><td>ON</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU1</td><td></td><td>0.955</td><td>0.021</td><td>45.997</td><td>0.000</td></tr><tr><td>TAU3</td><td>ON</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU2</td><td></td><td>0.947</td><td>0.014</td><td>67.906</td><td>0.000</td></tr><tr><td>TAU4</td><td>ON</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU3</td><td></td><td>0.959</td><td>0.015</td><td>62.487</td><td>0.000</td></tr><tr><td colspan="2">Residual Variances</td><td></td><td></td><td></td><td></td></tr><tr><td>Y1</td><td></td><td>0.159</td><td>0.023</td><td>6.832</td><td>0.000</td></tr><tr><td>Y2</td><td></td><td>0.135</td><td>0.019</td><td>6.971</td><td>0.000</td></tr><tr><td>Y3</td><td></td><td>0.113</td><td>0.016</td><td>6.968</td><td>0.000</td></tr><tr><td>Y4</td><td></td><td>0.105</td><td>0.015</td><td>6.832</td><td>0.000</td></tr><tr><td>TAU2</td><td></td><td>0.088</td><td>0.040</td><td>2.211</td><td>0.027</td></tr><tr><td>TAU3</td><td></td><td>0.104</td><td>0.026</td><td>3.926</td><td>0.000</td></tr><tr><td>TAU4</td><td></td><td>0.079</td><td>0.029</td><td>2.694</td><td>0.007</td></tr><tr><td colspan="2">R-SQUARE</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">Observed</td><td></td><td></td><td></td><td>Two-Tailed</td></tr><tr><td colspan="2">Variable</td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>P-Value</td></tr><tr><td colspan="2">Y1</td><td>0.841</td><td>0.023</td><td>36.018</td><td>0.000</td></tr><tr><td colspan="2">Y2</td><td>0.865</td><td>0.019</td><td>44.731</td><td>0.000</td></tr><tr><td colspan="2">Y3</td><td>0.887</td><td>0.016</td><td>54.499</td><td>0.000</td></tr><tr><td colspan="2">Y4</td><td>0.895</td><td>0.015</td><td>58.296</td><td>0.000</td></tr><tr><td colspan="2">Latent</td><td></td><td></td><td></td><td>Two-Tailed</td></tr><tr><td colspan="2">Variable</td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>P-Value</td></tr><tr><td colspan="2">TAU2</td><td>0.912</td><td>0.040</td><td>22.998</td><td>0.000</td></tr><tr><td colspan="2">TAU3</td><td>0.896</td><td>0.026</td><td>33.953</td><td>0.000</td></tr><tr><td colspan="2">TAU4</td><td>0.921</td><td>0.029</td><td>31.244</td><td>0.000</td></tr></table>

The standardized factor loadings show that the IQ measure $Y _ { t }$ was strongly correlated with the state factor at each time point (loadings between .917 and .946), indicating high reliability of measurement (corresponding to observed variable $R ^ { 2 }$ values/reliabilities between .841 and .895). Furthermore, the standardized autoregressive path coefficients were estimated to be very close to 1.0 (range: .947 through .959). The standardized path coefficients in this model can be interpreted as correlations between adjacent state factors. The high correlations in this example indicate that there was a very high stability of interindividual differences in true IQ scores— which one would expect for a rather trait-like construct such as intelligence. 

# BOX 3.5. Direct versus Indirect (Mediated) Variable Effects in the Simplex Model

The structural (latent variable) equation in the simplex model $[ \tau _ { t } = \beta _ { 0 t } + \beta _ { 1 t }$ ⋅ $\tau _ { t - 1 } + \zeta _ { t }$ , for $t = 2 , \ldots , n ]$ $t = 2$ implies that a latent state variable exhibits both a direct effect on the immediately following state and indirect effects on later states (via the immediately following states). For example, the latent state variable at Time 1 (τ ) has a direct effect on the latent state variable at Time 2 $( \tau _ { 2 } )$ and indirect effects on subsequent states $\tau _ { 3 } , \ldots , \tau _ { n }$ . Indirect effects are frequently referred to as mediated variable effects or statistical mediation in the literature (e.g., MacKinnon, 2008). 

Mathematically, the strength of the direct effect of $\tau _ { 1 }$ on $\tau _ { 2 }$ is quantified by the regression coefficient $\beta _ { 1 2 }$ (in either unstandardized or standardized form). In unstandardized form, $\beta _ { 1 2 }$ gives the expected increase or decrease in $\tau _ { 2 }$ scores for a one-unit increase in $\tau _ { 1 }$ . In fully standardized form (STDYX solution in Mplus), $\beta _ { 1 2 }$ equals the model- implied correlation between $\tau _ { 1 }$ and $\tau _ { 2 }$ (as in any bivariate linear regression model). The indirect effect is the product of two or more regression coefficients. For example, the product $\beta _ { 1 2 } \cdot \beta _ { 1 3 }$ quantifies the indirect effect of $\tau _ { 1 }$ on $\tau _ { 3 }$ (via $\tau _ { 2 ^ { \prime } }$ ). Likewise, the product $\beta _ { 1 2 } \cdot \beta _ { 1 3 } \cdot \beta _ { 1 4 }$ quantifies the indirect effect of $\tau _ { 1 }$ on $\tau _ { 4 }$ (via $\tau _ { 2 }$ and $\tau _ { 3 ^ { \prime } }$ ). 

Given that in the simplex model, latent state variables have direct effects only on immediately following state variables, the influence (or “effect”) of, for example, $\tau _ { 1 }$ on $\tau _ { 3 }$ is fully mediated by $\tau _ { 2 }$ . Moreover, the effect of $\tau _ { 1 }$ on all subsequent states is also fully mediated. The assumption of full mediation implied by a first-order autoregressive process can be relaxed in multiple- indicator extensions of the simplex model (see Chapter 5). 

In Mplus, indirect (mediated) variable effects can be computed using the MODEL INDIRECT option. A complete Mplus input file illustrating the MODEL INDIRECT option for the simplex model can be found on the companion website (see the box at the end of the table of contents). 

The large path coefficients correspond to latent variable R-SQUARE values [consistencies $C o n ( \tau _ { t } ) ]$ ranging between .896 and .921. This indicates that between 89.6 and $9 2 . 1 \%$ of the true variability in IQ scores could be predicted based on the previous state factor in this example. The occasion-specificity coefficients $O s p ( \tau _ { t } )$ can be found under Residual variances for TAU1 through TAU3, and they ranged between .079 and .104. This shows that between 7.9 and $1 0 . 4 \%$ of the state variability $V a r ( \tau _ { t } )$ was due to situation and/or person $\times$ situation interaction effects at Time t. In Box 3.5, I explain the distinction between direct and indirect effects in the simplex model. 

# 3.2.6 Summary

The simplex model resolves some of the issues with the single-factor approaches discussed in Chapter 2. Most notably, the simplex model does not require the rank order of individuals’ true scores to remain the same across time. Moreover, the simplex model is an intuitive longitudinal model, as its structure maps well onto many social science processes for which previous behavior is the best predictor of subsequent behavior. The model also is well in line with one of the basic ideas of LST-R theory according to which previous situations can influence future behavior. 

The simplex model can be extended by adding covariates to the model or by examining the longitudinal processes for two or more constructs simultaneously in so-called autoregressive/cross-lagged models (Jöreskog, 1979a, 1979b). I discuss such cross-lagged extensions in detail in Chapter 5 for multipleindicator versions of the simplex model. A change score version of the simplex model is discussed next. 

# 3.3 THE LATENT CHANGE SCORE MODEL

# 3.3.1 Introduction

Researchers are often interested in studying interindividual differences in intraindividual changes across time. The simplex model includes state latent variables, but no variables that directly reflect interindividual variability in change across time. However, the simplex model can be reformulated as an equivalent latent change score model (see Figure 3.2; McArdle, 2009). The change score formulation has the same measurement model but includes latent state change score variables. The latent change score model thus allows researchers to study true state changes directly based on latent state difference score variables. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/61324d6289a429ea704dc01c165d8087ca7c56beaccd617385ecea2b596ce2af.jpg)



FIGURE 3.2. Path diagram of the latent change score version of the simplex model shown in Figure 3.1. $Y _ { t } =$ observed variable. $\tau _ { t } =$ latent state variable; $( \tau _ { t } - \tau _ { t - 1 } ) =$ latent state change score variable; $\varepsilon _ { t } =$ measurement error variable; $\gamma _ { 0 t } =$ constant regression intercept coefficient; $\gamma _ { 1 t } =$ constant regression slope coefficient; $\varsigma _ { t } =$ latent residual variable. Parameter restrictions necessary for model identification are discussed in the text.


# 3.3.2 Model Description

In the first step, the latent state variables at $t \geq 2$ are “decomposed” into the previous state plus change: 

$$
\tau_ {t} = \tau_ {t - 1} + (\tau_ {t} - \tau_ {t - 1})
$$

State $=$ Previous State + Change 

Notice that this decomposition does not involve making any additional restrictive assumptions. In fact, the decomposition is trivial in that we add something $( \tau _ { t - 1 } )$ to $\tau _ { t } ,$ and then we subtract the same thing again. Though seemingly trivial, this decomposition allows us to include the latent change score variables $( \tau _ { t } \mathrm { ~ - ~ } \tau _ { t \mathrm { ~ - ~ } 1 } )$ as “new” latent variables in the structural model. These variables reflect interindividual differences in true state changes across time. 

The latent change score variables $( \tau _ { t } - \tau _ { t - 1 } )$ are then regressed on the previous state in the structural model: 

$$
\left(\tau_ {t} - \tau_ {t - 1}\right) = \gamma_ {0 t} + \gamma_ {1 t} \cdot \tau_ {t - 1} + \varsigma_ {t}
$$

where $\boldsymbol { \gamma } _ { 0 t }$ is a fixed latent intercept, $\gamma _ { 1 t }$ is a fixed slope (path or regression) coefficient, and $\mathsf { \mathsf { S } } _ { t }$ is a latent residual change variable with a mean of zero that is uncorrelated with $\tau _ { t - 1 }$ . The change score residual variable $\varsigma _ { t }$ reflects interindividual differences in true state changes that cannot be linearly predicted from the previous state. It can therefore be interpreted as a variable representing residualized true change, where residualized means “adjusted for a linear relationship with the previous state.” 

Given that the change score model is just a reformulation of the simplex model, it makes the same assumptions, has the name number of parameters for a given number of measurement occasions, and will show an identical model fit in empirical applications. Assuming that all latent residual variances $V a r ( \varsigma _ { t } )$ [but not the measurement error variances $V a r ( \varepsilon _ { t } ) ]$ are set equal across time, we obtain $V a r ( \varsigma _ { t } ) = V a r ( \varsigma _ { s } ) = V a r ( \varsigma )$ for all time points t, $s = 2$ , . . . , n. Under this assumption, the change score model estimates the following parameters: 

•	 the state factor mean $E ( \tau _ { 1 } )$ at Time 1, 

•	 the state factor variance $V a r ( \tau _ { 1 } )$ at Time 1, 

•	 one residual change factor variance $V a r ( \varsigma )$ for all t, $s = 2$ , . . . , n, 

• $n - 1$ latent intercept constants $\boldsymbol { \gamma } _ { 0 t }$ , 

• $n - 1$ latent path (regression slope) constants $\boldsymbol { \gamma } _ { 1 t } .$ , and 

•	 n measurement error variances $V a r ( \varepsilon _ { t } )$ , one for each time point $t = 1$ , . . . , n. 

Therefore, in general, the latent change score model—like the simplex model—has $3 n + 1$ free model parameters when residual change factor variances are set equal across time and only 3n free model parameters when, instead, the measurement error variances are set equal across time. 

# 3.3.3 Variance Decomposition and Coefficients

The variance decomposition and reliability coefficient in the latent change score model are identical to the simplex model. In the latent variable portion of the model, the change score variance decomposition is as follows: 

$$
V a r (\tau_ {t} - \tau_ {t - 1}) = \gamma_ {1 t} ^ {2} \cdot V a r (\tau_ {t - 1}) + V a r (\varsigma_ {t}) \mathrm {f o r} t \geq 2
$$

Hence, there may be one portion of the variability in each change score variable that is due to the previous state $[ \gamma _ { 1 t } ^ { 2 } \cdot V a r ( \tau _ { t - 1 } ) ]$ and one portion that is due to other influences $[ V a r ( \varsigma _ { t } ) ]$ . The latent $R _ { ( \tau - \tau _ { t - 1 } ) } ^ { 2 }$ coefficient in the latent change score model gives the proportion of variability in change over time that is accounted for by the previous state: 

$$
\begin{array}{l} R _ {(\tau - \tau_ {t - 1})} ^ {2} = \gamma_ {1 t} ^ {2} \cdot \operatorname {V a r} \left(\tau_ {t - 1}\right) / \operatorname {V a r} \left(\tau_ {t} - \tau_ {t - 1}\right) \\ = \gamma_ {1 t} ^ {2} \cdot \operatorname {V a r} \left(\tau_ {t - 1}\right) / \left[ \gamma_ {1 t} ^ {2} \cdot \operatorname {V a r} \left(\tau_ {t - 1}\right) + \operatorname {V a r} \left(\varsigma_ {t}\right) \right] \\ = 1 - \{V a r (\varsigma_ {t}) / [ \gamma_ {1 t} ^ {2} \cdot V a r (\tau_ {t - 1}) + V a r (\varsigma_ {t}) ] \} \\ \end{array}
$$

When the standardized solution (STDYX) is requested, Mplus prints the $R _ { ( \tau - \tau _ { t - 1 } ) } ^ { 2 }$ coefficient under R-SQUARE Latent variable in the output. 

# 3.3.4 Mplus Application

In Mplus, the latent change score model can be specified as follows: 

```txt
MODEL:  
TAU1 by Y1@1;  
TAU2 by Y2@1;  
TAU3 by Y3@1;  
TAU4 by Y4@1;  
! define change score variables  
C21 by Y1@0;  
TAU2 on TAU1@1 C21@1;  
TAU2@0;  
C32 by Y1@0;  
TAU3 on TAU2@1 C32@1;  
TAU3@0;  
C43 by Y1@0;  
TAU4 on TAU3@1 C43@1;  
TAU4@0;  
! change score regressions with slope coefficients gamma t  
C21 on TAU1 (gamma12);  
C32 on TAU2 (gamma13);  
C43 on TAU3 (gamma14);  
[Y1-Y4@0]; ! observed intercepts fixed at zero  
[TAU1] (E1); ! latent state mean at Time 1  
[C21] (gamma02); ! latent change intercept T2 - T1  
[C32] (gamma03); ! latent change intercept T3 - T2  
[C43] (gamma04); ! latent change intercept T4 - T3  
Y1-Y4 (errvar); ! error variances set equal across time 
```

In the input file, the variables C21, C32, and C43 refer to the latent state change score variables for Time 2 minus Time 1 $( \tau _ { 2 } - \tau _ { 1 } )$ , Time 3 minus Time 2 $( \tau _ { 3 } - \tau _ { 2 } )$ , and Time 4 minus Time 3 $( \tau _ { 4 } - \tau _ { 3 } )$ , respectively. Note that the latent change score variables appear only in the structural model equations 

$$
\tau_ {t} = \tau_ {t - 1} + (\tau_ {t} - \tau_ {t - 1})
$$

and 

$$
\left(\tau_ {t} - \tau_ {t - 1}\right) = \gamma_ {0 t} + \gamma_ {1 t} \cdot \tau_ {t - 1} + \varsigma_ {t}
$$

and are thus not directly linked to any observed variables (see also Figure 3.2). Therefore, in order to define the latent change score variables in Mplus, a trick is used in which the variables are “measured by” an arbitrarily chosen observed variable with a loading of zero. This is shown, for example, by the command C21 by Y1@0;. The fixed loading of zero means that the change score variables are not directly measured by $Y _ { 1 }$ . This specification thus merely serves to trick Mplus into using another set of latent variables that are not directly connected to observed variables (in this case, the change score variables). 

Subsequently, the structural equation $\tau _ { t } = \tau _ { t - 1 } + ( \tau _ { t } - \tau _ { t - 1 } )$ is implemented using a regression (ON) statement in Mplus. The state variables in this equation are perfectly determined by the previous state plus change (there is no residual variable in the equation). Therefore, the residual variance of each state has to be fixed to zero for $t > 1$ . For example, the state residual variance at Time 2 is set to zero by specifying TAU2@0;. 

In the next step, the change score variables are regressed on the previous state variables, implementing the second structural equation $( \tau _ { t } - \tau _ { t - 1 } ) = \gamma _ { 0 t } + \gamma _ { 1 t }$ $\cdot \tau _ { t - 1 } + \varsigma _ { t }$ . An example is the statement C21 on TAU1 (gamma12);. In the last set of commands, I set the observed intercepts to zero, estimated the first (exogenous) state factor mean, estimated the latent change factor intercepts $\boldsymbol { \gamma } _ { 0 t }$ , and set the measurement error variances equal across time. 

For illustration, I fit the latent change score model to the same data set that I used above to illustrate the simplex model. Recall that in this hypothetical study, potential changes in IQ scores across time are examined. The simplex and latent change score models are mathematically equivalent and thus fit a given data set equally well. Below is an excerpt of the key Mplus parameter estimates for the change score model: 

<table><tr><td colspan="6">MODEL RESULTS</td></tr><tr><td></td><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-TailedP-Value</td></tr><tr><td colspan="6">C21 ON</td></tr><tr><td>TAU1</td><td></td><td>0.054</td><td>0.050</td><td>1.078</td><td>0.281</td></tr><tr><td colspan="6">C32 ON</td></tr><tr><td>TAU2</td><td></td><td>0.045</td><td>0.042</td><td>1.083</td><td>0.279</td></tr><tr><td colspan="6">C43 ON</td></tr><tr><td>TAU3</td><td></td><td>0.002</td><td>0.037</td><td>0.059</td><td>0.953</td></tr><tr><td colspan="6">Means</td></tr><tr><td>TAU1</td><td></td><td>100.109</td><td>0.880</td><td>113.805</td><td>0.000</td></tr><tr><td colspan="6">Intercepts</td></tr><tr><td>C21</td><td></td><td>-5.942</td><td>5.026</td><td>-1.182</td><td>0.237</td></tr><tr><td>C32</td><td></td><td>-7.761</td><td>4.205</td><td>-1.846</td><td>0.065</td></tr><tr><td>C43</td><td></td><td>-4.954</td><td>3.566</td><td>-1.389</td><td>0.165</td></tr><tr><td colspan="6">Variances</td></tr><tr><td>TAU1</td><td></td><td>195.123</td><td>19.480</td><td>10.017</td><td>0.000</td></tr><tr><td colspan="6">Residual Variances</td></tr><tr><td>C21</td><td></td><td>20.829</td><td>9.582</td><td>2.174</td><td>0.030</td></tr><tr><td>C32</td><td></td><td>30.006</td><td>7.631</td><td>3.932</td><td>0.000</td></tr><tr><td>C43</td><td></td><td>25.073</td><td>9.476</td><td>2.646</td><td>0.008</td></tr></table>

The unstandardized parameter estimates show us that the change score variables were unrelated to the immediately preceding states in this example. This can be seen from the estimated regression coefficients $\boldsymbol { \gamma } _ { 1 t }$ shown in the ON statements, which are small and not significantly different from zero. In other words, how much or how little individuals’ true IQ scores changed over time could not be predicted from their previous true IQ levels in these data. Individuals with high IQ scores did not change more (or less) than individuals with low IQ scores. The intercepts $\boldsymbol { \gamma } _ { 0 t }$ indicate the expected amount of change for individuals with previous IQ state scores of zero, which is not meaningful in this case because zero intelligence does not make sense (centering observed scores prior to the analysis would resolve this issue; this can be done in Mplus using the DEFINE command). The residual variances $V a r ( \varsigma _ { t } )$ indicate the amount of residual variability in the change scores after accounting for the previous states (which did not explain any significant amount of variability here). The very smallthe st $R _ { ( \tau - \tau _ { t - 1 } ) } ^ { 2 }$ values (to be found under R-SQUARE Latent Variable in ized solution) also show that in this example, the change score variables were virtually unrelated to the previous state levels: 

<table><tr><td>STANDARDIZED MODEL</td><td>RESULTS (STDYX</td><td colspan="3">Standardization)</td></tr><tr><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-TailedP-Value</td></tr><tr><td>R-SQUARE</td><td></td><td></td><td></td><td></td></tr><tr><td>LatentVariable</td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-TailedP-Value</td></tr><tr><td>C21</td><td>0.026</td><td>0.053</td><td>0.494</td><td>0.622</td></tr><tr><td>C32</td><td>0.016</td><td>0.030</td><td>0.535</td><td>0.593</td></tr><tr><td>C43</td><td>0.000</td><td>0.002</td><td>0.029</td><td>0.977</td></tr></table>

# 3.3.5 Summary

The latent change score model represents a convenient reparameterization of the simplex model when a researcher is interested in studying interindividual differences in change across time. In extended change score models, the change score variables may be related to external variables (e.g., gender, age, other individual difference variables) to examine predictors of interindividual differences in change while controlling for the previous state level of the same construct. In Mplus, additional predictor variables can simply be added to the ON statements in the MODEL command (they also have to be listed in the USEVARIABLES statement in the VARIABLE command). In these extended models, the $\boldsymbol { \gamma } _ { 1 t }$ coefficients are interpreted as partial regression coefficients as in standard multiple regression analysis. In addition, change score variables can also be used as independent variables themselves to predict other outcomes. In that case, the change score variables would appear on the right hand side of ON statements. 

Even though attractive in many ways, both the simplex model and its change score version have some limitations. One limitation is that they require at least four measurement occasions as well constraints on either the measurement error or latent residual variances to be identified. Researchers may only have access to fewer than four time points and/or the required constraints may not be plausible in empirical applications (e.g., the amount of measurement error is sometimes larger at the first wave of a longitudinal study than at subsequent waves). The simplex model is also not suitable for purely state-like constructs that show very low stability of interindividual differences across time. In this case, the model may become empirically underidentified due to very small or zero autoregressive coefficients $\beta _ { 1 t }$ . These limitations are addressed by multipleindicator models discussed in Chapter 5. Another limitation of the simplex and change models is that they do not allow separating trait variance from state residual variance. The next model addresses this limitation. 

# 3.4 THE TRAIT–STATE–ERROR MODEL

# 3.4.1 Introduction

One limitation of the previously described single-factor models (random intercept, random and fixed intercepts, $\xi$ -congeneric; see Chapter 2) from the perspective of LST-R theory is that these models only include trait latent variables, but no state residual latent variables. As a consequence, these models do not allow separating variance components due to trait versus state residual (situational and person $\times$ situation interaction) influences. The simplex model presented in Section 3.2 is a multifactor model that allows separating temporally stable variance (consistency) from reliable situation-specific variance (occasion specificity) and measurement error variance (unreliability) for $t \geq 2$ . However, the simplex model also does not explicitly separate trait components from state residual and measurement error components for all measurement occasions. Kenny and Zautra (1995) presented a single-indicator longitudinal model that allows separating trait, state residual, and measurement error components for all time points. 

# 3.4.2 Model Description

The so-called trait–state–error (TSE) model is depicted in Figure 3.3.3 The TSE model resembles the simplex model described above in that it also allows for a first-order autoregressive process (represented by the autoregressive slope coefficient $\delta _ { \mathrm { 1 } }$ in Figure 3.3). However, in contrast to the simplex model, the TSE model contains a trait factor $\xi _ { 1 }$ in addition to occasion-specific latent residual variables $\zeta _ { t }$ and $O _ { t }$ and measurement error variables $\varepsilon _ { t }$ .4 Therefore, as I show in detail later, the TSE model allows separating various variance components of interest in LST-R theory. 

Using the concepts and notation of LST-R theory, we can describe the measurement portion of the TSE model by the following equation: 

$$
Y _ {t} = \left\{ \begin{array}{l} \zeta_ {1} + \zeta_ {1} + \varepsilon_ {1} \text {f o r} t = 1 \\ \delta_ {0 t} + \xi_ {1} + O _ {t} + \varepsilon_ {t} \text {f o r} t \geq 2 \end{array} \right.
$$

where $\delta _ { 0 t }$ indicates a real constant (fixed intercept). 

Notice that for Time 1, the TSE measurement model equation is identical to the basic LST-R decomposition of an observed variable into trait, state residual, and measurement error components. On subsequent time points, the observed variables are decomposed into a constant intercept $\delta _ { 0 t } ,$ the Time-1 trait factor $\xi _ { 1 }$ , a latent residual variable $O _ { t } ,$ and a measurement error variable $\mathcal { E } _ { t }$ . There is no 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/1f86aed40d6c6572dfa53a58ebe0521cdf8a48d06ce60d3139086b078842f535.jpg)



FIGURE 3.3. Path diagram of the trait–state–error (TSE) model. $Y _ { t } =$ observed variable; $\tau _ { t } =$ latent state variable; $\xi _ { 1 } =$ latent trait factor at Time 1; $\zeta _ { t } =$ latent state residual variable; $O _ { t } =$ latent occasion residual variable; $\varepsilon _ { t } =$ measurement error variable; $\delta _ { \scriptscriptstyle 0 t } =$ constant regression intercept coefficient; $\ S _ { 1 } =$ constant autoregressive slope coefficient. Parameter restrictions necessary for model identification are discussed in the text.


intercept (additive constant) for Time 1, implying $\delta _ { 0 1 } = 0$ . The reason for this specification is explained in detail later.5 The latent residual variables $\zeta _ { 1 }$ and $O _ { t }$ both reflect true score variability that is not accounted for by the trait $\xi _ { 1 }$ . (In Box 3.6, I explain why it is useful to use different symbols [i.e., $\zeta _ { t }$ vs. $O _ { t } ]$ for these latent residual variables.) 

In the structural (latent variable) portion of the TSE model, the latent residual variables $\zeta _ { 1 }$ and $O _ { t }$ are connected through a first-order autoregressive process with an autoregressive path (slope) coefficient $\delta _ { \mathrm { l } }$ such that 

$$
O _ {t} = \left\{ \begin{array}{l} \delta_ {1} \cdot \zeta_ {1} + \zeta_ {2} \text {f o r} t = 2 \\ \delta_ {1} \cdot O _ {t - 1} + \zeta_ {t} \text {f o r} t \geq 3 \end{array} \right.
$$

where $\delta _ { \mathrm { 1 } }$ denotes a real constant. Notice that the autoregressive slope coefficient $\delta _ { \mathrm { 1 } }$ does not have an index t for the time point, implying that this parameter is assumed to be time-invariant.6 

The TSE model implies that there is one part of each occasion residual $O _ { t }$ that can be explained by previous deviations from the trait $( \delta _ { \mathrm { 1 } } \cdot \zeta _ { \mathrm { 1 } }$ for $t = 2$ and $\delta _ { \mathrm { l } }$ ⋅ $O _ { t - 1 }$ for $t \geq 3$ ) and one part that is unique to the given time point and cannot be 

explained by previous deviations from the trait $\zeta _ { t }$ for $t \geq 2 )$ ). Note that there is no additive constant (intercept) in the structural equation for $O _ { t } .$ because the $O _ { t }$ variables are regression residual variables that have means equal to zero by definition. 

The autoregression among the $O _ { t }$ variables implies the presence of so-called carryover effects, which are very common in social science data, especially when measurement occasions are closely spaced in time. For example, in ecological momentary assessments (EMA), an individual’s momentary deviation from his or her general (trait) mood level (i.e., a worse than normal or better than normal mood state) often carries over to the next measurement occasion—particularly when the next occasion is only a few hours away. Over time, a person’s particularly bad or good mood tends to change back toward his or her normal (trait) level. Such a process of short-term stability of mood state deviations from general trait mood levels is captured by the autoregressive effects among residual variables in the TSE model. The autoregressive slope parameter $\delta _ { \mathrm { 1 } }$ allows quantifying the strength of the autoregression. In completely standardized form (STDYX solution in Mplus) or under specific restrictions that I discuss later on in this chapter, $\delta _ { 1 }$ gives the correlation between adjacent latent residual variables. The higher the correlation, the stronger the carryover effects. 

Although both $\zeta _ { t }$ and $O _ { t }$ reflect variability in the measured variables $Y _ { t }$ that is not accounted for by the trait factor $\xi _ { 1 }$ , the variables $\zeta _ { t }$ and $O _ { t }$ differ in their meaning (hence the use of different symbols to represent them). As I show in Box 3.6, the variables $\zeta _ { t }$ are identical to the latent state residuals in the sense of LST-R theory. Therefore, the latent state residual variables $\zeta _ { t }$ reflect variability in the measured variables $Y _ { t }$ that is due to situational and/or person $\times$ situation interaction influences at Time t. In contrast, the occasion residual variables $O _ { t }$ are a function of the latent state residual variable $\zeta _ { t }$ and previous latent state residuals (Eid, Holtmann, Santangelo, & Ebner-Priemer, 2017; see Box 3.6). The variables $O _ { t }$ thus reflect variability in the measured variables $Y _ { t }$ that is due to either current situational and/or person $\times$ situation interaction influences (represented by $\zeta _ { t } )$ or previous situational and/or person $\times$ situation interaction influences (represented by $\zeta _ { 1 }$ and/or $\delta _ { 1 } \cdot O _ { t - 1 } )$ ). 

The random and fixed intercepts model described in Chapter 2, Section 2.3, can be seen as a special case of the TSE model in which all latent residual variables are zero (i.e., $\zeta _ { t } = O _ { t } = 0$ for all $t = 1$ , . . . , n). The simplex model described in Section 3.2 of this chapter could be seen as a special case of the TSE model in which the trait factor is omitted. In that case, the residual variables $\zeta _ { 1 }$ and $O _ { t }$ would represent latent states $\tau _ { t }$ . 

To be identified, the TSE model requires at least four measurement occasions. In addition, Kenny and Zautra (1995) presented the following simplifying 

# BOX 3.6. Defining the TSE Model Based on LST‑R Theory

Eid et al. (2017) showed how a model that is closely related to the TSE model can be defined as a model of LST-R theory and stated that the TSE model can be understood as a restricted version of their model. Here I show how the TSE model presented by Kenny and Zautra (1995; 2001) can be derived based on the concepts of LST-R theory. 

As described in Chapter 1, the measurement portion of the TSE model is in line with the basic LST-R decomposition of a measured variable $Y _ { t }$ into a latent state variable $\tau _ { t }$ and a measurement error variable $\mathcal { E } _ { t }$ : 

$$
Y _ {t} = \tau_ {t} + \varepsilon_ {t}
$$

According to LST-R theory, each latent state variable itself can be decomposed into a latent trait and a latent state residual variable: 

$$
\tau_ {t} = \xi_ {t} + \zeta_ {t} \text {f o r a l l} t = 1, \dots , n
$$

such that $\begin{array} { r } { Y _ { t } = \xi _ { t } + \zeta _ { t } + \varepsilon _ { t } . } \end{array}$ 

In terms of LST-R theory, the TSE model implies that for $t \geq 2$ , the trait variables $\xi _ { t }$ are linear functions of (1) the Time-1 trait variable $( \xi _ { 1 } )$ and (2) all previous state residual variables $\zeta _ { 1 } , \ldots , \zeta _ { ( t - 2 ) } , \zeta _ { ( t - 1 ) }$ $\zeta _ { ( t - 1 ) }$ such that 

$$
\xi_ {t} = \left\{ \begin{array}{l} \xi_ {1} \text {f o r} t = 1 \\ \delta_ {0 2} + \xi_ {1} + \delta_ {1} \cdot \zeta_ {1} \text {f o r} t = 2 \\ \delta_ {0 3} + \xi_ {1} + \delta_ {1} ^ {2} \cdot \zeta_ {1} + \delta_ {1} \cdot \zeta_ {2} \text {f o r} t = 3 \\ \delta_ {0 t} + \xi_ {1} + \delta_ {1} ^ {t - 1} \cdot \zeta_ {1} + \delta_ {1} ^ {t - 2} \cdot \zeta_ {2} + \ldots + \delta_ {1} ^ {2} \cdot \zeta_ {t - 2} + \delta_ {1} \cdot \zeta_ {t - 1} \text {f o r} t \geq 4 \end{array} \right.
$$

where $\delta _ { 0 t }$ and $\delta _ { \mathrm { l } }$ denote real constants. Note that the influence of the Time-1 trait does not change over time, whereas the influence of previous state residuals changes unless $\delta _ { \mathrm { 1 } } = \mathrm { 1 }$ . For Time 2, we obtain the following decomposition of the trait variable: 

$$
\xi_ {2} = \delta_ {0 2} + \xi_ {1} + \delta_ {1} \cdot \zeta_ {1}
$$

such that 

$$
\begin{array}{l} Y _ {2} = \xi_ {2} + \zeta_ {2} + \varepsilon_ {2} \\ = \delta_ {0 2} + \xi_ {1} + \delta_ {1} \cdot \zeta_ {1} + \zeta_ {2} + \varepsilon_ {2} \\ = \delta_ {0 2} + \xi_ {1} + O _ {2} + \varepsilon_ {2} \\ \end{array}
$$

where $O _ { 2 } \equiv \delta _ { 1 } \cdot \zeta _ { 1 } + \zeta _ { 2 }$ and the $\equiv$ symbol indicates that the residual variable $O _ { 2 }$ is defined to be equal to the linear combination $\boldsymbol { \delta } _ { 1 } \cdot \boldsymbol { \zeta } _ { 1 } + \boldsymbol { \zeta } _ { 2 }$ . 

Hence, I defined the residual variable $O _ { 2 }$ to be a function of the current and previous state residuals $( \boldsymbol { \delta } _ { 1 } \cdot \boldsymbol { \zeta } _ { 1 } + \boldsymbol { \zeta } _ { 2 } )$ . This function reflects the autoregressive process in the TSE model. 

For Time 3, we obtain the following equations: 

$$
\begin{array}{l} \xi_ {3} = \delta_ {0 3} + \xi_ {1} + \delta_ {1} ^ {2} \cdot \zeta_ {1} + \delta_ {1} \cdot \zeta_ {2} \\ = \delta_ {0 3} + \xi_ {1} + \delta_ {1} \cdot (\delta_ {1} \cdot \zeta_ {1} + \zeta_ {2}) \\ \end{array}
$$

such that 

$$
\begin{array}{l} Y _ {3} = \xi_ {3} + \zeta_ {3} + \varepsilon_ {3} \\ = \delta_ {0 3} + \xi_ {1} + \delta_ {1} \cdot (\delta_ {1} \cdot \zeta_ {1} + \zeta_ {2}) + \zeta_ {3} + \varepsilon_ {3} \\ = \delta_ {0 3} + \xi_ {1} + \delta_ {1} \cdot O _ {2} + \zeta_ {3} + \varepsilon_ {3} \\ = \delta_ {0 2} + \xi_ {1} + O _ {3} + \varepsilon_ {3} \\ \end{array}
$$

where 

$$
O _ {3} \equiv \delta_ {1} \cdot (\delta_ {1} \cdot \zeta_ {1} + \zeta_ {2}) + \zeta_ {3} = \delta_ {1} \cdot O _ {2} + \zeta_ {3}
$$

Again, I defined the residual variable $O _ { 3 }$ as a function of the current and previous state residuals $[ { \boldsymbol { \delta } } _ { 1 } \cdot ( { \boldsymbol { \delta } } _ { 1 } \cdot { \boldsymbol { \zeta } } _ { 1 } + { \boldsymbol { \zeta } } _ { 2 } ) + { \boldsymbol { \zeta } } _ { 3 } ]$ , reflecting the autoregressive process in the TSE model. The equations for subsequent time points can be derived in an analogous way. (As in the simplex model, they become increasingly complex with increasing t.) 

The above derivations show a number of interesting features of the TSE model. First, the model is in line with LST-R theory, as it allows for the potential influence of both the initial trait variable and previous state residual variables on individuals’ subsequent trait scores. This appears to make a lot of sense for many social science phenomena: Individuals remain to some extent stable over time (there is an ongoing “trait” influence), but individuals also respond to events and experiences that they encounter and those experiences may alter their subsequent trait scores (i.e., situations may change a person). Note that this is conceptually similar to what is assumed in the simplex model described in Section 3.2. 

Second, the derivations show that the residual variables $\zeta _ { t }$ are equal to the state residual variables as defined in LST-R theory. Therefore, these variables have a very clear interpretation. They represent situation and/or person $\times$ situation interaction effects on a given time point t. That is, the state residual 

variables $\zeta _ { t }$ represent influences that are unique to a given time point and that can be explained neither by previous trait influences nor by previous situational and/or person $\times$ situation interaction influences pertaining to the same construct. In contrast, each residual variable $O _ { t }$ represents a linear function of the current plus previous state residual variables. 

Notice that linear independence assumptions regarding measurement error and latent variables are not required in the TSE model, as by definition in LST-R theory, $C o \nu ( \varepsilon _ { t } , \zeta _ { s } ) = C o \nu ( \zeta _ { t } , \zeta _ { s } ) = 0$ , and $C o \nu ( \varepsilon _ { t } , \xi _ { s } ) = C o \nu ( \zeta _ { t } , \xi _ { s } ) = 0$ for $s \leq t$ . 

restrictions, not all of which are necessary for the TSE model to be identified.7 In Kenny and Zautra’s (1995) specification, 

1. All factor loadings are set equal within a given wave (it is common to simply fix all loadings to 1 as is implied in the above model equations; I follow this approach here). 

2. All measurement error variances are assumed to be equal across time such that $V a r ( \varepsilon _ { t } ) = V a r ( \varepsilon _ { s } ) = V a r ( \varepsilon )$ for all t $, s = 1 , \ldots , n$ $s = 1$ . 

3. All latent residual variances are assumed to be equal such that $V a r ( \zeta _ { 1 } ) =$ $V a r ( O _ { t } ) = V a r ( O _ { s } ) = V a r ( R )$ for all t, $s = 1$ , . . . , n. 

4. The autoregressive parameter $\delta _ { \mathrm { 1 } }$ is assumed to be equal across time. 

The above restrictions lead to a parsimonious model with only a few parameters to estimate (see below). In addition, setting all latent residual variances equal has the advantage that, under this specification, the autoregressive parameter $\delta _ { 1 }$ equals the common correlation $\phi$ between adjacent latent residual variables and thus is easy to interpret.8 With the above restrictions in place, the TSE model allows estimating the following free parameters: 

•	 the Time-1 trait factor mean $E ( \xi _ { 1 } )$ 

•	 the Time-1 trait factor variance $V a r ( \xi _ { 1 } )$ , 

•	 one common latent residual variance Var(R), 

•	 one constant autoregressive slope parameter $\delta _ { \mathrm { 1 } }$ (common correlation $\phi$ ), 

• $n - 1$ intercept constants $\delta _ { 0 t }$ (the intercept parameter at Time 1 has to be fixed to zero such that $\delta _ { 0 1 } = 0 \up$ ), and 

•	 one measurement error variance Var(ε). 

Therefore, the model in general has $n + 4$ free model parameters, where n again indicates the total number of measurement occasions. In our example, the TSE model has $4 + 4 = 8$ free model parameters and $1 4 - 8 = 6$ df. 

When only the variance/covariance structure of the measured variables is analyzed and the mean structure is left out, the number of parameters reduces to 4, regardless of the number of measurement occasions. This is because, in that case, the trait mean $E ( \xi _ { 1 } )$ and the $n - 1$ intercepts $\delta _ { 0 t }$ are no longer estimated. (The df remain unchanged when the mean structure is ignored.) In Box 3.7, I discuss the mean structure in the TSE model in detail, and I also show an alternative equivalent way to identify the mean structure in this model. 

# 3.4.3 Variance Decomposition and Coefficients

One of the most useful features of the TSE model is that it can be used to estimate various variance components due to trait effects, situation and/or person $\times$ situation interaction effects, and measurement error. The basic observed variable variance decomposition in LST-R theory also holds for the TSE model: 

$$
V a r \left(Y _ {t}\right) = V a r \left(\tau_ {t}\right) + V a r \left(\varepsilon_ {t}\right)
$$

In analogy to the previously discussed models, the TSE model allows researchers to estimate the reliability $R e l ( Y _ { t } )$ of the observed scores at each time point. As in the simplex model, the basic definition of reliability in LST-R theory applies: 

$$
\begin{array}{l} R e l (Y _ {t}) = \operatorname {V a r} (\tau_ {t}) / \operatorname {V a r} (Y _ {t}) \\ = 1 - \left[ \operatorname {V a r} \left(\varepsilon_ {\mu}\right) / \operatorname {V a r} \left(Y _ {\mu}\right) \right] \\ \end{array}
$$

In the TSE model, latent state variables $\tau _ { t }$ are not directly included but are a function of the trait variable $\xi _ { 1 }$ and latent residual variables $\zeta _ { 1 }$ or $O _ { t }$ : 

$$
\tau_ {t} = \left\{ \begin{array}{l} \xi_ {1} + \zeta_ {1} \text {f o r} t = 1 \\ \delta_ {0 t} + \xi_ {1} + O _ {t} \text {f o r} t \geq 2 \end{array} \right.
$$

Given that $\xi _ { 1 }$ is uncorrelated with both $\zeta _ { 1 }$ and all $O _ { t } ,$ the variance of the latent state variables is given by 

$$
V a r (\tau_ {t}) = \left\{ \begin{array}{l} V a r (\xi_ {1}) + V a r (\zeta_ {1}) \text {f o r} t = 1 \\ V a r (\xi_ {1}) + V a r (O _ {t}) \text {f o r} t \geq 2 \end{array} \right.
$$

# BOX 3.7. The Mean Structure in the TSE Model

The TSE model includes a (potentially time- varying) intercept parameter δ0t. $\delta _ { 0 t }$ This implies that trait scores can change over time by an additive constant $\delta _ { 0 t }$ , similar to the random and fixed intercepts model described in Section 2.3 in Chapter 2. As I explained in Box 3.6, from the perspective of LST theory, each trait variable $\xi _ { t }$ in the TSE model is a linear function of the Time-1 trait variable plus previous state residual variables. Therefore, the mean of $\xi _ { t }$ is given by 

$$
E (\xi_ {t}) = \delta_ {0 t} + E (\xi_ {1}), \mathrm {w h e r e} \delta_ {0 1} = 0
$$

This is because all state residuals $\zeta _ { t }$ have means of zero by definition, so that the mean of a given trait $\xi _ { t }$ is determined solely by the Time-1 trait mean plus a constant $\delta _ { 0 t }$ . The intercept constant therefore gives the mean difference relative to the Time-1 trait mean; that is, 

$$
\delta_ {0 t} = E (\xi_ {t}) - E (\xi_ {1})
$$

If in a given application the estimate of $\delta _ { 0 t }$ is significantly different from zero, this means that there is a significant mean difference between Time t and Time 1. 

An alternative equivalent way to specify the mean structure in the TSE model was presented by Kenny and Zautra (1995). In their alternative specification, all n trait means $E ( \xi _ { t } )$ are fixed to zero [including $E ( \xi _ { 1 } ) = 0 ]$ ] and all n intercepts $\delta _ { 0 t }$ are estimated (including the intercept for Time 1, $\delta _ { 0 1 ^ { \prime } }$ ). In this specification, the intercepts reflect the n trait means rather than the mean differences relative to Time 1. 

In Mplus, this alternative specification is obtained by default. (The Mplus default is to fix all latent variable means to zero and to freely estimate the intercepts for all measured variables). It can be made explicit by specifying 

```txt
[Y1-Y4*]；[KSI1@0]； 
```

in the MODEL command. 

For $t \geq 2$ , the latent state variance can also be written as 

$$
V a r (\tau_ {t}) = \left\{ \begin{array}{l} V a r (\xi_ {1}) + \delta_ {1} ^ {2} \cdot V a r (\zeta_ {1}) + V a r (\zeta_ {2}) \text {f o r} t = 2 \\ V a r (\xi_ {1}) + \delta_ {1} ^ {4} \cdot V a r (\zeta_ {1}) + \delta_ {1} ^ {2} \cdot V a r (\zeta_ {2}) + V a r (\zeta_ {3}) \text {f o r} t = 3 \\ V a r (\xi_ {1}) + (\delta_ {1} ^ {t - 1}) ^ {2} \cdot V a r (\zeta_ {1}) + (\delta_ {1} ^ {t - 2}) ^ {2} \cdot V a r (\zeta_ {2}) + \dots + \delta_ {1} ^ {4} \\ \quad \cdot V a r (\zeta_ {t - 2}) + \delta_ {1} ^ {2} \cdot V a r (\zeta_ {t - 1}) + V a r (\zeta_ {t}) \text {f o r} t \geq 4 \end{array} \right.
$$

The measured variable variance can thus be broken down as follows: 

$$
\operatorname {V a r} \left(Y _ {t}\right) = \left\{ \begin{array}{l} \operatorname {V a r} \left(\xi_ {1}\right) + \operatorname {V a r} \left(\zeta_ {1}\right) + \operatorname {V a r} \left(\varepsilon_ {1}\right) \text {f o r} t = 1 \\ \operatorname {V a r} \left(\xi_ {1}\right) + \operatorname {V a r} \left(O _ {t}\right) + \operatorname {V a r} \left(\varepsilon_ {t}\right) \text {f o r} t \geq 2 \end{array} \right.
$$

Therefore, the $R e l ( Y _ { t } )$ coefficient can be rewritten for the TSE model as follows: 

$$
R e l (Y _ {t}) = \left\{ \begin{array}{l} \left[ V a r (\xi_ {1}) + V a r (\zeta_ {1}) \right] / \left[ V a r (\xi_ {1}) + V a r (\zeta_ {1}) + V a r (\varepsilon_ {1}) \right] \text {f o r} t = 1 \\ \left[ V a r (\xi_ {1}) + V a r (O _ {t}) \right] / \left[ V a r (\xi_ {1}) + V a r (O _ {t}) + V a r (\varepsilon_ {t}) \right] \text {f o r} t \geq 2 \end{array} \right.
$$

The $R e l ( Y )$ coefficient is printed under R-SQUARE Observed Variable in the Mplus output when the standardized solution STDYX is requested. A consistency coefficient for the latent state variables $C o n ( \tau _ { t } )$ can be defined as follows (Eid et al., 2017): 

$$
C o n (\tau_ {t}) = \left\{ \begin{array}{l} V a r (\xi_ {1}) / V a r (\tau_ {1}) \text {f o r} t = 1 \\ [ V a r (\xi_ {1}) + \delta_ {1} ^ {2} \cdot V a r (\zeta_ {1}) ] / V a r (\tau_ {2}) \text {f o r} t = 2 \\ [ V a r (\xi_ {1}) + \delta_ {1} ^ {4} \cdot V a r (\zeta_ {1}) + \delta_ {1} ^ {2} \cdot V a r (\zeta_ {2}) ] / V a r (\tau_ {3}) \text {f o r} t = 3 \\ [ V a r (\xi_ {1}) + (\delta_ {1} ^ {t - 1}) ^ {2} \cdot V a r (\zeta_ {1}) + (\delta_ {1} ^ {t - 2}) ^ {2} \cdot V a r (\zeta_ {2}) + \dots + \delta_ {1} ^ {4} \\ \quad \cdot V a r (\zeta_ {t - 2}) + \delta_ {1} ^ {2} \cdot V a r (\zeta_ {t - 1}) ] / V a r (\tau_ {t}) \text {f o r} t \geq 4 \end{array} \right.
$$

$C o n ( \tau _ { t } )$ ranges between 0 and 1 and indicates the proportion of variability in latent state scores that is due to previous trait and/or state residual influences. In other words, $C o n ( \tau _ { t } )$ reflects all influences on the state variable $\tau _ { t }$ that lie in the past and are not due to current (Time-t) situational or person $\times$ situation interaction influences. For example, a value of $C o n ( \tau _ { t } ) = . 8$ means that $8 0 \%$ of the variability in $\tau _ { t }$ scores is due to previous trait, situational, or person $\times$ situation interaction influences. The $C o n ( \tau _ { t } )$ coefficient thus indicates the degree of stability in state scores across time. 

We can see that for Time 1, consistency is based solely on the ratio of Trait-1 variance to total state variance. This is because at Time 1, we have no 

knowledge about previous (i.e., prior-to-Time-1) state residual influences. As a consequence, prior-to-Time-1 situational and person $\times$ situation interaction influences are part of the Time-1 trait variable and inseparable from it. For the subsequent time points $t \geq 2$ , the equations become more and more complex because consistency is now not only based on the Time-1 trait influence, but also takes into account the influence of (the increasing number of) previous state residuals. In other words, one part of the stability (“consistency”) in the TSE model is reflected by the Time-1 trait, and the other part is reflected in the autoregressive structure that characterizes the influence of previous situations and/or person $\times$ situation interactions on the current trait. These two components are additive and can also be looked at separately (Eid et al., 2017).9 

The trait consistency coefficient $T C o n ( \tau _ { t } )$ reflects the proportion of state variability that is due only to the Time-1 trait: 

$$
T C o n (\boldsymbol {\tau} _ {t}) = V a r (\xi_ {1}) / V a r (\boldsymbol {\tau} _ {t})
$$

Notice that for Time 1, $T C o n ( \tau _ { \mathrm { l } } ) = C o n ( \tau _ { \mathrm { l } } )$ , because there are no known previous state residual influences at Time 1. For $t \geq 2$ , $T C o n ( \tau _ { t } )$ will be smaller than $C o n ( \tau _ { t } )$ unless there is no autoregressive stability $\left( \delta _ { \mathrm { l } } = 0 \right.$ ; in this case, the TSE model is no longer mathematically identified) or all previous $V a r ( \zeta _ { t } ) = 0$ (no previous situational or person $\times$ situation interaction influences). 

The situation consistency coefficient $S C o n ( \tau _ { t } )$ excludes the Time-1 trait influence and thus reflects the proportion of state variability that is solely due to previous state residual influences: 

$$
S C o n (\tau_ {t}) = \left\{ \begin{array}{l} 0 \text {f o r} t = 1 \\ \delta_ {1} ^ {2} \cdot V a r (\zeta_ {1}) / V a r (\tau_ {2}) \text {f o r} t = 2 \\ [ \delta_ {1} ^ {4} \cdot V a r (\zeta_ {1}) + \delta_ {1} ^ {2} \cdot V a r (\zeta_ {2}) ] / V a r (\tau_ {3}) \text {f o r} t = 3 \\ [ (\delta_ {1} ^ {t - 1}) ^ {2} \cdot V a r (\zeta_ {1}) + (\delta_ {1} ^ {t - 2}) ^ {2} \cdot V a r (\zeta_ {2}) + \dots + \delta_ {1} ^ {4} \cdot V a r (\zeta_ {t - 2}) \\ \qquad + \delta_ {1} ^ {2} \cdot V a r (\zeta_ {t - 1}) ] / V a r (\tau_ {t}) \text {f o r} t \geq 4 \end{array} \right.
$$

Notice that for Time 1, $S C o n ( \tau _ { \mathrm { l } } ) = 0$ by definition (again, there are no known previous state residual influences at Time 1). For $t \geq 2$ , $S C o n ( \tau _ { t } )$ will be smaller than $C o n ( \tau _ { t } )$ unless there is no trait influence $[ V a r ( \xi _ { 1 } ) = 0 ]$ . 

The occasion-specificity coefficient $O s p ( \tau _ { t } )$ indicates the proportion of variability in the latent state scores that is due to momentary situation and/or person $\times$ situation interaction effects present at the given measurement occasion (Time t) and is defined as follows: 

$$
\begin{array}{l} O s p (\tau_ {t}) = V a r (\zeta_ {t}) / V a r (\tau_ {t}) \\ = 1 - C o n (\tau_ {t}) \\ \end{array}
$$

For example, a value of $O s p ( \tau _ { t } ) = . 2$ means that $2 0 \%$ of the true state variability is due to situational and/or person $\times$ situation interaction influences at Time t rather than previous trait or previous situational and/or previous person $\times$ situation interaction influences. The $C o n ( \tau _ { t } )$ , TCon(τ ), $S C o n ( \tau _ { t } )$ , and $O s p ( \tau _ { t } )$ coefficients are not directly output by Mplus. In Section 3.4.5, I show how these coefficients can be computed by using the MODEL CONSTRAINT option. 

# 3.4.4 Mplus Application

Below, I show the Mplus specification of a TSE model for four measurement occasions. In this example, I implemented all of the restrictions proposed by Kenny and Zautra (1995; see the discussion above). As I discuss here, this requires the use of the MODEL CONSTRAINT option in Mplus (see Box 2.7 on pages 40–41 for general information on this option). 

```txt
MODEL:  
KSI1 by Y1-Y4@1;  
[KSI1*];  
KSI1* (KSI1_var);  
ZETA1 by Y1@1;  
ZETA1* (ZETA1_var);  
O2 by Y2@1;  
O3 by Y3@1;  
O4 by Y4@1;  
KSI1 with ZETA1@0 O2-O4@0;  
O2 on ZETA1* (delta1);  
O3 on O2* (delta1);  
O4 on O3* (delta1);  
O2-O4* (ZETA_var);  
Y1-Y4* (err_var);  
[Y1@0];  
[Y2* Y3* Y4*];  
MODEL CONSTRAINT:  
NEW(O2_var O3_var O4_var);  
O2_var = (delta1**2) * ZETA1_var + ZETA_var;  
O3_var = (delta1**2) * O2_var + ZETA_var;  
O4_var = (delta1**2) * O3_var + ZETA_var;  
0 = ZETA1_var - O2_var; 
```

In the first line of code KSI1 by Y1-Y4@1;, I specified that all measured variables load onto the Time-1 trait factor $\xi _ { 1 }$ , with each factor loading fixed at 1. The trait factor mean [KSI1*] and variance $\mathrm { K S I 1 ^ { \star } }$ are freely estimated. I labeled the $\xi _ { 1 }$ variance as (KSI1_var), so that this parameter can be used later on in the MODEL CONSTRAINT option. 

The measured variable at Time 1 also has a unit loading on the Time-1 state residual factor $\zeta _ { 1 }$ : ZETA1 by Y1@1;. The variance $V a r ( \zeta _ { 1 } )$ is estimated and labeled ZETA1_var by specifying ZETA1* (ZETA1_var);. Again, the label for this variance parameter is needed to use the parameter later on in the MODEL CONSTRAINT option. Subsequent measured variables have unit loadings on occasion residual factors $O _ { t } ,$ for example: O2 by Y2@1;. The trait factor is uncorrelated with the Time-1 state residual and all occasion residual factors: KSI1 with ZETA1@0 O2-O4@0;. 

The next three lines of code specify the first-order autoregressive process among the latent residual variables using ON statements. The autoregressive slope parameter $\delta _ { \mathrm { l } }$ is held constant across time by specifying the same label (delta1) at the end of each ON statement. The three state residual variances Var(ζ2), $V a r ( \zeta _ { 3 } )$ , and $V a r ( \zeta _ { 4 } )$ are set equal by specifying ${ \mathsf { O } } 2 { - } { \mathsf { O } } 4 ^ { \star }$ (ZETA_var);. The label ZETA_var serves to set the three variances equal so that there is a common state residual variance $V a r ( \zeta )$ for $t \geq 2$ . The label is also required for the MODEL CONSTRAINT specification and makes clear that the residuals of the autoregression (i.e., the residuals of the $O _ { t }$ factors) are the state residuals $\zeta _ { t }$ with common variance Var(ζ). 

Next, I constrained the four measurement error variances to be equal across time by specifying $\mathtt { Y 1 - Y 4 ^ { \star } }$ (err_var);. The measurement intercept at Time 1 is fixed at zero [Y1@0] to identify the trait factor mean $[ \mathrm { K S I 1 ^ { \star } } ]$ . The remaining intercepts are freely estimated: $\begin{array} { r l } { [ \Upsilon 2 ^ { \star } } & { { } \Upsilon 3 ^ { \star } \quad \Upsilon 4 ^ { \star } ] ; } \end{array}$ . (I discussed an alternative mean structure specification in Box 3.7.) 

Finally, the MODEL CONSTRAINT option is needed to implement the restriction $V a r ( \zeta _ { 1 } ) = V a r ( O _ { 2 } ) = V a r ( O _ { 3 } ) = V a r ( O _ { 4 } ) = V a r ( R )$ . This restriction cannot be specified in the regular MODEL command because the variances of the $O _ { t }$ factors are not directly estimated in the model. Rather, the variances $V a r ( O _ { t } )$ are functions of other parameters in the model, namely, Var(ζ ), $\delta _ { \mathrm { l } }$ , and the common state residual variance $V a r ( \zeta )$ : 

$$
\begin{array}{l} V a r \left(O _ {2}\right) = \delta_ {1} ^ {2} \cdot V a r \left(\zeta_ {1} ^ {\prime}\right) + V a r (\zeta) \\ V a r \left(O _ {3}\right) = \delta_ {1} ^ {2} \cdot V a r \left(O _ {2}\right) + V a r (\zeta) = \delta_ {1} ^ {2} \cdot \left[ \delta_ {1} ^ {2} \cdot V a r \left(\zeta_ {1}\right) + V a r (\zeta) \right] + V a r (\zeta) \\ \operatorname {V a r} \left(O _ {4}\right) = \delta_ {1} ^ {2} \cdot \operatorname {V a r} \left(O _ {3}\right) + \operatorname {V a r} (\zeta) = \delta_ {1} ^ {2} \cdot \left\{\delta_ {1} ^ {2} \cdot \left[ \delta_ {1} ^ {2} \cdot \operatorname {V a r} \left(\zeta_ {1}\right) + \operatorname {V a r} (\zeta) \right] + \operatorname {V a r} (\zeta) \right\} \\ + \operatorname {V a r} (\zeta) \\ \end{array}
$$

Recall that in the MODEL command above, I labeled $V a r ( \zeta _ { 1 } )$ as ZETA1 var; $\delta _ { \mathrm { l } }$ as delta1; and Var $( \zeta )$ as ZETA_var. These labels can now be used to define the three occasion residual variances as new parameters in MODEL CONSTRAINT: 

```txt
NEW(O2_var 03_var 04_var);  
O2_var = (delta1**2) * ZETA1_var + ZETA_var;  
O3_var = (delta1**2) * O2_var + ZETA_var;  
O4_var = (delta1**2) * O3_var + ZETA_var; 
```

In the final step, the constraint $V a r ( \zeta _ { 1 } ) = V a r ( O _ { 2 } )$ is implemented, which can be reformulated as $0 = V a r ( \zeta _ { 1 } ) - V a r ( { O } _ { 2 } )$ to be suitable for the MODEL CON-STRAINT option: 

```txt
0 = ZETA1_var - 02_var; 
```

Additional statements for the remaining variances $V a r ( O _ { 3 } )$ and $V a r ( O _ { 4 } )$ are not needed, because it logically follows from the above constraints that these must also be equal to $V a r ( \zeta _ { 1 } )$ . 

Selected Mplus parameter estimates for the illustrative application of the TSE model based on simulated data appear below. In this example, I simulated data based on a large sample size of $N = 2 { , } 0 0 0$ given the instability of the TSE model estimates at smaller sample sizes (see Box 3.8 on page 83 for details). 

```txt
MODEL RESULTS Estimate S.E. Est./S.E. Two-Tailed P-Value .02 ON ZETA1 0.424 0.117 3.633 0.000 O3 ON O2 0.424 0.117 3.633 0.000 O4 ON O3 0.424 0.117 3.633 0.000 Means KSI1 0.022 0.023 0.966 0.334 Intercepts Y1 0.000 0.000 999.000 999.000 Y2 0.300 0.020 14.973 0.000 Y3 0.479 0.023 20.873 0.000 Y4 0.619 0.024 25.736 0.000 
```

<table><tr><td colspan="5">Variances</td></tr><tr><td>KSI1</td><td>0.403</td><td>0.045</td><td>8.999</td><td>0.000</td></tr><tr><td>ZETA1</td><td>0.512</td><td>0.061</td><td>8.347</td><td>0.000</td></tr><tr><td colspan="5">Residual Variances</td></tr><tr><td>Y1</td><td>0.106</td><td>0.091</td><td>1.167</td><td>0.243</td></tr><tr><td>Y2</td><td>0.106</td><td>0.091</td><td>1.167</td><td>0.243</td></tr><tr><td>Y3</td><td>0.106</td><td>0.091</td><td>1.167</td><td>0.243</td></tr><tr><td>Y4</td><td>0.106</td><td>0.091</td><td>1.167</td><td>0.243</td></tr><tr><td>O2</td><td>0.420</td><td>0.096</td><td>4.387</td><td>0.000</td></tr><tr><td>O3</td><td>0.420</td><td>0.096</td><td>4.387</td><td>0.000</td></tr><tr><td>O4</td><td>0.420</td><td>0.096</td><td>4.387</td><td>0.000</td></tr><tr><td colspan="5">New/Additional Parameters</td></tr><tr><td>O2_VAR</td><td>0.512</td><td>0.061</td><td>8.347</td><td>0.000</td></tr><tr><td>O3_VAR</td><td>0.512</td><td>0.061</td><td>8.347</td><td>0.000</td></tr><tr><td>O4_VAR</td><td>0.512</td><td>0.061</td><td>8.347</td><td>0.000</td></tr></table>

The autoregressive slope parameter $\delta _ { \mathrm { 1 } }$ was significant in the application (estimate $= 0 . 4 2 4$ , $S E = 0 . 1 1 7$ , $z = 3 . 6 3 3$ , $p < . 0 0 1$ ; the true population value of $\delta _ { \mathrm { 1 } }$ was 0.5). Recall that $\delta _ { \mathrm { l } }$ is equal to the correlation $\phi$ between adjacent latent residual variables in this case because I implemented the constraint $V a r ( \zeta _ { 1 } ) =$ $V a r ( O _ { 2 } ) = V a r ( O _ { 3 } ) = V a r ( O _ { 4 } ) = V a r ( R )$ . A correlation of $\phi = . 4 2 4 $ indicates a moderate amount of short-term stability (carryover effects). Given the large sample size, the estimated SE of 0.117 in this example can be seen as relatively large given the size of the parameter estimate (true population value $\phi = . 5 )$ ). This is a rather typical finding in applications of the TSE model, which tends to be unstable in many applications (see Box 3.8). 

Another noteworthy result is that the measurement error variance Var(ε) was estimated to be rather small (estimate $= 0 . 1 0 6 )$ ) with a fairly large standard error $\mathit { S E } = 0 . 0 9 1 $ ). The true population value of the measurement error variance was substantially larger (0.2) and was chosen so as to correspond to a population reliability of .8 (recall that I set the population parameters so as to imply a measured variable variance of 1.0). That is, $2 0 \%$ of the observed variable variance in the population model represented error variance, whereas in the analyzed sample the conclusion would have been that the measure had a very small (if any) error variance component. The TSE model thus returned a biased estimate of the error variance parameter, despite the large sample size and a correctly specified model. 

The trait factor (KSI1) and all latent residual variables (ZETA1, O2, O3, and O4) had substantial variance estimates. (The $O _ { t }$ variance estimates are listed under New/Additional Parameters in the Mplus output because they were defined using the MODEL CONSTRAINT option.) Notice that the 

# BOX 3.8. Estimation Problems and Bias in the TSE Model

The TSE model is a complex model that results in estimation problems in many empirical applications. Cole et al. (2005) conducted Monte Carlo simulations of the TSE model to examine its performance across a wide range of conditions. They found that the model is prone to improper solutions (e.g., negative variance estimates) unless both the number of measurement occasions and the sample size are very large. Problems are exacerbated when the autoregressive stability is either low $( \delta _ { 1 }$ close to zero) or high (standardized $\delta _ { \mathrm { l } }$ close to 1). 

In accordance with Cole et al.’s (2005) findings, I encountered various problems when I simulated the data for the illustration of the model in Mplus. Even though I generated the data based on rather favorable conditions (population values implying moderate stability of the state residual factors [latent correlation $\phi = . 5 ]$ as recommended by Cole et al., 2005), many replications in my simulations resulted in nonconverged or improper solutions for sample sizes lower than $N = 1 { , } 0 0 0$ . Even when I generated data for a sample as large as $N =$ 1,500, fairly substantial parameter and standard error (SE) bias still occurred for the variance components in the TSE model. (Parameter and SE estimate bias was a lot worse for the smaller sample size conditions.) In my simulations, trait and measurement error variances tended to be underestimated, whereas the latent residual variances tended to be overestimated. The autoregressive coefficient $\delta _ { 1 }$ showed relatively small parameter and SE estimate bias; however, this parameter still showed large average SEs, even at $N = 1 { , } 5 0 0$ . Large SEs can indicate instability in the estimation. Moreover, large SEs lead to a reduction in statistical power, which can also be problematic in empirical applications. Based on their extensive simulations, Cole et al. (2005) recommended using the TSE model only when both the number of measurement occasions and the sample size are very large. Even in those situations, parameters may be biased or show large standard errors. LST models with autoregression that use multiple indicators per measurement occasions tend to produce more stable results. Multiple- indicator LST models with and without autoregressive effects are discussed in Chapter 5. 

variances Var $( \zeta _ { 1 } )$ , Var $( O _ { 2 } )$ , $V a r ( O _ { 3 } )$ , and $V a r ( O _ { 4 } )$ were all estimated to the same value of $V a r ( R ) = 0 . 5 1 2$ $S E = 0 . 0 6 1$ , $z = 8 . 3 4 7$ ). This confirms that this portion of the desired model restrictions was correctly implemented. 

Although the trait factor variance (estimate $= 0 . 4 0 3$ , $S E = 0 . 0 4 5$ ) was very close to its true population value of 0.4 with a small SE, the common residual variance $V a r ( R ) = 0 . 5 1 2$ was substantially positively biased relative to its true population value of 0.4 (and also had a slightly larger SE). Taken together, the results indicate that the TSE model in this example estimated the amount of trait variance adequately but underestimated the amount of measurement error variance and overestimated the amount of latent residual variance. 

The trait factor mean was estimated to be $E ( \xi _ { 1 } ) = 0 . 0 2 2$ . The intercepts were estimated to be $\delta _ { 0 2 } = 0 . 3$ , $\delta _ { 0 3 } = 0 . 4 7 9$ , and $\delta _ { \scriptscriptstyle 0 4 } = 0 . 6 1 9$ . All intercepts were statistically significant $( p \mathrm { { ' s } } < . 0 0 1 )$ , indicating a significant increase in the means relative to Time 1. Below I present the $R ^ { 2 }$ estimates from the completely standardized solution (STDYX): 

<table><tr><td>STANDARDIZED MODEL</td><td>RESULTS (STDYX</td><td colspan="2">Standardization)</td><td>Two-Tailed</td></tr><tr><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>P-Value</td></tr><tr><td>R-SQUARE</td><td></td><td></td><td></td><td></td></tr><tr><td>Observed</td><td></td><td></td><td></td><td>Two-Tailed</td></tr><tr><td>Variable</td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>P-Value</td></tr><tr><td>Y1</td><td>0.897</td><td>0.089</td><td>10.110</td><td>0.000</td></tr><tr><td>Y2</td><td>0.897</td><td>0.089</td><td>10.110</td><td>0.000</td></tr><tr><td>Y3</td><td>0.897</td><td>0.089</td><td>10.110</td><td>0.000</td></tr><tr><td>Y4</td><td>0.897</td><td>0.089</td><td>10.110</td><td>0.000</td></tr><tr><td>Latent</td><td></td><td></td><td></td><td>Two-Tailed</td></tr><tr><td>Variable</td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>P-Value</td></tr><tr><td>O2</td><td>0.180</td><td>0.099</td><td>1.816</td><td>0.069</td></tr><tr><td>O3</td><td>0.180</td><td>0.099</td><td>1.816</td><td>0.069</td></tr><tr><td>O4</td><td>0.180</td><td>0.099</td><td>1.816</td><td>0.069</td></tr></table>

It can be seen that the common reliability estimate $[ R e l ( Y ) = . 8 9 7 ]$ for the measured variable indicated that at each time point, $8 9 . 7 \%$ of the variability in the measured scores were due to true individual differences between people, whereas the remaining $1 0 . 3 \%$ were due to random errors of measurement. This shows us that the measure in this example was highly reliable. Note, however, that reliability was positively biased, as discussed earlier. Estimated $R ^ { 2 }$ values for the latent $O _ { t }$ variables (.18) indicated that $1 8 \%$ of the variability in $O _ { t }$ scores was accounted for by the previous occasion residual variable $\langle \zeta _ { 1 }$ or $O _ { t - 1 } )$ at each time point. Again, this shows that there was a moderate degree of stability between adjacent occasions of measurement. 

# 3.4.5 Computing the Con(τt), TCon(τt), SCon(τt), and $\pmb { \mathrm { o s p } } ( \pmb { \tau } _ { \uparrow } )$ Coefficients in Mplus

One attractive feature of the TSE model is that, in addition to reliability $R e l ( Y _ { t } )$ , it allows computing the $C o n ( \tau _ { t } )$ , TCon(τ ), $S C o n ( \tau _ { t } )$ , and $O s p ( \tau _ { t } )$ coefficients for quantifying proportions of state variability due to current versus previous trait and state residual influences. In Mplus, these coefficients can be computed via the MODEL CONSTRAINT option so that one does not have to calculate them by hand: 

```txt
MODEL CONSTRAINT:  
NEW(TAU_var Con1 Con2 Con3 Con4 TCon SCon1 SCon2 SCon3 SCon4 Osp1 Osp2 Osp3 Osp4);  
TAU_var = KSI1_var + ZETA1_var;  
Con1 = KSI1_var / TAU_var;  
Con2 = (KSI1_var + (delta1**2) * ZETA1_var) / TAU_var;  
Con3 = (KSI1_var + (delta1**4) * ZETA1_var + (delta1**2) * ZETA_var) / Tau_var;  
Con4 = (KSI1_var + ((delta1**3) **2) * ZETA1_var + (delta1**4) * ZETA_var + (delta1**2) * ZETA_var) / Tau_var;  
TCon = KSI1_var / TAU_var;  
SCon1 = 0 / TAU_var;  
SCon2 = (delta1**2) * ZETA1_var / TAU_var;  
SCon3 = ((delta1**4) * ZETA1_var + (delta1**2) * ZETA_var) / Tau_var;  
SCon4 = (((delta1**3) **2) * ZETA1_var + (delta1**4) * ZETA_var + (delta1**2) * ZETA_var) / Tau_var;  
Osp1 = ZETA1_var / TAU_var;  
Osp2 = ZETA_var / TAU_var;  
Osp3 = ZETA_var / TAU_var;  
Osp4 = ZETA_var / TAU_var; 
```

For this purpose, the coefficients are first specified as NEW parameters to be defined in MODEL CONSTRAINT. Subsequently, they are defined using the mathematical formulas presented above. Notice that given the equality constraints on the latent variances, the formulas for computing Con(τt), TCon(τt), $S C o n ( \tau _ { t } )$ , and $O s p ( \tau _ { t } )$ that I presented above are simplified in this example. As a consequence, the state variance TAU_VAR and the trait consistency coefficient TCon are the same for all time points and are defined only once. Below I show the section of the Mplus output that contains the newly defined parameters and coefficients: 

<table><tr><td colspan="5">MODEL RESULTS</td></tr><tr><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-Tailed P-Value</td></tr><tr><td colspan="5">... New/Additional Parameters</td></tr><tr><td>TAU VAR</td><td>0.916</td><td>0.093</td><td>9.837</td><td>0.000</td></tr><tr><td>CON1</td><td>0.440</td><td>0.028</td><td>15.855</td><td>0.000</td></tr><tr><td>CON2</td><td>0.541</td><td>0.060</td><td>8.997</td><td>0.000</td></tr><tr><td>CON3</td><td>0.541</td><td>0.060</td><td>8.997</td><td>0.000</td></tr><tr><td>CON4</td><td>0.541</td><td>0.060</td><td>8.997</td><td>0.000</td></tr><tr><td>TCON</td><td>0.440</td><td>0.028</td><td>15.855</td><td>0.000</td></tr><tr><td>SCON1</td><td>0.000</td><td>0.000</td><td>0.000</td><td>1.000</td></tr><tr><td>SCON2</td><td>0.100</td><td>0.055</td><td>1.812</td><td>0.070</td></tr><tr><td>SCON3</td><td>0.100</td><td>0.055</td><td>1.812</td><td>0.070</td></tr><tr><td>SCON4</td><td>0.100</td><td>0.055</td><td>1.812</td><td>0.070</td></tr><tr><td>OSP1</td><td>0.560</td><td>0.028</td><td>20.143</td><td>0.000</td></tr><tr><td>OSP2</td><td>0.459</td><td>0.060</td><td>7.635</td><td>0.000</td></tr><tr><td>OSP3</td><td>0.459</td><td>0.060</td><td>7.635</td><td>0.000</td></tr><tr><td>OSP4</td><td>0.459</td><td>0.060</td><td>7.635</td><td>0.000</td></tr></table>

The common latent state variance was estimated to be $V a r ( \tau ) = 0 . 9 1 6 .$ . Given that the common measurement error variance was estimated to be $V a r ( \varepsilon ) = 0 . 1 0 6$ , common reliability can be calculated as $R e l ( Y _ { t } ) = 0 . 9 1 6 / ( 0 . 9 1 6 + 0 . 1 0 6 ) = . 8 9 6$ (recall that Mplus gave the observed variable $R ^ { 2 }$ as .897 in the above standard output, which is within rounding error of .896). For Time 1, $C o n ( \tau _ { \mathrm { l } } ) = T C o n ( \tau _ { \mathrm { l } } )$ was estimated to be .44, indicating that $4 4 \%$ of the true score (state) variance at Time 1 can be attributed to trait influences $( \xi _ { 1 } )$ . The remaining $5 6 \%$ of the true state variance were due to situational and/or person $\times$ situation interaction influences at Time 1 ( $\zeta _ { 1 } ; 0 S \mathbb { P 1 } = . 5 6 )$ . Consistency coefficients were higher (Con $= . 5 4 1 \AA$ at Times 2, 3, and 4. 

The larger portion of consistency at these time points was due to trait consistency $( \zeta _ { 1 } ; \mathrm { T C O N } = . 4 4 )$ , whereas the smaller portion of consistency was due to situation consistency (previous $\zeta _ { t }$ ; $\mathtt { S C O N } = . 1 0 \}$ . Within rounding error, $\mathbb { T } \mathbb { C } \mathbb { O N } +$ $\mathrm { S C O N } = \mathrm { C O N }$ , here $. 4 4 + . 1 0 \approx . 5 4 1$ . Occasion specificity for $t \geq 2$ was estimated to be $\tt O S P = . 4 5 9$ , indicating that $4 5 . 9 \%$ of the state variability at Times 2, 3, and 4 were due to situational and/or person $\times$ situation interaction influences at the given time point $( \zeta _ { t } )$ . 

# 3.4.6 Summary

The TSE model addresses one key issue of interest in LST-R theory, which is distinguishing between trait, state residual, and measurement error components in longitudinal studies. Moreover, the model takes into account both long-term 

trait stability and the more short-term carryover (autoregressive) effects of situations. It is well in line with the fundamental idea of LST-R theory, according to which previous situations can alter the individual’s present and future trait scores. The theoretical structure of the TSE model is well in line with the longitudinal course of many social science constructs, which tend to show both a certain degree of stability, and short- and long-term changes across time. 

Despite its theoretical-conceptual appeal, in practice, the TSE model is unfortunately prone to estimation and empirical underidentification problems across a wide range of conditions. This is likely because the model attempts to extract a lot of information from very little data (only one measured variable per time point). The typical problems with the TSE model were also apparent in the simulated data set that I used for illustration of the model, even though I generated data using a population model that did not contain extreme parameters. A large sample size was needed for proper parameter estimates. Nonetheless, a number of latent variance parameters were still biased even in a sample of $N = 2 { , } 0 0 0$ . 

Application of the TSE model is thus recommended only when a researcher has access to a large sample and/or many waves of data (e.g., in large-sample ecological momentary assessment data). Kenny and Zautra (1995) recommended that no fewer than 100 cases and at least six waves of data be used. Even in this case, one should carefully check whether the resulting solution appears trustworthy. First of all, researchers should check for improper solutions (e.g., negative error variance estimates). Furthermore, the parameter estimates and associated standard errors should be of reasonable size given a researcher’s expectations or prior knowledge about a given measure or construct. If they are not, then a solution may not be trustworthy. The Bayesian estimation methods discussed in Chapter 6 may provide more reasonable parameter estimates than maximum likelihood estimation, particularly for applications of the model that are based on suboptimal conditions (Lüdtke, Robitzsch, & Wagner, 2018). 

To date, the best solution to the problems associated with the TSE model in practice appears to be the use of a measurement design with more than one repeatedly measured variable (e.g., more than one item or a multi-item scale that can be used to create item parcels before the analysis). For such designs, multiple-indicator latent state–trait models can be applied that appear to be far less prone to estimation problems due to the availability of more information from the observed data. Moreover, multiple indicator models require less stringent assumptions with regard to the equality (“stationarity”) of certain parameters over time, including the autoregressive parameter $\delta _ { 1 }$ . This is generally advantageous, especially when a researcher has to deal with unequal spacing between time points. I discuss multiple-indicator latent state–trait models with and without autoregression in Chapter 5. 

# 3.5 LATENT GROWTH CURVE MODELS

# 3.5.1 Introduction

In Section 3.3, we saw that latent variables representing true changes across time can be included by reformulating the simplex model as a latent change score model. Another way to examine changes explicitly is by means of socalled latent growth curve (LGC) models. LGC models can be estimated based on single-indicator data. LGC models can be seen as extensions of the random intercept model described in Chapter 2, Section 2.2, which included only a single-trait factor. LGC models add additional factors to the random intercept model that represent different components of trait changes (e.g., linear trait change). 

# 3.5.2 The Linear LGC Model

# 3.5.2.1 Introduction

The starting point in an analysis of LGC models is frequently a model that assumes linear changes across time. In addition to a random intercept factor that reflects true individual differences in trait scores at the onset (Time 1), the model also contains a latent factor that represents individual differences in linear trait changes across time. 

# 3.5.2.2 Model Description

Figure 3.4 shows a linear LGC model. In addition to a random intercept factor $\xi _ { 1 }$ , the model also contains the linear trait-change factor $( \xi _ { 2 } - \xi _ { 1 } )$ . The random intercept factor now reflects individuals’ initial trait scores at Time 1. The “slope” factor $( \xi _ { 2 } - \xi _ { 1 } )$ is properly interpreted as a linear trait-change factor, given that the factor loadings for this factor are fixed to $t - 1$ . Figure 3.5 illustrates the model-implied trait-change process in the linear LGC model. It can be seen that all trajectories are required to follow a straight line in the model. However, individuals do not have to maintain the same rank order on the trait variable, as some people can show high initial scores and decline, whereas others might start low and end up high. In addition, some people may not change at all. 

In summary, the single-indicator linear LGC model can be described by the following measurement equation: 

$$
Y _ {t} = \xi_ {1} + (t - 1) \cdot (\xi_ {2} - \xi_ {1}) + \varepsilon_ {t} \text {f o r a l l} t = 1, \dots , n
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/f6123127cc4c5f00a18cd53681af4024591547b6d8b06805bb54c2b4ec3cc9d8.jpg)



FIGURE 3.4. Path diagram of a linear latent growth curve (LGC) model. $Y _ { t } =$ observed variable; $\xi _ { 1 } = \mathrm { T i m e } { \cdot } 1$ $\xi _ { 1 } =$ (random intercept) trait factor; $( \xi _ { 2 } - \xi _ { 1 } ) =$ latent trait-change (random slope) factor; $\varepsilon _ { t } =$ measurement error variable.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/6bb65c40473acfd8fbc92d408a6d49ffda0bfe1f572beed3d035b9f47d467698.jpg)



FIGURE 3.5. Illustration of possible model-implied trait-change patterns in the linear LGC model for three hypothetical individuals. It can be seen that the model implies linear changes (or no changes) in the trait scores for all individuals.


It can be seen that the linear LGC model simplifies to the random intercept model when $( \xi _ { 2 } - \xi _ { 1 } ) = 0$ (i.e., when there is no trait change). Moreover, when the variance of the slope factor is zero [i.e., $V a r ( \xi _ { 2 } - \xi _ { 1 } ) = 0 ]$ , but the mean of the slope factor differs from zero [i.e., $E ( \xi _ { 2 } - \xi _ { 1 } ) \neq 0 ]$ , the linear LGC model simplifies to a restricted version of the random and fixed intercepts model. In that case, 

$$
Y _ {t} = \xi_ {1} + (t - 1) \cdot E (\xi_ {2} - \xi_ {1}) + \varepsilon_ {t} \mathrm {f o r a l l} t = 1, \dots , n
$$

The term $( t - 1 ) \cdot E ( \xi _ { 2 } - \xi _ { 1 } )$ here is a constant and thus serves as the fixed intercept. In this special case, trait mean changes are allowed but no interindividual differences in trait change. In addition, mean change is restricted to be linear because the fixed intercept in the equation is restricted to be equal to $( t - 1 ) \cdot E ( \boldsymbol { \xi } _ { 2 } - \boldsymbol { \xi } _ { 1 } )$ . 

In summary, the linear LGC model estimates the following parameters: 

•	 the intercept factor mean $E ( \xi _ { 1 } )$ , 

•	 the intercept factor variance $V a r ( \xi _ { 1 } )$ 

•	 the slope factor mean $E ( \xi _ { 2 } - \xi _ { 1 } )$ , 

•	 the slope factor variance $V a r ( \xi _ { 2 } - \xi _ { 1 } )$ 

•	 the intercept and slope factor covariance $C o v [ \xi _ { 1 } , ( \xi _ { 2 } - \xi _ { 1 } ) ]$ , and 

•	 n measurement error variances $V a r ( \varepsilon _ { t } )$ , one for each for each time point $t = 1 .$ $t = 1 , \ldots , n .$ 

Therefore, the model in general has $n + 5$ free model parameters. In our example, we have $4 + 5 = 9$ free parameters and $1 4 - 9 = 5$ df. In Box 3.9, I show how the single-indicator linear LGC model can be defined based on the concepts of LST-R theory. 

# 3.5.2.3 Variance Decomposition and Reliability Coefficient

In the linear LGC model, the observed variable variances can be decomposed as follows: 

$$
\operatorname {V a r} (Y _ {t}) = \left\{ \begin{array}{l} \operatorname {V a r} (\xi_ {1}) + \operatorname {V a r} (\varepsilon_ {1}) \text {f o r} t = 1 \\ \operatorname {V a r} (\xi_ {1}) + (t - 1) ^ {2} \cdot \operatorname {V a r} (\xi_ {2} - \xi_ {1}) + 2 \cdot (t - 1) \cdot \operatorname {C o v} [ \xi_ {1}, (\xi_ {2} - \xi_ {1}) ] \\ \qquad + \operatorname {V a r} (\varepsilon_ {t}) \text {f o r} t \geq 2 \end{array} \right.
$$

A reliability coefficient can then be defined as follows for the linear LGC: 

$$
R e l (Y _ {t}) = \left\{ \begin{array}{l} V a r (\xi_ {1}) / V a r (Y _ {1}) \text {f o r} t = 1 \\ \{V a r (\xi_ {1}) + (t - 1) ^ {2} \cdot V a r (\xi_ {2} - \xi_ {1}) + 2 \cdot (t - 1) \\ \quad \cdot C o v [ \xi_ {1}, (\xi_ {2} - \xi_ {1}) ] \} / V a r (Y _ {t}) \text {f o r} t \geq 2 \end{array} \right.
$$

Notice that since $\xi _ { 1 }$ and $( \xi _ { 2 } \ - \ \xi _ { 1 } )$ can (and often will) be correlated, their covariance $C o v [ \xi _ { 1 }$ , $\left( \boldsymbol { \xi } _ { 2 } - \boldsymbol { \xi } _ { 1 } \right) ]$ has to be taken into account when computing the variance $V a r ( Y _ { t } )$ . Mplus prints the LGC reliability coefficient under R- SQUARE Observed Variable when the standardized solution (STDYX) is requested. 

# BOX 3.9. Defining the Linear LGC Model Based on LST-R Theory

Using the concepts of LST-R theory, we can define a linear LGC model by making the following assumptions: 

1. Linear trait change: $\xi _ { t } = \xi _ { 1 } + ( t - 1 ) \cdot ( \xi _ { 2 } - \xi _ { 1 } )$ for all $t = 1$ , . . . , n. 

2. No situation or person $\times$ situation interaction influences: All latent state residual variables are zero, $\zeta _ { t } = \zeta _ { s } = 0$ for all t, $s = 1 , \ldots , n$ . 

3. Linear independence of latent trait-change and error variables: $C o v [ ( \xi _ { 2 } - \xi _ { 1 } )$ $\boldsymbol { \varepsilon } _ { t } ] = 0$ for all $t = 1 , \ldots , n$ $t = 1$ . 

The first assumption leads to the structural equation in the linear LGC model, according to which each trait variable is a function of the initial trait at Time 1 plus linear trait change. The second assumption implies that there are no situation or person $\times$ situation interaction effects and is equivalent to the second assumption made in all single- factor models described in Chapter 2. 

Recall the basic LST-R measurement equation $\begin{array} { r } { Y _ { t } = \xi _ { t } + \zeta _ { t } + \varepsilon _ { t } . } \end{array}$ Based on Assumption 2, this equation here simplifies to $Y _ { t } = \xi _ { t } + \varepsilon _ { t } .$ . Replacing $\xi _ { t }$ by $\xi _ { 1 } +$ $( t - 1 ) \cdot ( \xi _ { 2 } - \xi _ { 1 } )$ leads to the measurement equation in the linear LGC model. 

The third assumption means that measurement error variables are not allowed to correlate with the linear slope factor. Notice that the intercept factor $\xi _ { 1 }$ is also uncorrelated with all error variables $\varepsilon _ { t } ,$ as trait variables by definition do not correlate with present or future error variables in LST-R theory (see Chapter 1, Box 1.2). 

# 3.5.2.4 Mplus Application

For the illustrative application in Mplus, I simulated data for $N = 3 0 0$ individuals whose hypothetical IQ scores were recorded on four measurement occasions. There are several ways to specify LGC models in Mplus. The conventional Mplus specification for the linear LGC model is as follows: 

```markdown
MODEL:  
KSI1 by Y1-Y4@1;  
KSI21 by Y2@1 Y3@2 Y4@3;  
[Y1-Y4@0];  
[KSI1 KSI21]; 
```

The first two commands specify the intercept and slope factors with fixed loadings, respectively. The third line of code sets the observed variable intercepts to zero. The fourth line of code requests the estimation of the latent variable means. An alternative, simplified specification is through the Mplus-specific syntax for growth models: 

```txt
MODEL: KSI1 KSI21 | Y1@0 Y2@1 Y3@2 Y4@3; 
```

In this simplified specification, the intercept and slope factors are specified in just one line of code. In this LGC-specific syntax, intercepts do not have to be explicitly fixed to zero, and latent means do not have to be explicitly specified. The program estimates the proper LGC model by default. 

Regardless of which model specification is used, the Mplus PLOT command is useful with LGC models, as it allows plotting the individual growth curves as well as the average model-implied curves. The PLOT command can be specified as follows: 

```txt
PLOT: TYPE = PLOT3;  
SERIES = Y1 (KSI21) Y2 (KSI21) Y3 (KSI21) Y4 (KSI21); 
```

The option TYPE $=$ PLOT3; allows examining individual growth curves as well as the average growth curve. The SERIES option is used to specify the order of the $Y _ { t }$ variables on the $x$ (time) axis. To view plots in the Mplus, one first runs the model and then clicks on Plot View plots in the dropdown menu in the Mplus output window. The “Observed individual values” option allows viewing all individual curves either consecutively or in random order. Figure 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/86ea9d75cd12577d2c38846a888fc0bba5f13facd8e425be3d27a8cc366ce267.jpg)



plus graph showing the observed longitudinal trajectories of 10 randomly se


3.6 shows an example in which 10 randomly selected observed trajectories were plotted. 

The Mplus output file contains the following parameter estimates: 

<table><tr><td colspan="6">MODEL RESULTS</td></tr><tr><td></td><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-Tailed P-Value</td></tr><tr><td>KSI1</td><td>|</td><td></td><td></td><td></td><td></td></tr><tr><td>Y1</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y2</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y3</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y4</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>KSI21</td><td>|</td><td></td><td></td><td></td><td></td></tr><tr><td>Y1</td><td></td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y2</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y3</td><td></td><td>2.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y4</td><td></td><td>3.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td colspan="2">KSI21 WITH KSI1</td><td>-20.119</td><td>5.300</td><td>-3.796</td><td>0.000</td></tr><tr><td colspan="2">Means</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">KSI1</td><td>100.190</td><td>0.903</td><td>110.939</td><td>0.000</td></tr><tr><td colspan="2">KSI21</td><td>2.132</td><td>0.307</td><td>6.938</td><td>0.000</td></tr><tr><td colspan="2">Intercepts</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">Y1</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td colspan="2">Y2</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td colspan="2">Y3</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td colspan="2">Y4</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td colspan="2">Variances</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">KSI1</td><td>219.703</td><td>20.219</td><td>10.866</td><td>0.000</td></tr><tr><td colspan="2">KSI21</td><td>21.627</td><td>2.450</td><td>8.828</td><td>0.000</td></tr><tr><td colspan="2">Residual Variances</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">Y1</td><td>36.928</td><td>7.366</td><td>5.013</td><td>0.000</td></tr><tr><td colspan="2">Y2</td><td>33.435</td><td>4.102</td><td>8.150</td><td>0.000</td></tr><tr><td colspan="2">Y3</td><td>31.982</td><td>4.048</td><td>7.900</td><td>0.000</td></tr><tr><td colspan="2">Y4</td><td>30.387</td><td>7.335</td><td>4.143</td><td>0.000</td></tr></table>

The average initial true IQ level in this application was estimated to be 100.190 (intercept KSI1 factor mean). The average true change in IQ scores was estimated to be 2.132 (linear slope KSI21 factor mean; $S E = 0 . 3 0 7$ , $z = 6 . 9 3 8$ , $p < . 0 0 1 ,$ ). The positive and significant slope factor mean indicates that true IQ scores on average increased over time. Specifically, average IQ socres increased by 2.132 IQ points per unit of time. The two estimated latent means can be used to plot the average true growth curve implied by the model. Mplus provides this plot under Plot View plots Estimated means in the dropdown menu in the Mplus output window (see Figure 3.7). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/0c71a5c04cca26743af414b5c22bbe6bf307b423b59aa29836cc04698a7ec132.jpg)



eans FIGURE 3.7. Mplus graph showing the average latent growth curve based on the estimated intercept and slope factor


The output also reveals substantial variability in both initial true IQ scores (intercept factor variance estimate $= 2 1 9 . 7 0 3$ , $S E = 2 0 . 2 1 9 $ ) and true change (slope factor variance estimate $= 2 1 . 6 2 7$ , $S E = 2 . 4 5 0 \rangle$ . We can thus conclude that there were individual differences in initial IQ scores as well as in how much individuals changed linearly across time. Under KSI21 WITH KSI1, we see that the intercept and slope factor showed a significant negative covariance (estimate $= - 2 0 . 1 1 9$ , $S E = 5 . 3 0 0$ , $z = - 3 . 7 9 6$ , $p < . 0 0 1 ,$ ). In the standardized solution, we can see that this covariance corresponds to a moderatesized negative correlation between intercept and slope of $\Phi = - . 2 9 2$ . The negative relationship between intercept and slope indicates that individuals who started out with larger IQ scores tended to show less of an increase in their IQ scores relative to individuals with initially lower IQ scores. The standardized solution also reveals high reliabilities of the measure at each time point. Between 85.6 and $9 0 . 6 \%$ of the observed score variability in this example was accounted for by the intercept and/or slope factors (R-SQUARE for observed variables). 

<table><tr><td>STANDARDIZED MODEL</td><td>RESULTS (STDYX</td><td colspan="3">Standardization)</td></tr><tr><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-TailedP-Value</td></tr><tr><td>KSI21 WITH KSI1</td><td>-0.292</td><td>0.064</td><td>-4.573</td><td>0.000</td></tr><tr><td>R-SQUARE 
Observed</td><td></td><td></td><td></td><td rowspan="2">Two-TailedP-Value</td></tr><tr><td>Variable</td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td></tr><tr><td>Y1</td><td>0.856</td><td>0.029</td><td>29.957</td><td>0.000</td></tr><tr><td>Y2</td><td>0.857</td><td>0.018</td><td>47.026</td><td>0.000</td></tr><tr><td>Y3</td><td>0.876</td><td>0.017</td><td>52.603</td><td>0.000</td></tr><tr><td>Y4</td><td>0.906</td><td>0.023</td><td>40.105</td><td>0.000</td></tr></table>

# 3.5.2.4 Summary

The linear LGC model can be seen as an extension of the random intercept model presented in Chapter 2, Section 2.2. In contrast to the random intercept model, the linear LGC model allows for trait changes over time as well as interindividual differences in trait changes. However, trait changes are required to follow a straight line for all individuals. When all individuals show perfect stability in their trait scores across time, the linear LGC model reduces to the random intercept model. Extensions of the linear LGC model imply more complex (i.e., nonlinear) patterns of trait changes. Below, I present an LGC model that freely estimates the form of change from the data. 

# 3.5.3 The LGC Model with Unspecified Growth Pattern

# 3.5.3.1 Introduction

Often, the linear LGC model does not fit social science data very well because it assumes that every individual’s true longitudinal trajectory of trait values exactly follows a straight line. This is a fairly restrictive assumption. It seems more plausible that many individuals show true change patterns that are less than perfectly linear. Nonlinear (e.g., quadratic) changes in trait scores can also be examined with single-indicator LGC models. Nonlinear growth functions are described in great detail elsewhere (e.g., Bollen & Curran, 2006; Duncan, Duncan, & Strycker, 2006). Here, I focus on an LGC model that leaves the form of growth unspecified by freely estimating the slope factor loadings. 

# 3.5.3.2 Model Description

A single-indicator LGC model for four time points and an unspecified growth pattern is depicted in Figure 3.8. It can be seen that in this model, the loadings of the observed variables $Y _ { t }$ on the intercept factor $\xi _ { 1 }$ remain fixed at 1.0 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/0f27224859ed73ab36dc181257aafb8244801e270cb26bce49f4a949a9532e08.jpg)



FIGURE 3.8. Path diagram of a latent growth curve (LGC) model with unspecified growth pattern. $Y _ { t } =$ observed variable; $\xi _ { 1 } = \mathrm { T i m e } { \cdot } 1$ (random intercept) trait factor; $( \xi _ { 2 } -$ $\xi _ { 1 } ) =$ latent trait-change factor reflecting trait-change between Time 2 and Time 1; $\lambda _ { t } =$ constant factor loading parameter; $\varepsilon _ { t } =$ measurement error variable.


for all time points as was the case in the linear LGC model. The slope factor $( \xi _ { 2 } - \xi _ { 1 } )$ now has unspecified (freely estimated) loadings $\lambda _ { { _ t } }$ for all observed variables except $Y _ { 1 }$ (by definition, there is no growth at Time 1; therefore, $\lambda _ { 1 }$ is set to 0 as in the linear LGC model) and $Y _ { 2 }$ (one factor loading has to be fixed to identify the metric of the slope factor; therefore, $\lambda _ { 2 }$ is set to 1 as in the linear LGC model). In summary, the single-indicator LGC model with unspecified growth pattern can be described by the following measurement equation: 

$$
Y _ {t} = \xi_ {1} + \lambda_ {t} \cdot (\xi_ {2} - \xi_ {1}) + \varepsilon_ {t} \text {f o r a l l} t = 1, \dots , n, \text {w h e r e} \lambda_ {1} = 0 \text {a n d} \lambda_ {2} = 1
$$

As was the case for the linear LGC model, the LGC model with unspecified growth pattern simplifies to the random intercept model when $( \xi _ { 2 } - \xi _ { 1 } ) =$ 0. When the variance of the slope factor is zero [i.e., $V a r ( \xi _ { 2 } - \xi _ { 1 } ) = 0 ]$ , but the mean of the slope factor differs from zero [i.e., $E ( \xi _ { 2 } - \xi _ { 1 } ) \neq 0 ]$ , the LGC model with unspecified growth pattern simplifies to the random and fixed intercepts model. In that case, 

$$
Y _ {t} = \xi_ {1} + \lambda_ {t} \cdot E (\xi_ {2} - \xi_ {1}) + \varepsilon_ {t} \text {f o r a l l} t = 1, \dots , n
$$

The term $\boldsymbol { \lambda } _ { t } \cdot \boldsymbol { E } ( \boldsymbol { \xi } _ { 2 } - \boldsymbol { \xi } _ { 1 } )$ is a constant and is equivalent to the fixed intercept ${ \bf \mathfrak { a } } _ { t }$ in the random and fixed intercepts model. Mean change in this special case is not restricted to be linear because the constant $\lambda _ { t }$ is freely estimated; hence, the model in this special case is equivalent to the random and fixed intercepts model. 

In summary, the LGC model with unspecified growth pattern estimates the following parameters: 

•	 the intercept factor mean $E ( \xi _ { 1 } )$ , 

•	 the intercept factor variance $V a r ( \xi _ { 1 } )$ , 

•	 the slope factor mean $E ( \xi _ { 2 } - \xi _ { 1 } )$ , 

•	 the slope factor variance $V a r ( \xi _ { 2 } - \xi _ { 1 } )$ , 

•	 the intercept and slope factor covariance $C o \nu [ \xi _ { 1 } , ( \xi _ { 2 } - \xi _ { 1 } ) ] .$ 

• $n - 2$ loadings $\lambda _ { { \scriptscriptstyle t } } ,$ and 

•	 n measurement error variances $V a r ( \varepsilon _ { t } )$ , one for each for each time point $t = 1 , \ldots , n$ . 

# BOX 3.10. Defining the LGC Model with Unspecified Growth Pattern Using the Concepts of LST‑R Theory

Using LST-R theory, we can define the LGC model with unspecified growth pattern by making the following assumptions: 

1. Congenericity of trait change: All trait- change score variables are positive linear functions of the Time-2–Time-1 trait- change variable: $( \xi _ { t } - \xi _ { 1 } ) =$ $\boldsymbol { \lambda } _ { t } \cdot ( \boldsymbol { \xi } _ { 2 } - \boldsymbol { \xi } _ { 1 } )$ , where $\lambda _ { { _ t } }$ is a real constant, $\lambda _ { \mathrm { l } } = 0$ , $\lambda _ { 2 } = 1$ , and $t = 1 , \ldots , n$ . 

2. No situation or person $\times$ situation interaction influences: All latent state residual variables are zero, $\zeta _ { t } = \zeta _ { s } = 0$ for all t, $s = 1 , \ldots , n$ $s = 1$ . 

3. Linear independence of latent trait-change and error variables: $C o v [ ( \xi _ { 2 } - \xi _ { 1 } )$ $\boldsymbol { \varepsilon } _ { t } ] = 0$ for all $t = 1 , \ldots , n$ $t = 1$ . 

Notice that without adding any restrictive assumptions, each trait variable $\xi _ { t }$ can be written as $\boldsymbol { \xi } _ { t } = \boldsymbol { \xi } _ { 1 } + ( \boldsymbol { \xi } _ { t } - \boldsymbol { \xi } _ { 1 } )$ . The first assumption made above allows replacing $( \xi _ { t } - \xi _ { 1 } )$ by $\boldsymbol { \lambda } _ { t } \cdot ( \boldsymbol { \xi } _ { 2 } - \boldsymbol { \xi } _ { 1 } )$ , such that according to the model $\xi _ { t } = \xi _ { 1 } + \lambda _ { t }$ $\cdot \ ( \zeta _ { 2 } - \zeta _ { 1 } )$ . Recall the basic LST measurement equation $Y _ { t } = \xi _ { t } + \zeta _ { t } + \varepsilon _ { t }$ . Based on Assumption 2, this equation here simplifies to $Y _ { t } = \xi _ { t } + \varepsilon _ { t }$ . Replacing $\xi _ { t } \log \xi _ { 1 } + \lambda _ { t }$ ⋅ $( \xi _ { 2 } - \xi _ { 1 } )$ leads to the measurement equation in the LGC model with unspecified growth pattern. 

The linear LGC model can be seen as a special case of the LGC model with unspecified growth pattern in which $\lambda _ { { t } } = t - 1$ . Therefore, when growth is perfectly linear in an empirical application, the $\lambda _ { { } _ { t } }$ coefficients would be estimated to be approximately equal to $t - 1$ in large enough samples. Also notice that for a given time point t, $\lambda _ { { } _ { t } }$ may be estimated to be zero in a given empirical application. In that case, the true trait scores at time t would be equal to the initial trait scores at $t = 1$ . 

The second and third assumptions are the same as in the linear LGC model and imply that there are no situational or person $\times$ situation interaction effects as well as that both the intercept and slope factor are uncorrelated with all measurement error variables. 

Therefore, the model in general has $2 n + 3$ free model parameters. In our example, we have $2 \cdot 4 + 3 = 1 1$ free parameters and $1 4 - 1 1 = 3$ df. In Box 3.10, I show how the LGC model with unspecified growth pattern can be defined based on the concepts of LST-R theory. 

# 3.5.3.3 Variance Decomposition and Reliability Coefficient

The observed variable variances can be decomposed as follows: 

$$
\operatorname {V a r} (Y _ {t}) = \left\{ \begin{array}{l} \operatorname {V a r} (\xi_ {1}) + \operatorname {V a r} (\varepsilon_ {1}) \text {f o r} t = 1 \\ \operatorname {V a r} (\xi_ {1}) + \operatorname {V a r} (\xi_ {2} - \xi_ {1}) + 2 \cdot \operatorname {C o v} [ \xi_ {1}, (\xi_ {2} - \xi_ {1}) ] + \operatorname {V a r} (\varepsilon_ {2}) \text {f o r} t = 2 \\ \operatorname {V a r} (\xi_ {1}) + \lambda_ {1} ^ {2} \cdot \operatorname {V a r} (\xi_ {2} - \xi_ {1}) + 2 \cdot \lambda_ {t} \cdot \operatorname {C o v} [ \xi_ {1}, (\xi_ {2} - \xi_ {1}) ] \\ \qquad + \operatorname {V a r} (\varepsilon_ {t}) \text {f o r} t \geq 3 \end{array} \right.
$$

The reliability coefficient for the LGC model with unspecified growth pattern is given by 

$$
R e l (Y _ {t}) = \left\{ \begin{array}{l} V a r (\xi_ {1}) / V a r (Y _ {1}) \text {f o r} t = 1 \\ \{V a r (\xi_ {1}) + V a r (\xi_ {2} - \xi_ {1}) + 2 \cdot C o v [ \xi_ {1}, (\xi_ {2} - \xi_ {1}) ] \} / V a r (Y _ {2}) \text {f o r} t = 2 \\ \{V a r (\xi_ {1}) + \lambda_ {1} ^ {2} \cdot V a r (\xi_ {2} - \xi_ {1}) + 2 \cdot \lambda_ {t} \cdot C o v [ \xi_ {1}, (\xi_ {2} - \xi_ {1}) ] \} / V a r (Y _ {t}) \\ \text {f o r} t \geq 3 \end{array} \right.
$$

The only difference relative to the linear LGC model is that we now use $\lambda _ { { _ t } }$ instead of $( t - 1 )$ . Mplus will again provide the LGC reliability coefficient under R-SQUARE Observed Variable when the standardized solution (STDYX) is requested. 

# 3.5.3.4 Mplus Application

To illustrate the LGC model with unspecified growth pattern, I again generated four-wave hypothetical IQ data for $N = 3 0 0$ individuals. Using the alternative, simplified LGC specification in Mplus, we can specify the model as follows: 

```txt
MODEL: KSI1 KSI21 | Y1@0 Y2@1 Y3* Y4*; 
```

Notice the asterisks following $Y _ { 3 }$ and $Y _ { 4 }$ , which indicate that the slope factor loadings $\lambda _ { { _ t } }$ pertaining to these variables should be freely estimated. Below are the unstandardized Mplus parameter estimates for this model: 

<table><tr><td colspan="6">MODEL RESULTS</td></tr><tr><td></td><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-Tailed P-Value</td></tr><tr><td>KSI1</td><td>|</td><td></td><td></td><td></td><td></td></tr><tr><td>Y1</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y2</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y3</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y4</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>KSI21</td><td>|</td><td></td><td></td><td></td><td></td></tr><tr><td>Y1</td><td></td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y2</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y3</td><td></td><td>1.720</td><td>0.238</td><td>7.219</td><td>0.000</td></tr><tr><td>Y4</td><td></td><td>2.296</td><td>0.421</td><td>5.450</td><td>0.000</td></tr><tr><td colspan="2">KSI21 WITH KSI1</td><td>-17.129</td><td>9.105</td><td>-1.881</td><td>0.060</td></tr><tr><td>Means</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">KSI1</td><td>100.207</td><td>0.928</td><td>107.998</td><td>0.000</td></tr><tr><td colspan="2">KSI21</td><td>2.040</td><td>0.509</td><td>4.011</td><td>0.000</td></tr><tr><td>Intercepts</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">Y1</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td colspan="2">Y2</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td colspan="2">Y3</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td colspan="2">Y4</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Variances</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">KSI1</td><td>217.776</td><td>22.018</td><td>9.891</td><td>0.000</td></tr><tr><td colspan="2">KSI21</td><td>18.031</td><td>8.234</td><td>2.190</td><td>0.029</td></tr><tr><td>Residual Variances</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">Y1</td><td>38.255</td><td>12.022</td><td>3.182</td><td>0.001</td></tr><tr><td colspan="2">Y2</td><td>33.342</td><td>4.324</td><td>7.711</td><td>0.000</td></tr><tr><td colspan="2">Y3</td><td>31.682</td><td>4.463</td><td>7.099</td><td>0.000</td></tr><tr><td colspan="2">Y4</td><td>31.207</td><td>7.661</td><td>4.074</td><td>0.000</td></tr></table>

It can be seen that the slope factor loadings $\lambda _ { 2 }$ and $\lambda _ { 3 }$ were estimated to be 1.720 and 2.296, respectively. This means that the true change between Time 3 and Time 1 was less than double the amount of change between Time 2 and Time 1 (as would be implied by a linear LGC model). Furthermore, change between Time 4 and Time 1 was less than triple the amount of change between Time 2 and Time 1 (as implied by the linear LGC model). Hence, the general pattern of change did not follow a straight line. 

The intercept factor mean $E ( \xi _ { 1 } )$ was estimated to be 100.207. The slope factor mean $E ( \xi _ { 2 } - \xi _ { 1 } )$ was estimated to be 2.04 and was statistically significant $\mathit { S E } = 0 . 5 0 9$ , $z = 4 . 0 1 1$ , $p < . 0 0 1 ,$ ). This indicated that between Time 1 and Time 2, there was an increase in average IQ scores by about two IQ points that was 

statistically significant. Notice that the slope factor mean in this model only indicates the average rate of change between Time 1 and Time 2. The means of the remaining change factors $( \xi _ { t } - \xi _ { 1 } )$ for $t \geq 3$ can be computed based on the $( \xi _ { 2 } - \xi _ { 1 } )$ mean and the estimated loadings $\lambda _ { { \scriptscriptstyle t } }$ : 

$$
E (\xi_ {t} - \xi_ {1}) = \lambda_ {t} \cdot E (\xi_ {2} - \xi_ {1})
$$

These additional change factor means can be defined as additional parameters in Mplus using the MODEL CONSTRAINT option (see also Box 2.7 on pages 40–41). This has the advantage that one also obtains standard errors and test statistics that can be used to examine the statistical significance of mean changes. In the same way, the mean differences between Time 3 and Time 2 as well as between Time 4 and Time 3 can also be calculated, along with standard errors and tests of significance. 

First, the loadings $\lambda _ { { } _ { t } }$ and the mean $E ( \xi _ { 2 } - \xi _ { 1 } )$ have to be given labels in the regular Mplus MODEL command. For this purpose, the conventional confirmatory factor specification of the LGC model (using BY statements rather than the | symbol) has to be used: 

```txt
MODEL: KSI1 by Y1-Y4@1;  
KSI21 by Y2@1  
Y3* (13)  
Y4* (14);  
[Y1-Y4@0];  
[KSI1];  
[KSI21] (E21);  
KSI21 (V21); 
```

Next, the MODEL CONSTRAINT option is used to define the mean differences as additional (“NEW”) parameters: 

MODELCONSTRAINT:   
NEW(E31E41); $\mathrm{E31} = 13^{*}\mathrm{E21}$ $\mathrm{E41} = 14^{*}\mathrm{E21}$ NEW(E32E43）; $\mathrm{E32} = \mathrm{E31} - \mathrm{E21}$ $\mathrm{E43} = \mathrm{E41} - \mathrm{E21} - \mathrm{E32}$ 

The first set of new parameters (E31 and E41) refers to the mean differences between Time 3 and Time 1 as well as between Time 4 and Time 1, respectively. The second set of new parameters (E32 and E43) refers to the mean differences between Time 3 and Time 2 as well as between Time 4 and 


Time 3. All four mean differences are then output by Mplus as New/Additional Parameters:


<table><tr><td colspan="5">New/Additional Parameters</td></tr><tr><td>E31</td><td>3.510</td><td>0.627</td><td>5.596</td><td>0.000</td></tr><tr><td>E41</td><td>4.684</td><td>0.737</td><td>6.352</td><td>0.000</td></tr><tr><td>E32</td><td>1.470</td><td>0.340</td><td>4.320</td><td>0.000</td></tr><tr><td>E43</td><td>1.174</td><td>0.405</td><td>2.901</td><td>0.004</td></tr></table>

All mean differences are statistically significant $( p ^ { \prime } s \leq . 0 0 4 )$ , indicating that average IQ scores increased significantly between all four time points. Recall that the initial average increase in IQ scores (i.e., the mean difference between Time 2 and Time 1) was 2.04 IQ points. The mean difference E32 indicates that the additional average increase between Time 2 and Time 3 amounted to only 1.47 IQ points (which is less than 2.04). Moreover, the additional increase in true IQ means between Time 3 and Time 4 was only 1.174. Taken together, these findings indicate that after an initial steeper increase, the average growth curve in this example flattened out. This is illustrated in Figure 3.9, which I created based on the estimated intercept and slope factor means. Figure 3.9 shows the model-implied trait means at all four time points. 

Intercept and slope factors showed substantial variance estimates, indicating the presence of interindividual differences in initial IQ trait scores and the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/b4ff3af48994f0916a9b163e3d4d56e0b43a8fb3d9618667c0460f4c53ead6d1.jpg)



FIGURE 3.9. Average latent growth curve in the application of the LGC model with unspecified growth pattern.


amount of change between Time 2 and Time 1. The slope factor variances for the remaining time points, that is, $V a r ( \xi _ { t } - \xi _ { 1 } )$ for $t > 2$ , can again be computed using the MODEL CONSTRAINT option (V21 here indicates the label given to the Time-2–Time-1 slope factor variance in the above MODEL command): 

MODELCONSTRAINT: NEW(V31V41); V31 $=$ (13\*\*2)\*V21; V41 $=$ (14\*\*2)\*V21; 

Notice that the squared loadings are multiplied with the Time-2–Time-1 slope factor variance using the second power $( \star \star 2 )$ to obtain the variances Var(ξt $- \left. \xi _ { 1 } \right.$ for $t \geq 3$ . The output reveals substantial variances also for the remaining change factors $( \xi _ { t } - \xi _ { 1 } )$ for $t \geq 3$ : 

```txt
New/Additional Parameters V31 53.359 14.042 3.800 0.000 V41 95.024 17.010 5.586 0.000 
```

As part of the standardized solution, Mplus outputs the correlation between intercept and slope factor and the indicator reliabilities: 

```txt
STANDARDIZED MODEL RESULTS (STDYX Standardization) Two-Tailed  
Estimate S.E. Est./S.E. P-Value  
KSI21 WITH  
KSI1 -0.273 0.090 -3.041 0.002  
R-SQUARE  
Observed  
Variable Estimate S.E. Est./S.E. P-Value  
Y1 0.851 0.047 18.273 0.000  
Y2 0.858 0.019 46.193 0.000  
Y3 0.870 0.019 44.956 0.000  
Y4 0.882 0.029 30.317 0.000 
```

The correlation between intercept and slope factor was again estimated to be negative $( \phi = - . 2 7 3$ , $S E = 0 . 0 9$ , $z = - 3 . 0 4 1$ , $p = . 0 0 2 \rangle$ ). This indicates that individuals with initially higher IQ scores tended to show smaller increases in their scores compared to individuals who started out with lower IQ scores. Indicator reliabilities were high (range .851 through .882), indicating that less than $1 5 \%$ of the observed IQ score variability reflected measurement error. 

# 3.5.3.5 Summary

LGC models offer another way of examining interindividual differences in change across time. Like the latent change score model, LGC models include difference score variables that directly reflect such interindividual differences in change. However, LGC models use trait-change variables rather than statechange variables. Hence, they implicitly assume that there are no situation or person $\times$ situation interaction influences. 

In the limited simulations that I conducted for the illustration of the LGC model with unspecified growth pattern, I encountered a fairly high rate of nonconverged and improper solutions, whereas no such problems arose in my simulations of the linear growth model. Moreover, the unspecified growth model showed larger standard errors for some of the variance estimates (in particular, the slope factor variance and some of the measurement error variances) than did the linear LGC model. Overall, the unspecified growth model appeared to require a larger number of measurement occasions and/or a larger sample to provide similarly stable estimates as the linear LGC model. This is likely because the unspecified LGC model estimates more parameters than the linear LGC model based on the same amount of information. 

One limitation of all single-indicator LGC models is that they ignore situational and person $\times$ situation interaction influences. As a consequence, they are only appropriate for constructs that are strictly trait-like. For constructs that contain nonzero amounts of state residual variance, LGC models underestimate the reliabilities of the measures (Geiser, Keller, & Lockhart, 2013). Multipleindicator LGC models avoid these limitations. (These models are discussed in Chapter 5 in this volume.) 

# 3.6 CHAPTER SUMMARY

In this chapter, I expanded my discussion of longitudinal models for singleindicator designs to models with more than one latent factor. Table 3.1 provides an overview of the key features of all single-indicator models discussed so far, including the single-factor models presented in Chapter 2. 

For all models, I showed how they can be formulated on the basis of LST-R theory. This helps clarify what types of latent variables are used in the models and what they mean (i.e., are we dealing with state, trait, or state residual latent variables?). For example, in the simplex model (and the equivalent change score model), we consider latent state (and state change) variables, whereas in the linear LGC model, we deal with trait and trait-change latent variables. This 


mary and Comparison of Models for Single‑Indicator Longit


<table><tr><td>Model</td><td>No. of waves needed for identification</td><td>No. of free parameters (4 waves)</td><td>No. of latent factors</td><td>Longitudinal process</td><td>Variance components</td><td>Coefficients</td><td>Autoregressive process?</td></tr><tr><td>Random intercept</td><td>2</td><td>6</td><td>1 trait</td><td>Stable trait</td><td>Trait, measurement error</td><td>Reliability</td><td>No</td></tr><tr><td>Random and fixed intercepts</td><td>2</td><td>9</td><td>1 trait</td><td>Trait with mean change</td><td>Trait, measurement error</td><td>Reliability</td><td>No</td></tr><tr><td>ξ-congeneric</td><td>3</td><td>12</td><td>1 trait</td><td>Trait with mean and variance change</td><td>Trait, measurement error</td><td>Reliability</td><td>No</td></tr><tr><td>Simplex</td><td>4</td><td>12 or 13 [depending on whether Var(εt) or Var(ζt) are set equal across time]</td><td>n states, n-1 state residuals</td><td>First-order autoregressive states</td><td>Previous state, state residual, measurement error</td><td>Reliability, consistency, occasion specificity</td><td>Yes</td></tr><tr><td>Change score</td><td>4</td><td>12 or 13 [depending on whether Var(εt) or Var(ζt) are set equal across time]</td><td>n states, n-1 state change, n-1 state change residuals</td><td>State change</td><td>Previous state, residual change, measurement error</td><td>Reliability, R² (for change score variables)</td><td>Yes (regression of change scores on previous states)</td></tr><tr><td>Trait-state-error</td><td>4</td><td>8</td><td>1 trait, n-1 occasion residuals, n state residuals</td><td>State variability, trait change</td><td>Trait, state residual, occasion residual, measurement error</td><td>Reliability, consistency, trait consistency, situation consistency, occasion specificity</td><td>Yes</td></tr><tr><td>Linear growth</td><td>3</td><td>9</td><td>1 trait, 1 trait change</td><td>Linear trait change</td><td>Trait/ trait change, measurement error</td><td>Reliability</td><td>No</td></tr><tr><td>Unspecified growth</td><td>3</td><td>11</td><td>1 trait, 1 trait change</td><td>Unspecified trait change</td><td>Trait/ trait change, measurement error</td><td>Reliability</td><td>No</td></tr></table>


pt, random and fixed intercepts, and ξ-congeneric models are described in Chapter 2. All other model ar 


clarifies, for instance, that a change score model formulated on the basis of the simplex approach (see Section 3.3) considers changes in latent state scores (which, according to LST-R theory, may contain both trait and situation residual components), whereas a linear LGC model (Section 3.5) deals with changes in latent trait scores. 

The latent (state) change score approach thus confounds changes in traits with changes in situational influences, whereas the LGC approach focuses on trait changes and ignores potential situational influences entirely. In Chapter 5, I present multiple-indicator change and growth curve models that allow disentangling trait-change, state residual, and measurement error components properly. 

By using the concepts of LST-R theory to define the TSE model, the meaning of the latent variables in this model became very clear: the “common” trait in the TSE model is equal to the trait variable at Time 1 $( \xi _ { 1 } )$ , whereas the occasion residuals $O _ { t }$ in this model are a linear function of current and previous latent state residuals $( \zeta _ { t } )$ . The LST approach also clarifies the interpretation of the LGC model with an unspecified growth pattern. The LGC model with an unspecified growth pattern as formulated based on LST-R theory shows that in this model, trait-change score variables for $t > 2$ are linear functions of the Time-2–Time-1 trait-change score variable. 

Models with multiple latent variables as presented in this chapter address some of the limitations of single-factor models presented in Chapter 2. The simplex model offers an intuitive way of looking at longitudinal data in terms of autocorrelated latent states. A first-order autoregressive process is often plausible in social science constructs and allows researchers to study stability and change in a more flexible way. The change process reflected in the simplex model is less restrictive than in any of the single-factor approaches. The simplex model can be reformulated as an equivalent latent state change score model. The state change score model allows researchers to directly study interindividual differences in intraindividual changes across time in terms of latent state difference score variables. 

The simplex model has the downside that it requires at least four measurement occasions to be mathematically identified. Even with four measurement occasions, equality restrictions on either the measurement error variances or the latent residual variances are required for model identification. The model requires a nonzero amount of covariance stability in the construct under study, which is usually present in social science data but may be violated for state-like constructs such as mood when there are long time lags between measurement occasions. The simplex model also does not allow separating trait from state residual variables. 

The TSE model can be understood as an extension of the simplex model that contains trait, state, occasion residual, and measurement error variables. This model assumes that there is both long-term stability in a construct (as represented by the Time-1 trait factor influence) and short-term stability (as represented by the first-order autoregressive process among occasion residual variables). Such a trait–state–autoregressive process is plausible for many constructs in the social sciences (e.g., mood, depression, anxiety, hormone levels). Unfortunately, the TSE model is prone to problems of empirical underidentification, improper parameter estimates, and parameter bias. It can be a tricky model to fit in empirical applications unless both the number of waves and the sample size are large. The TSE model also requires at least four waves of data and equality constraints on certain model parameters to be identified. Multiple-indicator extensions presented in Chapter 5 avoid these problems. 

Single-indicator LGC models take a different and somewhat less intuitive approach to modeling changes across time. In these models, an intercept (initial trait) factor and, in the simplest case, a linear slope (trait-change) factor are considered. Linear LGC models are appropriate for constructs that show linear trait change across time and no situation-specific deviations (no state residual influences). Linear LGC models require at least three measurement occasions to be identified. 

LGC models can also be specified with nonlinear growth components. Additionally, the form of change can be freely estimated from the data by specifying the trait-change factor with free loadings. For measures that contain situation or person $\times$ situation interaction variance, single-indicator LGC models overestimate the measurement error variances and underestimate reliabilities. 

One limitation of all models discussed in this chapter is that they use only a single measured variable per time point. Although this can be practical in studies that cannot administer more than one measure per construct due to time or cost constraints, it comes with significant limitations regarding the statistical modeling. One limitation is that most single-indicator models require identification constraints (e.g., equality restrictions) that are not necessarily plausible in every application. For example, the assumption of equal measurement error variances across time is frequently violated in longitudinal data due to the presence of a so-called Socratic effect (Jagodzinski, Kühnel, & Schmidt, 1987). This effect can lead to more measurement error and/or state variability at the first measurement occasion as compared to subsequent measurement occasions. 

Even when equality constraints are plausible and supported by the data, complex single-indicator models such as the TSE model can be prone to instability and estimation problems. Such problems are likely due to the limited amount of information available with only a single measured variable per time 

point. Theoretically, these issues can be resolved by increasing the sample size and/or the number of measurement occasions— but this is not always possible in practice. 

Another important limitation of single- indicator approaches is that they do not allow researchers to study measurement equivalence (ME) across time in much detail. ME is an important prerequisite for a meaningful interpretation of change (difference) scores across time. In single- indicator approaches, the assumption of strong ME (equal origin and units of measurement) is implicitly 

# BOX 3.11. Using Ordered Categorical Observed Variables as Indicators

All models described in this book assume that the measured variables are continuous (or quasi- continuous), that is, that the scores are on an interval scale (e.g., test or questionnaire item sum scores). The models can also be applied to ordered categorical (ordinal) indicators, including binary variables. In this case, a different estimation method should be used, particularly when the number of ordered response categories is smaller than five (Finney & DiStefano, 2006). 

A detailed presentation of appropriate estimation methods for ordinal indicators in longitudinal studies can be found, for example, in Mehta, Neale, and Flay (2004). The currently most widely recommended approach for ordinal variables uses tetrachoric correlations (for binary) and polychoric correlations (for ordinal) variables as well as mean- and variance- adjusted weighted least squares (WLSMV) estimation of the model parameters. This approach is implemented in Mplus. When binary or ordinal variables are used as indicators in Mplus, the variables should be defined as such in the Mplus VARIABLE command in the input file, for example as follows: 

VARIABLE: NAMES $=$ C1 C2 C3 C4; CATEGORICAL $=$ C1 C2 C3 C4; 

Here, the variables C1 through C4 are listed in both the NAMES and CATEGORICAL statements, indicating that they are binary or ordered categorical (ordinal). The number of categories of the variables does not have to be specified— it is determined automatically by Mplus. When the CATEGORI-CAL option is used in the VARIABLE command, Mplus switches from maximum likelihood estimation (the default estimator with continuous variables) to WLSMV estimation and provides the tetrachoric or polychoric correlations as part of the SAMPSTAT output. For more details on the use of WLSMV estimation in Mplus, see Muthén and Asparouhov (2002). 

made but cannot be tested. In the next chapter, I discuss a basic longitudinal model for multiple indicator designs that can be used to test different levels of ME. In Chapter 5, I describe additional models for multiple indicators per measurement occasion and show how they overcome the limitations of singleindicator models. Box 3.11 provides information on how models can be properly specified for ordered categorical (ordinal) indicators. 

# 3.7 RECOMMENDED READINGS



Bollen, K. A., & Curran, P. J. (2006). Latent curve models: A structural equation per‑ spective. New York: Wiley. 





Cole, D. A., Martin, N. M., & Steiger, J. H. (2005). Empirical and conceptual problems with longitudinal trait–state models: Introducing a trait–state–occasion model. Psychological Methods, 10, 3–20. 





Duncan, T., Duncan, S., & Strycker, L. (2006). An introduction to latent variable growth curve modeling: Concepts, issues, and applications (2nd ed.). Mahwah, NJ: Erl‑ baum. 





Eid, M., Holtmann, J., Santangelo, P., & Ebner-­ Priemer, U. (2017). On the definition of latent state–trait models with autoregressive effects: Insights from LST-R theory. European Journal of Psychological Assessment, 33, 285–295. 





Geiser, C., Keller, B. T., & Lockhart, G. (2013). First- versus second-­ order latent growth curve models: Some insights from latent state–trait theory. Structural Equation Modeling, 20, 479–503. 





Jöreskog, K. G. (1979). Statistical models and methods for analysis of longitudinal data. In K. G. Jöreskog & D. Sörbom (Eds.), Advances in factor analysis and structural equation models (pp. 129–169). Cambridge, MA: Abt. 





Kenny, D. A., & Zautra, A. (1995). The trait–state–error model for multiwave data. Journal of Consulting and Clinical Psychology, 63, 52–59. 





McArdle, J. J. (2009). Latent variable modeling of differences and changes with longi‑ tudinal data. Annual Review of Psychology, 60, 577–605. 



# NOTES

1. Jöreskog (1979a, b) showed that a simplex model for four waves of data $( n = 4 )$ ) can also be identified by constraining $V a r ( \varepsilon _ { \mathrm { l } } ) = V a r ( \varepsilon _ { \mathrm { 4 } } ) = 0$ and freely estimating the remaining measurement error and latent residual variances. This constraint implies that the measure $Y _ { t }$ is perfectly reliable (contains no measurement error variance) at Time 1 and Time 4. I do not discuss this option here because I 

feel that assuming perfect reliability (zero measurement error) is unrealistic in almost all social science applications. 

2. It is unlikely for the $\beta _ { 1 t }$ coefficients to take on negative values in practical applications, given that the state variables represent the same construct at different time points and thus should be positively correlated. From the perspective of model identification, it is required that the $\beta _ { 1 t }$ coefficients be different from zero, regardless of whether they are positive or negative. 

3. In their later work, Kenny and Zautra (2001) relabeled the TSE model as the STARTS model and also changed their labels for the different latent variables in the model. I use the original TSE label because it corresponds more closely to the concepts in Steyer et al.’s (1992, 2015) LST and LST-R theories. Furthermore, I use labels for the latent variables that correspond to their meaning based on the formulation of the model within LST-R theory. 

4. Kenny and Zautra (1995) referred to both the $\zeta _ { 1 }$ and $O _ { t }$ residual variables as “states” and in their later work (Kenny & Zautra, 2001) as “autoregressive trait.” In this book, I explain that from the perspective of LST-R theory, these variables are better described as state residuals $( \zeta _ { t } )$ and occasion residuals $( O _ { t } )$ , respectively. 

5. Notice that for the sake of introducing and formulating the model in line with the concepts of LST-R theory, I deviate slightly from Kenny and Zautra (1995) in my presentation of the measurement model equation. I assume that the intercept (additive constant) is zero at Time 1 $( \delta _ { 0 1 } = 0 )$ ) so that the mean of the trait factor $E ( \xi _ { 1 } )$ can be identified and estimated. In contrast, Kenny and Zautra (1995) described an equivalent specification with an intercept for each time point and assumed that all latent variables (including the trait factor) had means equal to zero. See Box 3.7 for more details regarding alternative mean structure specifications in the TSE model. 

6. Kenny and Zautra’s (1995) original TSE model requires $\delta _ { \mathrm { l } }$ to be time-invariant for model identification. For unequal time intervals between measurement occasions, it is usually not realistic to assume that $\delta _ { \mathrm { l } }$ is time-invariant. Multipleindicator LST models with autoregression presented in Chapter 5 resolve this problem. 

7. As noted by Kenny and Zautra (1995), not all of the restrictions are necessary for the model to be identified, and certain restrictions may not be realistic in many empirical applications. For example, the measurement error variances can be allowed to vary across time, with the model still being identified. Similarly, not all latent residual variances have to be equal for model identification. For simplicity and consistency, I follow Kenny and Zautra’s (1995) assumptions in this book. 

8. This follows because 

$$
\delta_ {1} = \phi_ {2, 1} \cdot \sqrt {\operatorname {V a r} \left(O _ {2}\right)} / \sqrt {\operatorname {V a r} \left(\zeta_ {1}\right)} \text {f o r} t = 2
$$

and 

$$
\delta_ {1} = \phi_ {t, t - 1} \cdot \sqrt {\operatorname {V a r} \left(O _ {t}\right)} / \sqrt {\operatorname {V a r} \left(O _ {t - 1}\right)} \text {f o r} t > 2
$$

where $\boldsymbol { \Phi } _ { t , t - 1 }$ indicates the correlation between adjacent latent residual variables. Under the restriction $V a r ( \zeta _ { 1 } ) = V a r ( O _ { t } ) = V a r ( O _ { s } ) = V a r ( R )$ for all t, $s = 1$ $s = 1 , \ldots , n$ the above equations reduce to 

$$
\delta_ {1} = \phi_ {t, t - 1} \cdot \sqrt {\operatorname {V a r} (R)} / \sqrt {\operatorname {V a r} (R)} = \phi .
$$

9. Eid et al. (2017) used different labels for the coefficients discussed here. Whereas Eid et al. labeled the $T C o n ( \tau _ { t } )$ coefficient as “Predictability by trait1 $( \mathrm { P r e d } _ { \mathrm { t r a i t l } } ) ^ { \mathfrak { n } }$ and the $S C o n ( \tau _ { t } )$ coefficient as “Unpredictability by trait1 $( \mathrm { U P r e d } _ { \mathrm { t r a i t l } } )$ ,” I use the labels “trait consistency” and “situation consistency” here because I feel that these labels make the meaning of the coefficients somewhat clearer. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/d945c6158e9653f131ec871dc56f2b807b46db6395c1c9e4c5ed90de1b1e750b.jpg)


# Latent State Models and Measurement Equivalence Testing in Longitudinal Studies

# 4.1 INTRODUCTION

In Chapters 2 and 3, I discussed various longitudinal models for single-indicator data. These models are useful when a researcher has access to only a single measured variable (indicator) per time point. Unfortunately, single-indicator models have a number of limitations, as I outlined in detail in Chapter 3. One important limitation of single-indicator models is that they do not allow researchers to test for measurement equivalence (ME) across time. The key question in ME testing is whether the psychometric properties of a measure such as the origin, units of measurement, and/or associated measurement error variance remained the same across time (Meredith, 1993; Millsap, 2011; Widaman & Reise, 1997). As I discuss in this chapter, ME is a prerequisite for meaningful across-time comparisons of, for example, latent factor means. With just a single indicator per time point, ME cannot be fully tested. 

Multiple-indicator models allow researchers to conduct detailed tests of ME across time, as I show in this chapter. To illustrate the ME concept in longitudinal studies, I first introduce the so-called latent state (LS) or multistate model as a general longitudinal measurement model for multiple indicators. Subsequently, I show how ME can be tested by comparing different versions of the LS model that differ in terms of various parameter equality constraints. In the last 

part of this chapter, I introduce a more general version of the LS model that can be used when indicators are less than perfectly homogeneous. Both LS model versions can be used for ME testing and as baseline models for subsequently testing more complex models that I discuss in Chapter 5. 

# 4.2 THE LATENT STATE MODEL

# 4.2.1 Introduction

The latent state (LS) or multistate model is a general longitudinal measurement model that is often analyzed in the first step of a longitudinal study with multiple indicators. The LS model allows examining a number of key issues without making overly restrictive assumptions. It can be used to examine measurement-related issues such as the homogeneity (unidimensionality) of indicators and the degree of ME across time. The LS model allows separating random measurement error from true score variance and can thus also be used to study true stability and changes across time. Once a well-fitting version of the LS model has been established, its parameter estimates can guide a researcher’s choice regarding more complex longitudinal models (e.g., latent autoregressive/cross-lagged, latent state–trait, or multiple-indicator latent growth curve [LGC] models; see Chapter 5) that represent more specific hypotheses about the longitudinal course of a construct over time. Many of the subsequently discussed, more complex models can be viewed as special cases or extensions of the LS model. 

# 4.2.2 Model Description

The LS model (see Figure 4.1) can be seen as a longitudinal extension of a basic confirmatory factor analysis (CFA) or classical test theory (CTT) congeneric measurement model (see Box 4.1). In the LS model, observed variables $Y _ { i t }$ (i $=$ indicator, where i, $j = 1$ , . . . , m; $t =$ time point, where t, $s = 1$ , . . . , n) that are supposed to measure a common construct and share the same time point t are used as indicators of a time-specific common latent state variable $\tau _ { t }$ . In line with a congeneric measurement structure known from CTT, different observed variables can have different intercepts ${ \mathfrak { a } } _ { { \mathfrak { i } } t }$ and factor loadings $\lambda _ { i t }$ . This allows for use of indicators that measure the same construct but differ in their metric (i.e., in scaling; e.g., self-report vs. physiological measures of stress; see the detailed discussion on scale setting below). The LS model can be described by the following measurement equation: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/6276a5e179f989f88f798b7f1a71763d6b380cb1eb5dcaeb591dcb697d9d454d.jpg)



FIGURE 4.1. Path diagram of the latent state (LS) model for three observed variable $Y _ { i t }$ that are measured on four time points. $\tau _ { t } =$ common latent state factor; $\varepsilon _ { \mathrm { i } t } =$ measurement error variable; ${ \bf { \alpha } } _ { \mathrm { { i } } t } = { \bf { \alpha } }$ constant (fixed) intercept coefficient; $\lambda _ { _ { i t } } =$ constant factor loading (slope) coefficient. All latent state factors can be correlated.


$$
Y _ {i t} = \alpha_ {i t} + \lambda_ {i t} \cdot \tau_ {t} + \varepsilon_ {i t}
$$

The common factors $\tau _ { t }$ have the same meaning as in the simplex model discussed in Chapter 3. They are latent state variables in the sense of LST-R theory and thus may contain both trait $( \xi )$ and state residual (situation and person $\times$ situation interaction; $\zeta _ { t } )$ components, although these components are not separated in the LS model (latent state–trait models that I describe in Chapter 5 allow separating trait and state residual components). 

Due to the use of multiple indicators, the LS model offers more flexibility than the single-indicator simplex approach (see also Box 4.2). In the LS model, all state variables can be correlated (in the simplex model, the covariance structure of the $\tau _ { t }$ variables is constrained to follow a first-order autoregressive process). Furthermore, each LS variable can have a mean and a variance as a free model parameter. This leads to a saturated latent variable structure, meaning that no restrictions need to be placed on the covariance or mean structure of the latent state variables in the LS model for the model to be mathematically identified. In Box 4.2, I discuss which information is generally used to estimate unknown model parameters in multiple-indicator longitudinal models, including the LS model. 

The most general version of the LS model allows estimating the following parameters: 

•	 n state factor means $E ( \tau _ { t } )$ , 

•	 n state factor variances Var $( \tau _ { t } )$ , 

• $0 . 5 ( { n } ^ { 2 } - { n } )$ state factor covariances $C o v ( \tau _ { t } , \tau _ { s } )$ 

• $n ( m - 1 )$ constant intercepts ${ \sf { a } } _ { _ { i t } }$ (one intercept per measurement occasion is fixed to 0 for identification; see discussion on scaling below), 

• $n ( m - 1 )$ constant factor loadings $\lambda _ { _ { i t } }$ (one loading per measurement occasion is fixed to 1 for identification; see discussion on scaling below), and 

•	 nm measurement error variances $V a r ( \varepsilon _ { i t } )$ 

Therefore, the model in general (i.e., without any invariance restrictions) has $3 n m + 0 . 5 ( n ^ { 2 } - n )$ free model parameters, where n again indicates the total number of measurement occasions and m indicates the total number of measures. For our example with three measures $( m = 3 )$ ) and four time points ${ \mathrm { ( } } n =$ 4), we obtain $3 \cdot 4 \cdot 3 + 0 . 5 \cdot ( 1 6 - 4 ) = 4 2$ free model parameters for the model. With three measures and four time points, we have 90 pieces of known information (see Box 4.2 for details), and so the general version of the LS model in this case has 48 df. 

# 4.2.3 Scale Setting

Notice that the list of LS model parameters above includes only $n ( m - 1 )$ intercepts ${ \mathfrak { a } } _ { _ { \mathrm { i } t } }$ and only $n ( m - 1 )$ factor loadings $\lambda _ { _ { i t } }$ as free parameters (rather than nm 

# BOX 4.1. Relationships Between the LS and CTT Models

As I mentioned in the text, the LS model can be viewed as a longitudinal generalization of the (cross- sectional) congeneric factor model in CTT. For measures that share the same units and/or origin of measurement, more restrictive measurement models can be tested that parallel the tau- equivalence and essential tau- equivalence models of CTT. An LS model with all loadings $\lambda _ { _ { i t } }$ constrained to be equal across measures within each time point (but freely estimated intercepts $\mathbf { a } _ { i t } )$ would represent a longitudinal extension of the essential tauequivalence model. An LS model with both loadings and intercepts constrained to be equal across all measures within each time point would represent a longitudinal extension of the tau- equivalence model. An LS model with loadings, intercepts, and measurement error variances constrained to be equal across all measures within each time point would represent a longitudinal extension of the tau- parallel model. 

# BOX 4.2. Available Information and Model Degrees of Freedom in Multiple‑Indicator Longitudinal Designs

In multiple- indicator longitudinal designs, we have several (repeatedly observed) measures $( m > 1 )$ ) as well as $n > 1$ time points. Multiple- indicator designs therefore allow researchers to draw on a lot more observed information than the single- indicator designs discussed in Chapters 2 and 3. As a consequence, multiple- indicator longitudinal structural equation models tend to be more flexible and more stable (but also more complex) than single- indicator models. 

With m indicators and n time points, we can draw on information from mn measured variables $Y _ { i t } \colon Y _ { 1 1 } , \ldots , Y _ { j s } , \ldots , Y _ { m n }$ js For example, for a three- measure, four-wave design, we have $3 \cdot 4 = 1 2$ measured variables. 

Each measured variable $Y _ { i t }$ has a mean $E ( Y _ { i t } )$ , a variance $V a r ( Y _ { i t } )$ , and covariances $C o v ( Y _ { i t } , Y _ { j s } )$ , (i $, t ) \neq ( j , s )$ , with all other measured variables. As for singleindicator models, the observed $Y _ { i t }$ means, variances, and covariances provide the information that we use to estimate unknown parameters in our models. 

In multiple- indicator longitudinal designs, we have mn observed $Y _ { i t }$ variances, mn observed $Y _ { i t }$ means, and $0 . 5 ( [ m n ] ^ { 2 } - m n )$ observed unique $Y _ { i t }$ covariances to estimate unknown model parameters from. In total, there are 1.5mn $+ ~ 0 . 5 ( m n ) ^ { 2 }$ pieces of available information in multiple- indicator longitudinal designs. Notice that this is a lot more information than in single- indicator designs. Recall from Chapter 2 that with a single indicator and four measurement occasions, we had 14 pieces of available information (4 means, 4 variances, and 6 unique covariances). When we use two indicators instead of one in a four-wave study, we already have 44 pieces of information (8 means, 8 variances, and 28 unique covariances), which is more than three times the amount of information available in the four-wave, single- indicator design. For three indicators and four time points, we have 90 pieces of information (12 means, 12 variances, and 66 unique covariances). The degrees of freedom (df) of a model are calculated in the same way as for single- indicator designs: df = number of pieces of available information – number of estimated model parameters. 

in each case). In other words, one intercept and one factor loading are set to a prespecified value at each measurement occasion. Specifically, I assume here, as well as for subsequent models discussed in Chapter 5, that (1) the intercept of the first indicator is fixed to zero and (2) the loading of the same indicator is fixed to unity at each time point. 

What is the purpose of these restrictions on the intercepts and loadings? In general, latent variables in CFA and structural equation modeling (SEM) such as the $\tau _ { t }$ factors in the LS model have an arbitrary metric. That is, their origin and units of measurement are not per se uniquely defined.1 As a result, their means $E ( \tau _ { t } )$ and variances $V a r ( \tau _ { t } )$ —both of which are model parameters to be estimated—are not uniquely defined either. The above restrictions on the intercepts and loadings ensure that the LS variable scale is identified and that the means and variances of all LS variables can be freely estimated at each time point. Below, I elaborate more on these issues and provide an illustrative example. 

Recall that the congeneric measurement structure in the LS model implies that different measures of a construct may be measured on different scales. That is, different indicators may have different origins (zero points) and/or units of measurement. This is why the measurement model $Y _ { i t } = \mathbf { a } _ { i t } + \boldsymbol { \lambda } _ { i t } \cdot \boldsymbol { \tau } _ { t } + \boldsymbol { \varepsilon } _ { i t }$ includes both intercepts ${ \tt G } _ { i t }$ and factor loadings $\lambda _ { _ { i t } }$ as free parameters to be estimated: In this way, different indicators can differ in their metrics. Differences in the intercepts and/or loadings can be due to the scaling of the indicators (see the example below) or to differences in item (or scale) difficulty and/or differences in discrimination (in the sense of item response theory). 

As an example, consider three different tests that are all supposed to measure a common latent variable labeled “general cognitive abilities.” Assume that one test uses the IQ-score metric $\mathit { M } = 1 0 0$ , $S D = 1 5$ ), the second uses the T-score metric $M = 5 0$ , $S D = 1 0 ,$ ), and the third uses the z-score metric $\boldsymbol { \mathcal { M } } = \boldsymbol { 0 }$ , $S D =$ 1). In this example, should the common latent variable $\tau _ { t }$ measured by these three tests represent latent (i.e., error-free) cognitive abilities in IQ-score metric, T-score metric, or z-score metric? From a statistical point of view, this is arbitrary and thus needs to be defined by the researcher.2 

In order to define the scale of a latent variable in CFA and SEM, different approaches are available. The method pursued in this book is to select a reference variable for which the intercept is fixed to zero and the loading is fixed to unity at each time point (for alternatives, see Box 4.3 as well as Little, 2013). In the example above, this could be, for instance, the test score variable in IQ-score metric. 

Without loss of generality, I (arbitrarily and without loss of generality) assume throughout the remainder of this book that the first indicator $Y _ { 1 t }$ is 

chosen as reference indicator. For this indicator, the intercept is fixed to zero $( \mathbf { \boldsymbol { a } } _ { 1 t } = 0 )$ and the factor loading is fixed to unity $( \lambda _ { 1 t } = 1 )$ at each time point. As a result, the measurement equation for the reference indicator simplifies to $Y _ { 1 t } = \tau _ { t }$ $+ \varepsilon _ { \mathrm { 1 } t } .$ This shows us that each LS variable $\tau _ { t }$ can now be interpreted as the (timespecific) true score variable pertaining to the IQ-score measure at time point $t$ . As a consequence, the latent variable $\tau _ { t }$ in the LS model is measured on the same scale (and has the same mean) as the reference indicator at each time point. 

In the example above, if we decided to select the measure in $I { \mathcal { Q } }$ -score metric to serve as reference, then the common latent variable would be in IQ-score units at each measurement occasion. As is explained in more detail in Box 4.7, the latent means would be directly identified via the observed mean of the IQscore measure: $E ( \tau _ { t } ) = E ( Y _ { 1 t } )$ . If we had selected the z-score measure to serve as reference, then the latent variable would be in z-score units and the mean would correspond to the z-score mean. 

Which measured variable should we select as reference indicator? In the social sciences, an indicator that represents a marker or “gold-standard measure” of the construct is often selected as a reference indicator. For example, researchers may choose an item or scale as reference that has high validity, is particularly well established, and/or is most widely used in their field of study. When a goldstandard measure is chosen, the latent variable’s metric directly corresponds to this measure so that, for example, the latent mean and variance are more easily interpreted. In the above example, IQ may be chosen as “standard metric” because IQ scores are fairly well known and understood by a wide audience. 

In contrast, the T- and z-scales are less well known outside of the scientific context. Therefore, a latent variable with a mean and variance in $T _ { - }$ or z-score metric may be more difficult to communicate. An additional argument against using a z-score variable as reference may be that z-scores can take on the value of zero or be negative. “Zero” or “negative” cognitive ability scores are likely to cause confusion among individuals not familiar with the z-score metric. 

If no variable appears to be particularly outstanding in terms of its substantive representation of the construct, validity, popularity, or scaling, the choice can be made in a purely arbitrary way. This is because selecting a different reference indicator results in a mathematically equivalent model and does not change the overall fit or key results of the model. 

The remaining (nonreference) indicators are compared (“contrasted”) to the reference measure. That is, their intercepts and loadings are interpreted relative to the reference indicator. When the indicators are measured on comparable scales (e.g., different items measuring life satisfaction on a scale from 0 to 10), a researcher can examine whether the remaining indicators have smaller or larger intercepts and/or loadings relative to the reference measure. This may indicate 

# BOX 4.3. Alternative Methods of Defining the Scale of Latent State Variables

Another way to identify the scale of a latent factor is to directly fix the mean and variance of the latent variable and to estimate all intercepts and loadings freely. For example, researchers sometimes choose to fix the means and variances of their latent variables to zero and one, respectively, to define the scale of the latent variables. In this case, the latent variables are standardized (defined to be in z-score metric). In longitudinal studies, this method is typically not recommended because it implies equal factor variances and means across time. 

A third way to identify the scale of latent variables is to impose a more complex constraint on the intercepts and loadings so that, for example, the intercepts sum to zero and the loadings sum to unity for a given latent variable (the so- called effect coding method of scale setting; Little, Slegers, & Card, 2006). Different methods of scaling result in mathematically equivalent models that show identical overall model fit and give the same answers to key questions (e.g., with regard to the reliability of the measures, construct stability and change, or the level of ME as discussed in this chapter). Nonetheless, researchers may prefer one method of scaling over another depending on the specific application, as some methods provide more readily interpretable results in certain situations. Little (2013) discusses different methods for scale setting and their interpretation in detail. 

differences in item (or scale) difficulty and/or discrimination (in the sense of item response theory). 

# 4.2.4 Model Definition Based on LST‑R Theory

In Box 4.4, I show how the LS model can be defined based on the concepts of LST-R theory. 

# 4.2.5 Variance Decomposition and Reliability Coefficient

Using the LS model, a researcher can examine a number of issues of interest in longitudinal data. First of all, the LS model can be used as a longitudinal measurement model to determine the reliabilities $R e l ( Y _ { i t } )$ of the observed variables at each time point. The variance of each observed variable can be decomposed as follows in the LS model: 

$$
V a r \left(Y _ {i t}\right) = \lambda_ {i t} ^ {2} \cdot V a r \left(\tau_ {t}\right) + V a r \left(\varepsilon_ {i t}\right)
$$

# BOX 4.4. Defining the LS Model Based on LST‑R Theory

Using concepts of LST-R theory, the LS model can be defined based on two assumptions.* 

1. Occasion- specific congenericity of latent state variables: All latent state variables measured at the same time point are positive linear functions of each other, such that $\boldsymbol { \tau } _ { i t } = \mathbf { a } _ { i j t } + \boldsymbol { \lambda } _ { i j t } \cdot \boldsymbol { \tau } _ { j t }$ for all indicators $i , j = 1 , \ldots , m$ and time points $t = 1$ , . . . , n. Here, ${ \mathfrak { a } } _ { { \mathfrak { i } } { \mathfrak { t } } }$ and $\lambda _ { i j t }$ denote real constants and $\lambda _ { \mathrm { \it i j t } } > 0$ . 

The assumption of occasion- specific congenericity implies the unidimensionality of the measured variables $Y _ { i t }$ at a given time point in the sense that the latent state variables $\tau _ { i t }$ and $\tau _ { j t }$ underlying two measures $Y _ { i t }$ and $Y _ { j t }$ are assumed to be perfectly positively correlated (they differ only by an additive and a multiplicative constant). 

The assumption of occasion- specific congenericity of the latent state variables can be formulated in an alternative, equivalent way as follows: 

$$
\tau_ {i t} = \alpha_ {i t} + \lambda_ {i t} \cdot \tau_ {t}
$$

where ${ \bf \mathfrak { a } } _ { { \mathrm { i } } t }$ and $\lambda _ { i t }$ denote real constants and $\lambda _ { i t } > 0$ . In words, each (indicatorspecific) latent state variable is a perfect linear function of a common latent state factor $\tau _ { t }$ . By arbitrarily choosing one variable as reference indicator (e.g., using the first measure $Y _ { 1 t }$ as reference), setting the intercept for this variable to zero (e.g., $\mathbf { a } _ { 1 t } = 0 .$ ) and the loading for the same variable to unity (e.g., $\lambda _ { _ { 1 t } } = 1 \mathrm { \Delta }$ ), the common latent state factor is uniquely defined as $\tau _ { t } \equiv \tau _ { 1 t } .$ Its mean and variance can be identified, provided there are at least two indicators measured on at least two time points and the latent state factors are substantially correlated with at least one other latent state factor or external variable in the model (with more than two indicators, the state factors do not have to be correlated for the model to be identified). By replacing $\tau _ { { \mathrm { i } } t }$ by ${ \bf a } _ { i t } + \boldsymbol { \lambda } _ { i t } \cdot \boldsymbol { \tau } _ { t }$ in the basic LST-R decomposition of observed variables into state plus error $( Y _ { i t } = \tau _ { i t } + \varepsilon _ { i t } )$ , we obtain the LS measurement equation $Y _ { i t } = \mathbf { a } _ { i t } + \boldsymbol { \lambda } _ { i t } \cdot \boldsymbol { \tau } _ { t } + \varepsilon _ { i t }$ . In Section 4.3, I present a less restrictive version of the LS model that relaxes the assumption of unidimensionality to some extent to allow for indicator- specific (method) effects, which are frequently observed in longitudinal data. 

(continued on page 122) 

2. Linear independence of state and error variables: $C o \nu ( \tau _ { t } , \varepsilon _ { i s } ) = C o \nu ( \varepsilon _ { i t } , \varepsilon _ { j t } ) =$ 0 for all t, $s = 1$ , . . . , n and $i \neq j$ . 

The second assumption (uncorrelated latent states and errors) means that latent state variables are not allowed to correlate with any error variables and that error variables are not allowed to correlate with other error variables pertaining to different measures i and $j$ within the same time point t (all measurement error variables pertaining to different time points t and s are by definition uncorrelated in LST-R theory, see Chapter 1, Box 1.2). 

The $R e l ( Y _ { i t } )$ coefficient can then be computed as the proportion of variability in a measure that is accounted for by the corresponding common state factor: 

$$
\begin{array}{l} R e l \left(Y _ {i t}\right) = \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} \left(\tau_ {t}\right) / \operatorname {V a r} \left(Y _ {i t}\right) \\ = 1 - \left[ \operatorname {V a r} \left(\varepsilon_ {i t}\right) / \operatorname {V a r} \left(Y _ {i t}\right) \right] \\ = (\lambda_ {i t} ^ {S}) ^ {2} \\ \end{array}
$$

where $( \lambda _ { i t } ^ { S } ) ^ { 2 }$ indicates the squared standardized factor loading of $Y _ { i t }$ . This parallels reliability calculations in the congeneric measurement model of CTT; however, the LS model allows estimating the reliability of each measure at each time point. This can help researchers in determining whether the precision of measurement changes across time.3 When the standardized solution (STDYX) is requested, Mplus prints the $R e l ( Y _ { i t } )$ coefficient under R- SQUARE Observed variable in the output. 

# 4.2.6 Testing ME across Time

One strength of the LS model is that it allows us to test various levels of ME across time. ME refers to whether a measured variable is connected to its timespecific latent state variable with the same factor loading, intercept, and/or measurement error variance on different measurement occasions. ME is a prerequisite for meaningful across- time comparisons of, for example, latent state variable means. In Box 4.5, I discuss four levels of ME that can be distinguished. Subsequently, I explain which level of ME is typically desirable in longitudinal studies and I show how ME can be formally tested with the LS model. 

In practice, researchers typically aim for a restricted version of the LS model in which at least strong ME (see Box 4.5) is established. Under strong ME, the intercepts ${ \mathfrak { a } } _ { _ { \mathrm { i } t } }$ and factor loadings $\lambda _ { { _ { i t } } }$ are set equal across time for the same 

# BOX 4.5. Levels of ME According to Widaman and Reise (1997)

Widaman and Reise (1997) distinguished between four levels of ME (a.k.a. measurement invariance): 

1. Configural invariance: The same number of factors are present at each time point, and the same variables load onto the same factors (same loading pattern) across time. No parameters are restricted to be exactly equal across time, except for the reference indicator, which has its intercept fixed at 0 and its loading fixed to 1 at each time point. This is the LS model version presented in the text. 

2. Weak invariance: In addition to configural invariance, factor loadings remain the same across time for a given observed variable: $\lambda _ { _ { \mathrm { i } t } } = \lambda _ { _ { \mathrm { i } s } } = \lambda _ { _ { \mathrm { i } } }$ for all t, $s = 1 , \ldots , n .$ . 

3. Strong invariance: In addition to equal loadings, intercepts ${ \mathbf { \boldsymbol { a } } } _ { i t }$ also remain the same across time for a given observed variable: $\mathbf { a } _ { i t } = \mathbf { a } _ { i s } = \mathbf { a } _ { i }$ for all t, $s = 1 , \ldots , n$ . 

4. Strict invariance: In addition to equal loadings and intercepts, measurement error variances $V a r ( \varepsilon _ { i t } )$ also remain the same across time for a given observed variable: $V a r ( \varepsilon _ { i t } ) = V a r ( \varepsilon _ { i s } ) = V a r ( \varepsilon _ { i } )$ for all t, $s = 1 , \ldots , n$ $s = 1$ . 

measured variable. Strong ME is desirable because this condition ensures scale invariance (equal origin and units of measurement) across time. Scale invariance makes it possible to meaningfully compare the latent state factor means and variances across measurement occasions. Without ME, differences in latent state factor means or variances across occasions may be due to changes in measurement (observed variable) properties rather than true changes in latent variables. 

How can ME be tested? The different levels of ME described in Box 4.5 correspond to nested LS models. That is, LS models imposing weak, strong, and strict ME are all special (restricted) cases of the configural LS model. Moreover, the more restricted models are nested within each other. For example, the strong ME model is a special case of the weak ME model. Therefore, the strong ME model is said to be nested within the weak ME model. Because of the nesting of the models, their fit can be directly compared using chi- square difference tests. I provide more details on model nesting and chi- square difference tests in Box 4.6. 

# BOX 4.6. Nested Models and Chi‑Square Difference Testing

The fit of so- called nested models can be directly compared by conducting chi- square difference tests. A model (say Model B) is said to be nested within another model (say Model A) when Model B represents a special case of Model A. “Special case” here means Model B directly follows from Model A by implementing constraints on specific parameters. For example, the weak ME model (Model B) is nested within the configural ME model (Model A), because the weak ME model has the same structure as the configural ME model, but it contains equality restrictions on the factor loadings. 

In chi- square difference tests, the chi- square value for the less restricted Model A is subtracted from the chi- square value for the more restricted Model B. The same is done for the degrees of freedom (df) of the two models. The difference in chi- square values is then compared to a chi- square distribution, with df equal to the difference in df between the two models. A small $p$ -value (e.g., $p \leq . 0 5 )$ for the chi- square difference value indicates that the more constrained Model B may fit worse than the less constrained Model A. In this case, the hypothesis of a higher level of ME (e.g., weak vs. configural) would be rejected. 

For robust estimation methods (e.g., the Mplus MLR, MLM, and MLMV estimators for non- normal data), special procedures exist in Mplus that take into account so- called scaling correction factors. These procedures are described in detail on the Mplus website at http://statmodel.com). 

Other options for determining the level of ME include comparing the CFI values for different models (e.g., Little, 2013). Often, a difference of .01 between the CFI values for two models is seen as indicating a meaningful difference in fit. However, extensive research supporting the appropriateness of such guidelines is still lacking, and so this approach should be used with caution. 

Under the assumption of weak ME, the number of estimated factor loadings $\lambda _ { i t }$ reduces from $n ( m - 1 )$ to $m - 1$ because each free loading now has to be estimated only once. In our example with three measures and four time points, we have to estimate six parameters less (six fewer loadings) when weak ME restrictions are imposed. Hence, the total number of free parameters in the LS model reduces to 36 with weak ME in our case. Our weak ME version of the LS model thus has 54 df. 

When strong ME is imposed in the LS model, the number of estimated intercepts ${ \bf \mathfrak { a } } _ { i t }$ and factor loadings $\lambda _ { _ { i t } }$ combined reduces from $2 n ( m - 1 )$ to $2 ( m$ – 1). In our example, we have to estimate 12 parameters (6 loadings and 6 

intercepts) less when strong ME restrictions are imposed. The total number of free parameters in the LS model reduces to 30 and our strong ME version of the LS model has 60 df. With strict ME, we would save an additional nm – m parameters because under strict ME, the measurement error variances have to be estimated only once for each indicator (i.e., estimating only m instead of nm measurement error variances). 4 

# 4.2.7 Other Features of the LS Model

The means, variances, and correlations of the LS variables can be examined to study stability and change in a construct across time. Mean differences between LS variables indicate whether on average, true scores increased or decreased across time. Changes in the variances of the LS variables can be studied to find out whether true differences between individuals increased or decreased across time. The correlations between LS variables show to which extent the rank order of individuals remained the same or changed across time. These correlations tell us something about whether the construct under study is more trait-like or more state-like in nature. Stronger correlations point to more trait-like constructs, whereas smaller correlations indicate that constructs are more state-like. 

To illustrate, consider the extreme case in which all n LS variables are perfectly (1.0) correlated. In this case, there is perfect stability of interindividual differences across time (true mean and variance changes across time are still possible). The construct could be described as being perfectly “trait-like,” and the latent state factors $\tau _ { t }$ could be written as a positive linear function of a single common trait factor such that 

$$
\tau_ {t} = \gamma_ {0 t} + \gamma_ {1 t} \cdot \xi
$$

where $\boldsymbol { \gamma } _ { 0 t }$ and $\gamma _ { 1 t }$ denote real constants, $\boldsymbol { \gamma } _ { 1 t } > 0$ , and $\xi$ is a common trait factor in the sense of LST-R theory. The constants $\boldsymbol { \gamma } _ { 0 t }$ and $\gamma _ { 1 t }$ allow for mean and variance differences across time in the states $\tau _ { t }$ . Such a scenario could be realistic for highly stable constructs such as intelligence. 

The other extreme would be LS variables that are uncorrelated. This would indicate that there is no stability at all with regard to interindividual differences. In this case, a construct would be seen as completely “state-like,” and in the sense of LST-R theory, the $\tau _ { t }$ factors would be more appropriately described as state residuals $( \zeta _ { t } )$ . In most actual social science data, LS variables tend to be substantially correlated (usually between .5 and .9), indicating at least some amount of stability of interindividual differences (trait variance) across time. 

# 4.2.8 Mplus Application

For illustration of the LS model, I generated data for a design with three observed variables that were measured on four time points in line with Figure 4.1. The observed variables here refer to $N = 3 0 0$ individuals’ scores on different cognitive ability tests that are all supposed to measure the same construct (e.g., fluid intelligence). I generated the data such that the observed test score variables differed in their metrics to illustrate this feature of the LS model (the model allows for different intercepts ${ \tt a } _ { i t }$ and loadings $\lambda _ { _ { i t } }$ for different variables). 

In line with the example that I introduced earlier in the context of scale setting of the LS variables, I generated the first observed variable $Y _ { 1 t }$ (reference indicator) to be in IQ score metric $\mathit { M } = 1 0 0$ , $S D = 1 5$ ) in the population, similar to many of the data sets that I used in Chapters 2 and 3. In contrast, the second variable $Y _ { 2 t }$ was generated to be in T-score metric $\mathrm { \Delta } M = 5 0$ , $S D = 1 0 ,$ ) in the population, and the third variable $Y _ { 3 t }$ was generated to be in $\mathcal { Z }$ -score metric $( M = 0$ , $S D = 1 \AA$ ). 

I generated the data such that strict ME (see Box 4.5) would hold in the population model. Strict ME means that the measurement intercepts ${ \bf \mathfrak { a } } _ { i t } .$ factor loadings $\lambda _ { i t } ,$ and measurement error variances $V a r ( \varepsilon _ { i t } )$ were constrained to be time-invariant for the same variable in the population LS model from which I generated the data. I first fit the configural ME version of the LS model to a sample drawn from this population model. As explained in Box 4.5, configural ME means that the number of factors and the pattern of factor loadings are assumed to be the same at each time point, but the αit, λit, and $V a r ( \varepsilon _ { i t } )$ parameters are not formally constrained to be time-invariant in this model. The LS model with configural ME can be specified in Mplus by using the following MODEL statement: 

```txt
MODEL:  
TAU1 by Y11 Y21 Y31;  
TAU2 by Y12 Y22 Y32;  
TAU3 by Y13 Y23 Y33;  
TAU4 by Y14 Y24 Y34;  
[Y11@0 Y12@0 Y13@0 Y14@0];  
[TAU1-TAU4*]; 
```

The first four lines of code (by statements) after MODEL: assign the measures to their respective state factors. The factor loadings $\lambda _ { 1 t }$ of the first variable after each by statement (here $Y _ { 1 1 }$ , $Y _ { 1 2 }$ , $Y _ { 1 3 }$ , and $Y _ { 1 4 } )$ are fixed to 1.0 by default in Mplus to set the scale of each state factor. This makes the first variable $Y _ { 1 t }$ the reference variable at each time point. That is, the state factors are set to have the same units of measurement as the first observed variable $Y _ { 1 t }$ (here, $I { \mathcal { Q } }$ -scores). 

The factor loadings of the remaining indicators $Y _ { 2 t }$ and $Y _ { 3 t } )$ are freely estimated at each time point to take into account differences in the units of measurement between indicators (here: $I { \mathcal { Q } }$ -scores vs. $T _ { - }$ and z-scores). 

The fifth line of code sets the intercepts ${ \mathfrak { a } } _ { 1 t }$ of the reference variable $Y _ { 1 t }$ to zero, so that the latent state factor means (sixth line of code) can be identified as well. The remaining intercepts, $\mathbf { \boldsymbol { a } } _ { i t } , i \neq 1$ , are freely estimated to account for differences in the origin of measurement between indicators (e.g., $\mathrm { I Q } = 1 0 0 + 1 5$ ⋅ z). In Box 4.7, I discuss alternative ways to specify and analyze the intercepts and latent means in the LS model. 

The configural ME model fits the data well (see Table 4.1), which is not surprising, given that in the data-generating population model, an even stricter level of ME holds. Below are the unstandardized Mplus parameter estimates for the configural ME version of the LS model: 

<table><tr><td colspan="6">MODEL RESULTS</td></tr><tr><td></td><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-TailedP-Value</td></tr><tr><td>TAU1</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y11</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y21</td><td></td><td>0.628</td><td>0.023</td><td>27.111</td><td>0.000</td></tr><tr><td>Y31</td><td></td><td>0.065</td><td>0.002</td><td>27.904</td><td>0.000</td></tr><tr><td>TAU2</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y12</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y22</td><td></td><td>0.617</td><td>0.022</td><td>27.678</td><td>0.000</td></tr><tr><td>Y32</td><td></td><td>0.062</td><td>0.002</td><td>27.883</td><td>0.000</td></tr><tr><td>TAU3</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y13</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y23</td><td></td><td>0.659</td><td>0.026</td><td>25.767</td><td>0.000</td></tr><tr><td>Y33</td><td></td><td>0.066</td><td>0.003</td><td>26.340</td><td>0.000</td></tr><tr><td>TAU4</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y14</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y24</td><td></td><td>0.620</td><td>0.024</td><td>26.245</td><td>0.000</td></tr><tr><td>Y34</td><td></td><td>0.062</td><td>0.003</td><td>24.359</td><td>0.000</td></tr><tr><td>TAU1</td><td>WITH</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU2</td><td></td><td>185.679</td><td>16.875</td><td>11.003</td><td>0.000</td></tr><tr><td>TAU3</td><td></td><td>175.937</td><td>16.196</td><td>10.863</td><td>0.000</td></tr><tr><td>TAU4</td><td></td><td>180.380</td><td>16.509</td><td>10.926</td><td>0.000</td></tr><tr><td>TAU2</td><td>WITH</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU3</td><td></td><td>187.304</td><td>16.807</td><td>11.144</td><td>0.000</td></tr><tr><td>TAU4</td><td></td><td>184.703</td><td>16.835</td><td>10.971</td><td>0.000</td></tr><tr><td>TAU3</td><td>WITH</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU4</td><td></td><td>179.558</td><td>16.338</td><td>10.990</td><td>0.000</td></tr><tr><td>Means</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TAU1</td><td></td><td>99.690</td><td>0.865</td><td>115.285</td><td>0.000</td></tr><tr><td>TAU2</td><td></td><td>99.882</td><td>0.877</td><td>113.862</td><td>0.000</td></tr><tr><td>TAU3</td><td></td><td>99.952</td><td>0.852</td><td>117.286</td><td>0.000</td></tr><tr><td>TAU4</td><td></td><td>99.958</td><td>0.864</td><td>115.683</td><td>0.000</td></tr></table>

# BOX 4.7. Different Ways to Specify and Analyze the Mean Structure in the LS Model

In the example application of the LS model with configural ME described in the text, I used a reference indicator approach to identify the mean structure of the LS factors at each time point. In the reference approach, one indicator (e.g., $Y _ { 1 t } )$ is used to identify the scale and mean of the LS factors $\tau _ { t }$ by fixing this indicator’s intercept to zero (i.e., $\mathtt { a } _ { 1 t } = 0 \mathtt { . }$ ) and its loading to unity (i.e., $\lambda _ { 1 t } = 1 \mathrm { , }$ ) at each time point. All other intercepts and loadings are freely estimated in the configural ME model. The LS factor means $E ( \tau _ { t } )$ are then given by 

$$
E (\tau_ {t}) = E (Y _ {1 t})
$$

In the main text, I use the same approach for the weak, strong, and strict ME versions of the LS model. 

There are other ways to identify the LS factor means that a researcher might find useful in some cases. In the configural ME model, the LS factor means are arbitrary because there is no formal ME restriction on the loadings or intercepts (except for an arbitrarily chosen reference indicator as described above). An alternative equivalent specification in the configural ME model is therefore to freely estimate all intercepts and to fix all LS factor means to zero (which is the default setting in Mplus). This alternative specification leads to an equivalent solution in the configural ME case. 

With strong ME, the loadings and intercepts are constrained to be timeinvariant so that the LS factors are measured in the same metric (they now have the same origin and units of measurement) at each time point. As a consequence, the LS factor means can be meaningfully compared across time. In the text, I describe how such LS factor mean comparisons can be conducted using the reference indicator approach. An alternative approach in the strong ME case is to (1) fix the loading of one indicator per time point to unity as in the reference approach; (2) estimate all intercepts but constrain them to be equal across time for the same variable; (3) fix one of the LS factor means to zero [e.g., the LS factor mean at the first time point such that $E ( \tau _ { 1 } ) = 0 ]$ ; and (4) estimate all other LS factor means. This specification with one reference time point can be useful because it allows directly comparing the remaining $n - 1$ latent means against a reference mean (recall that n indicates the total number of measurement occasions). The $n - 1$ freely estimated LS factor means represent the difference in latent means relative to the reference time point for which the LS factor mean is set to zero. 

<table><tr><td colspan="5">Intercepts</td></tr><tr><td>Y11</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y12</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y13</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y14</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y21</td><td>-12.639</td><td>2.330</td><td>-5.424</td><td>0.000</td></tr><tr><td>Y22</td><td>-11.727</td><td>2.249</td><td>-5.215</td><td>0.000</td></tr><tr><td>Y23</td><td>-15.822</td><td>2.577</td><td>-6.139</td><td>0.000</td></tr><tr><td>Y24</td><td>-11.904</td><td>2.383</td><td>-4.995</td><td>0.000</td></tr><tr><td>Y31</td><td>-6.474</td><td>0.234</td><td>-27.635</td><td>0.000</td></tr><tr><td>Y32</td><td>-6.172</td><td>0.223</td><td>-27.664</td><td>0.000</td></tr><tr><td>Y33</td><td>-6.645</td><td>0.253</td><td>-26.220</td><td>0.000</td></tr><tr><td>Y34</td><td>-6.221</td><td>0.259</td><td>-24.055</td><td>0.000</td></tr><tr><td colspan="5">Variances</td></tr><tr><td>TAU1</td><td>198.825</td><td>18.385</td><td>10.814</td><td>0.000</td></tr><tr><td>TAU2</td><td>212.699</td><td>18.964</td><td>11.216</td><td>0.000</td></tr><tr><td>TAU3</td><td>190.518</td><td>17.833</td><td>10.683</td><td>0.000</td></tr><tr><td>TAU4</td><td>194.801</td><td>18.341</td><td>10.621</td><td>0.000</td></tr><tr><td colspan="5">Residual Variances</td></tr><tr><td>Y11</td><td>25.501</td><td>3.348</td><td>7.616</td><td>0.000</td></tr><tr><td>Y12</td><td>18.155</td><td>2.954</td><td>6.146</td><td>0.000</td></tr><tr><td>Y13</td><td>27.359</td><td>3.396</td><td>8.056</td><td>0.000</td></tr><tr><td>Y14</td><td>29.184</td><td>3.647</td><td>8.002</td><td>0.000</td></tr><tr><td>Y21</td><td>19.439</td><td>1.961</td><td>9.913</td><td>0.000</td></tr><tr><td>Y22</td><td>21.915</td><td>2.130</td><td>10.289</td><td>0.000</td></tr><tr><td>Y23</td><td>22.330</td><td>2.205</td><td>10.129</td><td>0.000</td></tr><tr><td>Y24</td><td>18.820</td><td>1.918</td><td>9.813</td><td>0.000</td></tr><tr><td>Y31</td><td>0.183</td><td>0.019</td><td>9.504</td><td>0.000</td></tr><tr><td>Y32</td><td>0.220</td><td>0.021</td><td>10.424</td><td>0.000</td></tr><tr><td>Y33</td><td>0.217</td><td>0.022</td><td>10.027</td><td>0.000</td></tr><tr><td>Y34</td><td>0.239</td><td>0.023</td><td>10.323</td><td>0.000</td></tr></table>

The unstandardized model results show that different observed variables differ in their unstandardized factor loadings, intercepts, and measurement error variances. This is expected given the different metrics of the variables (i.e., IQ- vs. T- vs. z-scores). All loadings are statistically significant $( p ^ { \prime } s < . 0 0 1 )$ , indicating that all measures are significantly correlated with the state factors. Results further indicate that the loadings, intercepts, and error variances for the same variable do not differ strongly across time (which also makes sense, given that the data were generated from a population model in which strict ME across time holds for all variables). 

The LS factor means are similar at each time point. However, before we have formally established at least strong ME across time (time-invariant loadings and intercepts), mean differences have to be interpreted with caution. The covariances between LS variables are all statistically significant, indicating 

nonzero stability of interindividual differences with regard to cognitive abilities across time. Standardized covariances (correlations) between LS variables are easier to interpret. Those can be found in the standardized solution (STDYX) given below: 

<table><tr><td colspan="6">STANDARDIZED MODEL RESULTS (STDYX Standardization)</td></tr><tr><td></td><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-TailedP-Value</td></tr><tr><td>TAU1</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y11</td><td></td><td>0.941</td><td>0.009</td><td>104.212</td><td>0.000</td></tr><tr><td>Y21</td><td></td><td>0.895</td><td>0.013</td><td>67.708</td><td>0.000</td></tr><tr><td>Y31</td><td></td><td>0.906</td><td>0.012</td><td>74.166</td><td>0.000</td></tr><tr><td>TAU2</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y12</td><td></td><td>0.960</td><td>0.007</td><td>130.791</td><td>0.000</td></tr><tr><td>Y22</td><td></td><td>0.887</td><td>0.014</td><td>64.181</td><td>0.000</td></tr><tr><td>Y32</td><td></td><td>0.886</td><td>0.014</td><td>64.341</td><td>0.000</td></tr><tr><td>TAU3</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y13</td><td></td><td>0.935</td><td>0.010</td><td>97.507</td><td>0.000</td></tr><tr><td>Y23</td><td></td><td>0.887</td><td>0.014</td><td>63.533</td><td>0.000</td></tr><tr><td>Y33</td><td></td><td>0.891</td><td>0.014</td><td>65.444</td><td>0.000</td></tr><tr><td>TAU4</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y14</td><td></td><td>0.933</td><td>0.010</td><td>93.132</td><td>0.000</td></tr><tr><td>Y24</td><td></td><td>0.894</td><td>0.013</td><td>66.417</td><td>0.000</td></tr><tr><td>Y34</td><td></td><td>0.872</td><td>0.016</td><td>56.155</td><td>0.000</td></tr><tr><td>TAU1</td><td>WITH</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU2</td><td></td><td>0.903</td><td>0.015</td><td>61.449</td><td>0.000</td></tr><tr><td>TAU3</td><td></td><td>0.904</td><td>0.015</td><td>59.933</td><td>0.000</td></tr><tr><td>TAU4</td><td></td><td>0.917</td><td>0.014</td><td>65.957</td><td>0.000</td></tr><tr><td>TAU2</td><td>WITH</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU3</td><td></td><td>0.930</td><td>0.012</td><td>75.586</td><td>0.000</td></tr><tr><td>TAU4</td><td></td><td>0.907</td><td>0.015</td><td>62.312</td><td>0.000</td></tr><tr><td>TAU3</td><td>WITH</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU4</td><td></td><td>0.932</td><td>0.013</td><td>72.917</td><td>0.000</td></tr><tr><td>R-SQUARE</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Observed</td><td></td><td></td><td></td><td></td><td>Two-TailedP-Value</td></tr><tr><td>Variable</td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td></td><td></td></tr><tr><td>Y11</td><td>0.886</td><td>0.017</td><td>52.106</td><td>0.000</td><td></td></tr><tr><td>Y12</td><td>0.921</td><td>0.014</td><td>65.396</td><td>0.000</td><td></td></tr><tr><td>Y13</td><td>0.874</td><td>0.018</td><td>48.753</td><td>0.000</td><td></td></tr><tr><td>Y14</td><td>0.870</td><td>0.019</td><td>46.566</td><td>0.000</td><td></td></tr><tr><td>Y21</td><td>0.801</td><td>0.024</td><td>33.854</td><td>0.000</td><td></td></tr><tr><td>Y22</td><td>0.787</td><td>0.025</td><td>32.091</td><td>0.000</td><td></td></tr><tr><td>Y23</td><td>0.787</td><td>0.025</td><td>31.766</td><td>0.000</td><td></td></tr><tr><td>Y24</td><td>0.799</td><td>0.024</td><td>33.208</td><td>0.000</td><td></td></tr><tr><td>Y31</td><td>0.821</td><td>0.022</td><td>37.083</td><td>0.000</td><td></td></tr><tr><td>Y32</td><td>0.786</td><td>0.024</td><td>32.171</td><td>0.000</td><td></td></tr><tr><td>Y33</td><td>0.794</td><td>0.024</td><td>32.722</td><td>0.000</td><td></td></tr><tr><td>Y34</td><td>0.761</td><td>0.027</td><td>28.077</td><td>0.000</td><td></td></tr></table>

The standardized model results first of all show the standardized loadings (correlations between each observed variable and its corresponding LS variable) under BY. All standardized loadings are fairly large, indicating moderate to high reliabilities of the cognitive ability measures at each time point. The actual reliabilities (squared standardized loadings) can be found under R-SQUARE in the Mplus output. With the reliabilities ranging from .761 to .921, most values are satisfactory. 

The LS factor correlations can be found under WITH and indicate high stability of interindividual differences across time (values between .903 and .932), as would be expected for many cognitive ability constructs. In other words, the construct studied here is clearly more trait-like than state-like. In the next step, we examine restricted versions of the LS model that contain ME constraints reflecting the various levels of ME described in Box 4.5. 

We first test an LS model version with weak ME. In this model, the factor loadings $\lambda _ { i t }$ for identical variables are constrained to be time-invariant. Such equality constraints on the factor loadings are implemented in Mplus as follows: 

```txt
MODEL:  
TAU1 by Y11  
Y21 (12)  
Y31 (13);  
TAU2 by Y12  
Y22 (12)  
Y32 (13);  
TAU3 by Y13  
Y23 (12)  
Y33 (13);  
TAU4 by Y14  
Y24 (12)  
Y34 (13); 
```

It can be seen that loadings of the same variable across time have been given the same label in parentheses after the variable name in the by statement [e.g., (l2) for the loading $\lambda _ { 2 t }$ pertaining to the second variable]. This tells Mplus to hold these loadings constant across time. The loading of the first variable $( \lambda _ { 1 t } )$ does not have to be labeled because it is fixed to 1.0 by default at each time point. As a consequence of being fixed to the same value at each time point, the loading is also time-invariant. The remaining commands for the specification of the intercepts and LS factor means are the same as those in the configural ME model and have therefore been omitted here. 

The weak ME model also fits the data well (see Table 4.1). Again, this is not surprising, given that the data were generated from a population model with an 

even stricter level of ME. The chi-square difference test (see Table 4.1) indicates no significant difference between the configural and weak ME models, $\chi ^ { 2 } \Delta =$ 3.383, $d f = 6$ , $p = . 7 5 9$ . In addition, the Bayesian information criterion (BIC) for model comparisons also indicates that the weak ME model is preferred. (As can be seen in Table 4.1, the BIC value for the weak ME model is smaller than the BIC value for the configural ME model.) 

In the next step, I fit the strong ME model. In the strong ME model, intercepts ${ \tt a } _ { i t }$ are set equal across time in addition to the time-invariant loadings. The strong ME model can be specified in Mplus by adding the following code to the syntax for the weak ME model in the MODEL command: 

```txt
MODEL:  
[ Y21 Y22 Y23 Y24 ] (a2);  
[ Y31 Y32 Y33 Y34 ] (a3); 
```

The intercepts ${ \alpha } _ { 2 t }$ and ${ \bf q } _ { 3 t }$ (pertaining to the indicators $Y _ { 2 t }$ and $Y _ { 3 t } )$ are now also set equal across time by stating the relevant variable names in brackets [] and providing a label in parentheses behind the brackets. Here, the labels 


TABLE 4.1. Goodness‑of‑Fit Statistics for Different Versions of the LS Model


<table><tr><td>Model</td><td>x²</td><td>df</td><td>p</td><td>x²Δ</td><td>dfΔ</td><td>p(x²Δ)</td><td>SRMR</td><td>AIC</td><td>BIC</td></tr><tr><td>Configural ME</td><td>46.807</td><td>48</td><td>.522</td><td></td><td></td><td></td><td>0.011</td><td>17,913</td><td>18,068</td></tr><tr><td>Weak ME</td><td>50.190</td><td>54</td><td>.622</td><td>3.383</td><td>6</td><td>.759</td><td>0.023</td><td>17,904</td><td>18,038</td></tr><tr><td>Strong ME</td><td>51.976</td><td>60</td><td>.760</td><td>1.786</td><td>6</td><td>.938</td><td>0.024</td><td>17,894</td><td>18,005</td></tr><tr><td>Strict ME</td><td>64.003</td><td>69</td><td>.648</td><td>12.027</td><td>9</td><td>.212</td><td>0.029</td><td>17,888</td><td>17,966</td></tr><tr><td>Strict ME, equal LS factor means</td><td>64.462</td><td>72</td><td>.724</td><td>0.459</td><td>3</td><td>.928</td><td>0.029</td><td>17,883</td><td>17,949</td></tr><tr><td>Strict ME, equal LS factor means and variances</td><td>65.515</td><td>75</td><td>.775</td><td>1.053</td><td>3</td><td>.788</td><td>0.034</td><td>17,877</td><td>17,933</td></tr><tr><td>Strict ME, equal LS factor means, variances, and covariances</td><td>73.539</td><td>80</td><td>.682</td><td>8.024</td><td>5</td><td>.155</td><td>0.034</td><td>17,876</td><td>17,912</td></tr></table>


Note. SRMR $=$ standardized root mean square residual; $A I C =$ Akaike’s information criterion; $B I C =$ Bayesian information criterion. The best-fitting model is shown in bold. $R M S E A = 0 . 0 0$ and $C F I =$ 1.00 for all models. 


(a2) and (a3) were chosen for the time-invariant intercepts ${ \mathfrak { a } } _ { 2 }$ and ${ \mathfrak { a } } _ { 3 }$ . Again, the intercepts ${ \mathfrak { a } } _ { 1 t }$ pertaining to the first variable $Y _ { 1 t }$ do not have to be labeled because they are fixed to zero at each time point and hence already are timeinvariant. All remaining commands are the same as for the weak ME model. 

As can be seen in Table 4.1, the strong ME model also fit the data very well, and it did not fit worse than the weak ME model according to the chi-square difference test and BIC. As a consequence, we proceed to the next level of ME, which is strict ME [additionally constraining the measurement error variances $V a r ( \varepsilon _ { i t } )$ to be time-invariant]. The LS model with strict ME can be obtained in Mplus by adding the following additional code to the syntax for the strong ME model in the MODEL command: 

```txt
MODEL: Y11-Y14 (e1); Y21-Y24 (e2); Y31-Y34 (e3); 
```

To set the measurement error variances equal across time, variables with the same index i are listed in the same line and given a label, for example, Y11- Y14 (e1). The strict ME model fit the data well also, and it showed no significant difference in fit relative to the strong ME model. In this case, a researcher would choose the strict ME model for subsequent analyses of the structural (latent variable) parameters, as the strict ME model is the most parsimonious model, and it does not fit worse than other, less parsimonious model versions. 

In the next step, a researcher may test whether LS factor means $E ( \tau _ { t } )$ remained the same across time, that is, whether there is mean stability across time. Constraining the means to be equal across time only requires a slight modification to the line of code that specifies the latent state factor means as shown below: 

```lisp
MODEL:  
[TAU1-TAU4*] (E_TAU); 
```

Here, I added the label (E_TAU) at the end of the line that requests the estimation of the four latent state factor means. This causes Mplus to hold these four means equal across time. The corresponding strict ME model with equal means in our example does not fit worse than the previous strict ME model with freely estimated means (see Table 4.1). Hence, we can conclude that individuals’ average true cognitive ability scores did not change across time. 

Another hypothesis of interest may be that true state variances $V a r ( \tau _ { t } )$ did not change across time. This can be tested by setting the LS factor variances equal across time as follows: 

```txt
MODEL:  
TAU1-TAU4 (VAR_TAU); 
```

As shown in Table 4.1, the strict ME model with equal LS factor means and variances also fit the data well. We can conclude that true individual differences in cognitive abilities also remained constant across time. The strict ME model with equal LS factor variances is a convenient model because it implies equal reliabilities of the same measures across time (i.e., this model implies that there is no change in either the measurement error variances or the true score variances across time). 

The last hypothesis that can be tested is whether LS factor covariances $C o v ( \tau _ { t } , \tau _ { s } )$ , $t \neq s$ , are the same across time (i.e., whether there is the same level of covariance stability at all times). This constraint can be implemented as follows: 

```txt
MODEL:  
TAU1-TAU4 with TAU1-TAU4 (COV_TAU); 
```

The model with time-invariant LS factor covariances also fits the example data well (see Table 4.1). Given that the LS factor variances are also timeinvariant in this model, all six LS factor correlations are equal as well. The corresponding estimated common LS factor correlation is strong in this example (.915). Taken together, this indicates that the cognitive ability construct under study can be classified as a trait construct with minimal state residual (situational) variability. An LST model with a single-trait factor and four-state residual factors at each time point also fits these data very well, as I show in Chapter 5. 

# 4.2.9 Summary

ME is an important prerequisite for a meaningful interpretation of changes in latent variables across time. Strong ME (implying the same origin and units of measurement across time) is often a desirable condition, as it allows for meaningful comparisons of latent variable means and variances across time. In this 

section, I showed how ME across time can be examined by comparing different versions of the LS model. The LS model is a useful starting point in longitudinal analyses that use multiple measures at each time point for multiple reasons. The most general version of the LS model has a saturated (just identified) latent variable (structural) model. In other words, all degrees of freedom in the model stem from the measurement model. The LS model thus allows researchers to study measurement-related issues first before moving on to (potentially complex) latent variable models of change. If the LS model does not fit well, this is typically a sign that the hypothesized measurement model is too restrictive (see the discussion below). 

From a measurement perspective, the model can be seen as a direct extension of the CTT congeneric measurement model for cross-sectional data. Like the congeneric model, the LS model allows testing whether the measures are unidimensional at each time point. Misfit of the LS model may indicate that the indicators measure multiple latent variables rather than a single one at each time point. The model also provides information on indicator reliabilities (measurement precision) at each measurement occasion and allows examining ME across time. 

Aside from measurement-related issues, the LS model can be used to explore the longitudinal course of a construct by estimating and comparing latent state factor means, variances, covariances, and correlations. In this way, a researcher can gather preliminary information with regard to the covariance and mean stability of a construct across time before testing more complex longitudinal models that imply more specific hypotheses with regard to the type of change. In the present example, the estimated latent state factor correlations were all very close to 1.0 and the latent state factor means did not change significantly across time. This shows us that the construct under study exhibited the typical features of a strongly trait-like construct, with high stability of both means and interindividual differences across time. 

One limitation of the basic LS model is that it makes fairly restrictive assumptions with regard to the homogeneity of the measured variables. That is, the assumption of occasion-specific congenericity of latent state variables implies that all measures pertaining to the same time point have perfectly correlated latent states. Furthermore, no residual associations between measures are allowed either at the same time point or across time. This implies the assumption that the latent state factors account for all of the covariances between the measures. This is often unrealistic for social science measures, which tend to show a certain degree of idiosyncrasy. An extension of the LS model that I discuss next addresses this issue. 

# 4.3 THE LS MODEL WITH INDICATOR‑SPECIFIC RESIDUAL FACTORS

# 4.3.1 Introduction

The LS model described above only fits empirical data well when the observed variables are strictly unidimensional. In practice, measured variables frequently contain idiosyncratic aspects due to, for example, specific item wording or content differences. Such “method” or indicator-specific (IS) effects often result in a complex longitudinal covariance structure in which the same measure is more highly correlated with itself across time than with the other measures of the same LS variable (Raffalovich & Bohrnstedt, 1987). An example of how IS effects manifest themselves in an observed variable correlation matrix is provided in Box 4.8. 

# 4.3.2 Model Description

Multiple approaches have been proposed to address the issue of indicator specificity in longitudinal data (e.g., Marsh & Grayson, 1994; Raffalovich & Bohrnstedt, 1987; Sörbom, 1975). Here, I present Eid, Schneider, and Schwenkmezger’s (1999) approach, which uses so-called residual method or IS factors. Their LS-IS approach is in line with LST-R theory and leads to a rather parsimonious extension of the LS model. In the LS-IS approach, one indicator is used as the reference or “marker” indicator, for example, the first indicator $Y _ { 1 t } .$ . The latent state variable for the reference indicator $( \tau _ { 1 t } )$ is contrasted against the remaining latent state variables $( \tau _ { i t } )$ using linear regression analysis (see Box 4.9 for details). For all indicators except the reference indicator, additional $I S _ { i }$ residual factors are included in the model as shown in Figure 4.2. As I explain in detail below, the $I S _ { i }$ factors are allowed to correlate with other $I S _ { i }$ factors, but are uncorrelated with the reference state factors. 

The reference indicator could be a specifically selected variable (i.e., a variable that is known either theoretically or empirically to be a particularly good indicator of the intended construct). For example, the item “I often feel depressed” may have especially high face validity as a measure of depression and/or this variable may show a particularly strong factor loading in a crosssectional factor analysis of a depression scale, making it a “marker indicator” for the depression factor. In cases in which there is no clear marker indicator, one can arbitrarily choose a variable to serve as reference. In this case, sensitivity analyses should be conducted to examine the impact of choosing one reference variable over another. 

# BOX 4.8. Indicator‑Specific Effects in Longitudinal Data

When the same measures are repeatedly administered (as is common in multiple- indicator longitudinal studies), a common pattern observed in the social sciences is that the same variables are more highly correlated with themselves over time than with other measures of the same construct. Below is a hypothetical example correlation matrix that illustrates this typical pattern for a longitudinal design with two measures $( m = 2 )$ ) administered on two time points $( n = 2 )$ . 

<table><tr><td></td><td>Y11</td><td>Y21</td><td>Y12</td></tr><tr><td>Y21</td><td>.83</td><td></td><td></td></tr><tr><td>Y12</td><td>.73</td><td>.62</td><td></td></tr><tr><td>Y22</td><td>.61</td><td>.71</td><td>.85</td></tr></table>

It can be seen that the two measures $Y _ { 1 t }$ and $Y _ { 2 t }$ are highly (.83 and .85, respectively) correlated within the same time points, indicating that they measure a common construct (and/or that they reflect the same situation- specific influences). Across time, the two measures are also substantially (.61 and .62) correlated, indicating that there is a substantial trait component (covariance stability) that is reflected in both measures. Notice that the correlations of the same measure across time (.71 and .73) are stronger than the correlations between different measures. This shows that each measure contains some temporally stable (“trait”) aspects that it does not share with the other measure. Such indicatorspecific effects are not accounted for in the LS model presented in Section 4.2 but can be adequately reflected in the LS-IS model presented in this section. 

Notice also that in this example, the correlations within time points are stronger than the correlations across time points (for both the same and different measures). This indicates that there are both stable (trait) and occasion- specific (situation and/or person $\times$ situation interaction) components to the construct under study. These components can be disentangled with latent state–trait models presented in Chapter 5. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/6e4c0c3b116928fbac8a31e05aff2013eeaf56971815be27609a49466ab0f38d.jpg)



FIGURE 4.2. Path diagram of the latent state model with indicator-specific factors (LS-IS model) for three observed variable $Y _ { i t }$ that are measured on four time points. $\tau _ { 1 t }$ $=$ indicator-specific latent state variable pertaining to the reference indicator $Y _ { 1 t } ;$ $I S _ { \mathrm { { i } } } = { }$ indicator-specific residual factors for non-reference indicators $( \mathrm { i } \neq \mathrm { l } )$ ; $\varepsilon _ { i t } =$ measurement error variable; ${ \bf \mathfrak { a } } _ { \mathrm { i } t } =$ constant (fixed) intercept coefficient; $\lambda _ { { \scriptscriptstyle \mathrm { i } } t } =$ constant factor loading (slope) coefficient. Correlations between $\tau _ { 1 t }$ and $I S _ { i }$ factors are not allowed.


The LS-IS model is depicted as a path diagram in Figure 4.2 for a design with three indicators and four time points. The model contains four reference latent state variables $\tau _ { { \mathrm { l } } t }$ (one for each time point). All measured variables (reference and non-reference) that share the same time point t load onto the proper reference latent state variable $\tau _ { \mathrm { l } t } .$ In addition, the non-reference indicators load onto an indicator-specific residual factor $I S _ { i }$ . Notice that in Figure 4.2, there are two $I S _ { i }$ factors, one for each of the two non-reference indicators. 

In contrast to the state factors $\tau _ { { \mathrm { l } } t }$ which represent time-specific latent variables (there is a separate $\tau _ { { \mathrm { l } } t }$ factor at each measurement occasion), the $I S _ { i }$ factors are time-unspecific (they have no subscript $t$ and variables pertaining to different time points load onto them). The $I S _ { i }$ factors thus capture across-time (residual) covariances of a measured variable with itself that are not reflected in the correlations between state factors $\tau _ { 1 t } .$ In other words, the “unique” stability of interindividual differences in the non-reference indicators is reflected in the variances of the $I S _ { i }$ factors. They can thus be interpreted as “residual trait factors” after accounting for trait variance that is shared with the reference indicator. 

The $I S _ { i }$ factors can be correlated with one another but not with the state 

variables $\tau _ { 1 t } .$ . The correlations between $I S _ { i }$ factors pertaining to different indicators are partial correlations (i.e., correlations between regression residuals, where the influence of the reference state variable $\tau _ { { \mathrm { l } } t }$ has been partialled out). These partial correlations indicate whether the non-reference indicators share part of the unique stability of interindividual differences, that is, stability that they do not share with the reference indicator. 

LS-IS models that use different reference indicators for the same data are not equivalent models. That is, when a researcher chooses a different reference indicator, the overall model fit of the LS-IS model is likely to change at least slightly. Therefore, as noted above, researchers should select a reference indicator based on theoretical, substantive, and/or prior empirical grounds. For example, there may be theoretical reasons to prefer a given measure as a “marker indicator” (e.g., because in theory, a certain measure best represents the construct under study), or previous factor-analytic or item-response theoretical studies may have revealed that a specific measure loads most strongly on the intended factor. In cases in which no marker indicator can be identified, researchers should conduct sensitivity analyses to determine the impact of choosing different measures as reference indicators. 

In addition, the interpretation of the model parameter estimates is always relative to the chosen reference indicator in the LS-IS model. That is, the latent state factors represent true state score variance in the reference indicator. The $I S _ { i }$ factors represent stable variance in the non-reference indicators that is not shared with the reference indicator. The data example that I present later illustrates the proper interpretation of the results in the LS-IS model. In Box 4.10 on page 144, I discuss an alternative way to account for indicator-specific effects in longitudinal data that is based on correlated measurement error variables. 

In summary, the LS-IS model estimates the following parameters: 

•	 n reference state factor means $E ( \tau _ { 1 t } )$ , 

•	 n reference state factor variances $V a r ( \tau _ { 1 t } )$ , 

• $0 . 5 ( { n } ^ { 2 } - { n } )$ reference state factor covariances $C o v ( \tau _ { 1 t } , \tau _ { 1 s } )$ 

• $m - 1$ indicator-specific factor variances Var(ISi), 

• $0 . 5 ( m - 1 ) ( m - 2 )$ indicator-specific factor covariances $C o v ( I S _ { i } , I S _ { j } ) , i \ne$ j, 

• $n ( m - 1 )$ constant intercepts ${ \mathfrak { a } } _ { _ { \mathrm { i } t } }$ (the intercept pertaining the reference indicator is fixed to 0 on each measurement occasion), 

• $n ( m - 1 )$ constant factor loadings $\lambda _ { i t }$ (the loading pertaining the reference indicator is fixed to 1 on each measurement occasion), and 

•	 nm measurement error variances $V a r ( \varepsilon _ { i t } )$ . 

# BOX 4.9. Defining the LS‑IS Model Based on LST‑R Theory

The LS-IS model can be formulated based in LST-R theory as follows. Without loss of generality, let $Y _ { 1 t }$ denote the reference indicator at each time point. For both the reference indicator $Y _ { 1 t }$ and the non- reference indicators $Y _ { i t } ^ { } ,$ , the basic LST-R measurement equation holds at each time point: 

$$
Y _ {i t} = \left\{ \begin{array}{l} \tau_ {1 t} + \varepsilon_ {1 t} \text {f o r} i = 1 \\ \tau_ {i t} + \varepsilon_ {i t} \text {f o r} i \neq 1 \end{array} \right.
$$

In Eid et al.’s (1999) approach, it is assumed that for a given time point t, the latent state variables pertaining to the non- reference indicators are regressed on the latent state variables pertaining to the reference indicator using a linear regression analysis. 

1. Linear regression of non- reference state variables on the reference state variable: 

$$
E (\tau_ {i t} \mid \tau_ {1 t}) = \alpha_ {i t} + \lambda_ {i t} \cdot \tau_ {1 t}
$$

where $E ( \tau _ { i t } \mid \tau _ { \mathrm { l } t } )$ denotes the conditional expectation (regression) of $\tau _ { i t }$ given $\tau _ { \mathrm { l } _ { t } } ,$ and ${ \bf \mathfrak { a } } _ { \mathrm { i } t }$ and $\lambda _ { i t }$ are real constants. In words, we are using the reference state variable $\tau _ { \mathrm { l } t }$ at time $t$ to predict the non- reference state variables $\tau _ { { \mathrm { i } } t }$ that are measured at the same time point through a linear regression analysis. In this regression, ${ \mathbf { \alpha } } _ { i t }$ is the regression intercept (representing the expected value of $\tau _ { i t }$ when $\tau _ { { \mathrm { l } } t }$ takes on the value of zero), and $\lambda _ { i t }$ is the regression slope coefficient (representing the expected change in $\tau _ { i t }$ for a one-unit change in $\tau _ { 1 t } )$ . The residual variable $I S _ { i t }$ of this regression represents the indicator specificity in $\tau _ { { \mathrm { i } } t }$ , that is, variability in $\tau _ { i t }$ that cannot be predicted by the reference true score variable $\tau _ { 1 t }$ in the linear regression: 

$$
\begin{array}{l} I S _ {i t} = \tau_ {i t} - E (\tau_ {i t} \mid \tau_ {1 t}) \\ = \tau_ {i t} - \left(\alpha_ {i t} + \lambda_ {i t} \cdot \tau_ {1 t}\right) \\ \end{array}
$$

As a consequence of its definition as a linear regression residual variable, the indicator- specific variable $I S _ { i t }$ has a mean of zero and is uncorrelated with the regressor $\tau _ { 1 t } .$ . In summary, the residual variable $I S _ { i t }$ represents unique variance in $\tau _ { { \mathrm { i } } t }$ that is not shared with $\tau _ { 1 t }$ . 

So far, each non- reference state variable has its own associated $I S _ { i t }$ variable, which leads to an underidentified model. To obtain an identified model, an assumption is made with regard to the homogeneity of the indicator- specific 

effects across time. Specifically, it is assumed that the $I S _ { i t }$ variables are equivalent for the same variable across time. 

2. Equivalence of indicator- specific variables for the same measure: 

$$
I S _ {i t} = I S _ {i s} = I S _ {i} \text {f o r a l l} i = 1, \dots , m \text {a n d} t, s = 1, \dots , n
$$

Note that Assumption 2 implies that all $I S _ { i t }$ variables for the same observed variable are identical and can thus be replaced by a common indicator- specific factor IS .* In summary, we obtain the following measurement equation in the LS-IS model: 

$$
Y _ {i t} = \left\{ \begin{array}{l} \tau_ {1 t} + \varepsilon_ {1 t} \text {f o r} i = 1 \\ \alpha_ {i t} + \lambda_ {i t} \cdot \tau_ {1 t} + I S _ {i} + \varepsilon_ {i t} \text {f o r} i \neq 1 \end{array} \right.
$$

Lastly, as in the LS model without $I S _ { i }$ factors, we make the assumption of uncorrelated latent and error variables: 

3. Linear independence of latent and error variables: $C o \nu ( \tau _ { { 1 t } } , \varepsilon _ { { i s } } ) = C o \nu ( { I S } _ { i } , \varepsilon _ { { j t } } )$ $= 0$ for all t, $s = 1 .$ , . . . , n and $C o v ( \varepsilon _ { i t } , \varepsilon _ { j t } ) = 0$ for all $t = 1$ , . . . , n and $i \neq j$ . 

Recall that error variables pertaining to different time points are by definition uncorrelated in LST-R theory and hence, no specific additional assumption is required with regard to these correlations. 

*Alternatively, we may assume that the $I S _ { i t }$ variables pertaining to the same indicator are positive linear functions of one another such that $I S _ { i t } = \delta _ { i t } \cdot I S _ { i }$ for all i and $t$ , where $\delta _ { i t }$ is a real constant and $\delta _ { i t } > 0$ . However, this more complex assumption is often not needed in practice, and all constants $\delta _ { i t }$ can be fixed to one as in the model version described in the text. 

Therefore, the LS-IS model in general (i.e., without any invariance restrictions) has $3 n m + 0 . 5 ( n ^ { 2 } - n ) + m - 1 + 0 . 5 ( m ^ { 2 } - 3 m + 2 )$ free model parameters. For our example with three measures $( m = 3$ ) and four time points $( n = 4 )$ ), we obtain $3 \cdot 4 \cdot 3 + 0 . 5 \cdot ( 1 6 - 4 ) + 3 - 1 + 0 . 5 \cdot ( 9 - 9 + 2 ) = 4 5$ free model parameters. With three measures and four time points, we still have 90 pieces of known information (78 variances and covariances plus 12 means) and so the general LS-IS model has 45 df. Note that no means are estimated for the $I S _ { i }$ factors. This is because the $I S _ { i }$ factors are defined as regression residuals and therefore have means of zero by definition. 

In practice, researchers typically aim for at least strong ME (see the preceding discussion), so that state factor means and variances can be meaningfully compared across measurement occasions. With strong ME, the number of 

estimated intercepts and loadings combined reduces from $2 n ( m - 1 )$ to $2 ( m - 1 )$ . In our example, with strong ME, we have to estimate 12 parameters less (6 fewer loadings and 6 fewer intercepts). Hence, the total number of free parameters reduces to 33 with strong ME in our case, and the model has 57 df. In Box 4.9, I show how the LS-IS model can be defined based on the concepts of LST-R theory. 

# 4.3.3 Variance Decomposition and Coefficients

In the LS-IS model, the variances of the reference indicator can be decomposed in the same way as in the fundamental LST-R variance decomposition (see Chapter 1, Box 1.2): 

$$
V a r (Y _ {1 i}) = V a r (\tau_ {1 i}) + V a r (\varepsilon_ {1 i}) \mathrm {f o r} i = 1
$$

As a consequence, the reliability coefficient for the reference indicator can be defined as follows: 

$$
\begin{array}{l} R e l \left(Y _ {1 t}\right) = V a r \left(\tau_ {1 t}\right) / V a r \left(Y _ {1 t}\right) \\ = 1 - \left[ \operatorname {V a r} \left(\varepsilon_ {1 t}\right) / \operatorname {V a r} \left(Y _ {1 t}\right) \right] \\ = (\lambda_ {1 t} ^ {S}) ^ {2} \\ \end{array}
$$

where $( \lambda _ { 1 t } ^ { S } ) ^ { 2 }$ indicates the squared standardized state factor loading of the reference indicator. 

For the non-reference indicators, the $I S _ { i }$ factors represent an additional source of reliable (however specific) variance. The variance decomposition of the non-reference indicators is thus more complex: 

$$
\begin{array}{l} V a r (Y _ {i t}) = V a r (\tau_ {i t}) + V a r (\varepsilon_ {i t}) \\ = \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} \left(\tau_ {1 t}\right) + \operatorname {V a r} \left(I S _ {i}\right) + \operatorname {V a r} \left(\varepsilon_ {i t}\right) \text {f o r} i \neq 1 \\ \end{array}
$$

where 

$$
V a r (\tau_ {i t}) = \lambda_ {i t} ^ {2} \cdot V a r (\tau_ {1 t}) + V a r (I S _ {i})
$$

Based on the variance decomposition, two coefficients can be defined for the non-reference indicators. The convergent validity coefficient $C V ( Y _ { i t } )$ indicates the proportion of variability in a non-reference indicator that is accounted for by the reference state factor: 

$$
\begin{array}{l} C V \left(Y _ {i t}\right) = \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} \left(\tau_ {1 t}\right) / \operatorname {V a r} \left(Y _ {i t}\right) \\ = (\lambda_ {i t} ^ {S}) ^ {2} \\ \end{array}
$$

where $( \lambda _ { i t } ^ { S } ) ^ { 2 }$ indicates the squared standardized factor loading on the reference state factor. 

The larger the $C V ( Y _ { i t } )$ coefficient, the greater the similarity between the reference and a given non-reference indicator. The indicator-specificity coefficient $I S ( Y _ { i t } )$ indicates the proportion of variability in a non-reference indicator that is accounted for by the indicator-specific factor: 

$$
\begin{array}{l} I S \left(Y _ {i t}\right) = V a r \left(I S _ {i}\right) / V a r \left(Y _ {i t}\right) \\ = (\delta_ {i t} ^ {S}) ^ {2} \\ \end{array}
$$

where $( \delta _ { i t } ^ { \mathsf { S } } ) ^ { 2 }$ indicates the squared standardized factor loading on the $I S _ { i }$ factor. The larger the $I S ( Y _ { i t } )$ coefficient, the greater the amount of specificity in a given non-reference indicator relative to the chosen reference indicator. The $C V ( Y _ { i t } )$ and $I S ( Y _ { i t } )$ coefficients add up to the reliability coefficient for each non-reference indicator: 

$$
\begin{array}{l} R e l (Y _ {i t}) = C V (Y _ {i t}) + I S (Y _ {i t}) \\ = \left[ \lambda_ {i t} ^ {2} \cdot V a r \left(\tau_ {1 t}\right) + V a r \left(I S _ {i}\right) \right] / V a r \left(Y _ {i t}\right) \\ = (\lambda_ {i t} ^ {\mathrm {S}}) ^ {2} + (\delta_ {i t} ^ {\mathrm {S}}) ^ {2} \\ \end{array}
$$

The CV and IS coefficients can also be defined with respect to the underlying latent state variables $\tau _ { i t }$ : 

$$
\begin{array}{l} C V \left(\tau_ {i t}\right) = \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} \left(\tau_ {1 t}\right) / \operatorname {V a r} \left(\tau_ {i t}\right) \\ = \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} \left(\tau_ {1 t}\right) / \left[ \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} \left(\tau_ {1 t}\right) + \operatorname {V a r} (I S _ {i}) \right] \\ \end{array}
$$

$$
\begin{array}{l} I S (\tau_ {i t}) = \operatorname {V a r} (I S _ {i}) / \operatorname {V a r} (\tau_ {i t}) \\ = \operatorname {V a r} \left(I S _ {i}\right) / \left[ \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} \left(\tau_ {1 t}\right) + \operatorname {V a r} \left(I S _ {i}\right) \right] \\ \end{array}
$$

This has the advantage that the $C V ( \tau _ { i t } )$ and $I S ( \tau _ { i t } )$ coefficients add up to 1.0 for a given variable and thus make it easier to evaluate the relative amounts of shared versus specific indicator variability for that variable. By definition, $C V ( \tau _ { 1 t } ) = 1$ and $I S ( \tau _ { 1 t } ) = 0$ for the reference variable. 

In Mplus, only the $R e l ( Y _ { i t } )$ coefficient is given by default when the standardized solution (STDYX) is requested (as in the LS model, it is printed under R-SQUARE Observed Variable in the Mplus output). The $C V ( \tau _ { i t } )$ and 

# BOX 4.10. Correlated Errors: An Alternative Way to Model Indicator Specificity in Longitudinal Data

There are other ways to represent indicator- specific effects (“unique stability”) in multiple- indicator longitudinal data that are often used in practice. One common approach uses correlated measurement error variables for the same measure across time (Sörbom, 1975). This approach is also known as “correlated uniqueness” (CU) approach in the context of multitrait– multimethod (MTMM) data (Kenny, 1976). In the CU approach, all measurement error variables that pertain to the same repeatedly measured observed variable are allowed to correlate across time. That is, some or all covariances $C o v ( \varepsilon _ { i t } , \varepsilon _ { i s } )$ are freely estimated. In Mplus, the CU approach can be implemented by specifying, for example, 

# MODEL:

TAU1 by Y11 Y21 Y31; 

TAU2 by Y12 Y22 Y32; 

TAU3 by Y13 Y23 Y33; 

Y11 with Y12 Y13; 

Y12 with Y13; 

Y21 with Y22 Y23; 

Y22 with Y23; 

Y31 with Y32 Y33; 

Y32 with Y33; 

In this example, there are three indicators and three time points $( 3 \times 3$ longitudinal design). Hence, there are three latent state factors, TAU1 through TAU3. All measurement error variables $\varepsilon _ { i t }$ are allowed to correlate with other error variables that pertain to the same measure as indicated in the with statements that refer to the residuals of the endogenous $Y _ { i t }$ variables. 

Though frequently used, the CU approach has a number of limitations. It is not parsimonious because many additional parameters (covariances) are estimated. As an example, for the above $3 \times 3$ design, Eid et al.’s (1999) IS approach estimates only three additional parameters (two IS factor variances and their covariance) compared to the LS model without IS factors. In contrast, the CU approach estimates nine additional covariance parameters. The CU approach also confounds measurement error variance with systematic stable (trait) variance and thus often results in an underestimation of the variables’ reliabilities. Often, a number of the estimated error covariances turn out to be close to zero and not statistically significant. In this case, the approach can lead to interpretation difficulties (Geiser & Lockhart, 2012). The CU approach also assumes that indicator- specific effects are not correlated across indicators, whereas the IS approach allows the non- reference indicators to have shared variance above and beyond what they share with the reference indicator. Lastly, according to LST-R theory, all covariances between measurement error variables across time are by definition equal to zero. Therefore, a CU model would not be in line with the LST-R measurement theoretical framework. 

$I S ( \tau _ { i t } )$ coefficients have to be computed manually. As I show later in the application, this can be done using the MODEL CONSTRAINT option in Mplus. 

# 4.3.4 Mplus Application

To illustrate the LS-IS model in Mplus, I generated hypothetical cognitive ability test data that are similar to the data for the LS model without the IS factors presented in Section 4.2. However, I no longer assumed that the three cognitive ability tests measure unidimensional state variables. Instead, I generated data with a small to medium amount of indicator-specific variance (divergence from the first indicator). The first variable $Y _ { 1 t }$ was again generated to be in $I { \mathcal { Q } }$ -score metric $M = 1 0 0$ , $S D = 1 5$ ) and served as reference indicator in the LS-IS model. The second variable was again in T-score metric $\mathrm { ~ M ~ } = 5 0$ , $S D = 1 0 ,$ ) and now contained a small amount of indicator-specific variance, that is, variance that it did not share with the reference $( I { \mathcal { Q } } )$ variable. The third variable was again generated to be in $\mathcal { Z }$ -score metric with a population mean of 0 and an SD of 1, and now contained a medium amount of indicator-specific variance. 

The population model furthermore assumed strict ME across time (this assumption is not required for the specification of $I S _ { i }$ factors, but was chosen here for the sake of illustration and simplicity) and equal latent state variances across time. This version of the LS-IS model has 69 df (as opposed to 57 with only strong ME and freely estimated state variances). This is because we save an additional 12 parameters (9 measurement error variances and 3 latent state variances) by setting the measurement error and latent state variances equal across time. Below is the complete Mplus MODEL command for specifying the LS-IS model with strict ME and equal state factor variances across time: 

```txt
MODEL:  
TAU11 by Y11  
Y21 (12)  
Y31 (13);  
TAU12 by Y12  
Y22 (12)  
Y32 (13);  
TAU13 by Y13  
Y23 (12)  
Y33 (13);  
TAU14 by Y14  
Y24 (12)  
Y34 (13);  
[Y11@0 Y12@0 Y13@0 Y14@0];  
[Y21 Y22 Y23 Y24] (a2);  
[Y31 Y32 Y33 Y34] (a3); 
```

```txt
TAU11-TAU14 (VAR_TAU);  
[TAU11-TAU14*];  
Y11-Y14 (e1);  
Y21-Y24 (e2);  
Y31-Y34 (e3);  
IS2 by Y21-Y24@1;  
IS3 by Y31-Y34@1;  
TAU11-TAU14 with IS2-IS3@0; 
```

The last three lines of code add the two $I S _ { i }$ factors to the model and specify that the $I S _ { i }$ factors are not allowed to correlate with any of the reference state factors $\tau _ { 1 t } .$ The remaining commands are identical to the commands in the LS model with strict ME without $I S _ { i }$ factors, except that the LS factors are now labeled $\tau _ { \mathrm { l } t }$ instead of $\tau _ { t }$ . This was done to make clear that in the LS-IS model, the state factors are specific to the reference indicator $Y _ { 1 t } .$ . 

In this example, the model with the $I S _ { i }$ factors showed convergence problems in my initial application. This may seem surprising, given that I specified the correct (data-generating) model. However, such convergence failures occur rather frequently in practice even for well-fitting models when variables are measured on different scales, as was the case for the non-reference indicators $Y _ { 2 t }$ and $Y _ { 3 t }$ in this example (T-scores with a mean of 50 and an SD of 10 vs. z-scores with a mean of 0 and an SD of 1). 

Such strong differences in the variances can cause SEM programs to show convergence failures when using default parameter starting values, which are generated in a random fashion. Providing adequate user-defined starting values for the $I S _ { i }$ factor variances and their covariance (here: based on the population parameters from which the sample data was generated) in the Mplus MODEL command solved the problem in this example (see Box 4.11 for details). (In my experience, convergence problems are uncommon in the LS-IS model when indicators have more similar variances.) 

Below are selected unstandardized and standardized Mplus parameter estimates for the LS-IS model with strict ME: 

<table><tr><td colspan="6">MODEL RESULTS</td></tr><tr><td></td><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-Tailed P-Value</td></tr><tr><td>TAU11</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y11</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y21</td><td></td><td>0.585</td><td>0.019</td><td>31.124</td><td>0.000</td></tr><tr><td>Y31</td><td></td><td>0.051</td><td>0.003</td><td>20.220</td><td>0.000</td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>IS2</td><td>WITH</td><td></td><td></td><td></td><td></td></tr><tr><td>IS3</td><td></td><td>0.591</td><td>0.160</td><td>3.688</td><td>0.000</td></tr></table>

# BOX 4.11. Providing User‑Defined Starting Values in Mplus

For most identified standard models, the default parameter starting values used by Mplus are sufficient to achieve convergence after a reasonable number of iterations (the Mplus default is to use a maximum of 1,000 iterations). However, for some complex models or variables that are measured in very different metrics, convergence sometimes fails. In those cases, it can be helpful to provide user- defined starting values that are closer to the (expected) final parameter estimates than the default starting values. This is done by providing the userdefined starting value behind each parameter following an asterisk $( ^ { * } )$ . In our LS-IS example, I provided the value of 10 as a user- defined starting value for the $I S _ { 2 }$ factor variance, the value of 0.3 for the $I S _ { 3 }$ factor variance, and the value of 0.51961513 for the covariance between the two $I S _ { i }$ factors: 

MODEL: 

$\pm { \cal S } 2 ^ { \star } 1 0$ 

$\mathbb { T } { \cal S } 3 ^ { \star } 0 . 3$ 

IS2 with IS3*0.51961513; 

In my simulated data example, I was in the lucky situation of knowing the true population values from which the sample data were generated. Hence, I was able to use those population values as starting values to help with model convergence. Given that my starting values represented the known “true” values in the population, I could expect them to be close to the final sample estimates (which can differ from the population values only due to random sampling error). Therefore, using the population values as starting values helped point Mplus “in the right direction.” 

In actual empirical applications, the true population parameters are typically unknown. Nonetheless, researchers can often make informed guesses as to what might be reasonable estimates for a given parameter that are better choices than the Mplus default starting values (e.g., based on the known metric of the variables or prior studies with similar variables). Another strategy with heterogeneous indicators that differ strongly in their metrics is to transform the indicators in such a way that they are rescaled to a common or at least more similar metric prior to the LS-IS analysis. 

<table><tr><td colspan="6">...</td></tr><tr><td colspan="6">Means</td></tr><tr><td colspan="2">TAU11</td><td>99.775</td><td>0.849</td><td>117.521</td><td>0.000</td></tr><tr><td colspan="2">TAU12</td><td>99.826</td><td>0.849</td><td>117.584</td><td>0.000</td></tr><tr><td colspan="2">TAU13</td><td>99.835</td><td>0.849</td><td>117.589</td><td>0.000</td></tr><tr><td colspan="2">TAU14</td><td>100.046</td><td>0.849</td><td>117.842</td><td>0.000</td></tr><tr><td colspan="6">Variances</td></tr><tr><td colspan="2">TAU11</td><td>198.908</td><td>15.867</td><td>12.536</td><td>0.000</td></tr><tr><td colspan="2">TAU12</td><td>198.908</td><td>15.867</td><td>12.536</td><td>0.000</td></tr><tr><td colspan="2">TAU13</td><td>198.908</td><td>15.867</td><td>12.536</td><td>0.000</td></tr><tr><td colspan="2">TAU14</td><td>198.908</td><td>15.867</td><td>12.536</td><td>0.000</td></tr><tr><td colspan="2">IS2</td><td>11.595</td><td>1.569</td><td>7.391</td><td>0.000</td></tr><tr><td colspan="2">IS3</td><td>0.300</td><td>0.030</td><td>9.831</td><td>0.000</td></tr><tr><td colspan="6">Residual Variances</td></tr><tr><td colspan="2">Y11</td><td>25.430</td><td>2.013</td><td>12.630</td><td>0.000</td></tr><tr><td colspan="2">Y12</td><td>25.430</td><td>2.013</td><td>12.630</td><td>0.000</td></tr><tr><td colspan="2">Y13</td><td>25.430</td><td>2.013</td><td>12.630</td><td>0.000</td></tr><tr><td colspan="2">Y14</td><td>25.430</td><td>2.013</td><td>12.630</td><td>0.000</td></tr><tr><td colspan="2">Y21</td><td>20.006</td><td>1.106</td><td>18.082</td><td>0.000</td></tr><tr><td colspan="2">Y22</td><td>20.006</td><td>1.106</td><td>18.082</td><td>0.000</td></tr><tr><td colspan="2">Y23</td><td>20.006</td><td>1.106</td><td>18.082</td><td>0.000</td></tr><tr><td colspan="2">Y24</td><td>20.006</td><td>1.106</td><td>18.082</td><td>0.000</td></tr><tr><td colspan="2">Y31</td><td>0.218</td><td>0.012</td><td>18.966</td><td>0.000</td></tr><tr><td colspan="2">Y32</td><td>0.218</td><td>0.012</td><td>18.966</td><td>0.000</td></tr><tr><td colspan="2">Y33</td><td>0.218</td><td>0.012</td><td>18.966</td><td>0.000</td></tr><tr><td colspan="2">Y34</td><td>0.218</td><td>0.012</td><td>18.966</td><td>0.000</td></tr><tr><td colspan="6">STANDARDIZED MODEL RESULTS (STDYX Standardization)</td></tr><tr><td colspan="2"></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-TailedP-Value</td></tr><tr><td>TAU11</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y11</td><td></td><td>0.942</td><td>0.006</td><td>150.164</td><td>0.000</td></tr><tr><td>Y21</td><td></td><td>0.827</td><td>0.015</td><td>54.285</td><td>0.000</td></tr><tr><td>Y31</td><td></td><td>0.708</td><td>0.025</td><td>28.371</td><td>0.000</td></tr><tr><td>TAU12</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y12</td><td></td><td>0.942</td><td>0.006</td><td>150.164</td><td>0.000</td></tr><tr><td>Y22</td><td></td><td>0.827</td><td>0.015</td><td>54.285</td><td>0.000</td></tr><tr><td>Y32</td><td></td><td>0.708</td><td>0.025</td><td>28.371</td><td>0.000</td></tr><tr><td>TAU13</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y13</td><td></td><td>0.942</td><td>0.006</td><td>150.164</td><td>0.000</td></tr><tr><td>Y23</td><td></td><td>0.827</td><td>0.015</td><td>54.285</td><td>0.000</td></tr><tr><td>Y33</td><td></td><td>0.708</td><td>0.025</td><td>28.371</td><td>0.000</td></tr><tr><td>TAU14</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y14</td><td></td><td>0.942</td><td>0.006</td><td>150.164</td><td>0.000</td></tr><tr><td>Y24</td><td></td><td>0.827</td><td>0.015</td><td>54.285</td><td>0.000</td></tr><tr><td>Y34</td><td></td><td>0.708</td><td>0.025</td><td>28.371</td><td>0.000</td></tr><tr><td>IS2</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y21</td><td></td><td>0.341</td><td>0.024</td><td>14.142</td><td>0.000</td></tr><tr><td>Y22</td><td></td><td>0.341</td><td>0.024</td><td>14.142</td><td>0.000</td></tr><tr><td>Y23</td><td></td><td>0.341</td><td>0.024</td><td>14.142</td><td>0.000</td></tr><tr><td>Y24</td><td></td><td>0.341</td><td>0.024</td><td>14.142</td><td>0.000</td></tr><tr><td>IS3</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y31</td><td></td><td>0.537</td><td>0.026</td><td>20.481</td><td>0.000</td></tr><tr><td>Y32</td><td></td><td>0.537</td><td>0.026</td><td>20.481</td><td>0.000</td></tr><tr><td>Y33</td><td></td><td>0.537</td><td>0.026</td><td>20.481</td><td>0.000</td></tr><tr><td>Y34</td><td></td><td>0.537</td><td>0.026</td><td>20.481</td><td>0.000</td></tr><tr><td>IS2</td><td>WITH</td><td></td><td></td><td></td><td></td></tr><tr><td>IS3</td><td></td><td>0.317</td><td>0.075</td><td>4.252</td><td>0.000</td></tr><tr><td>TAU12</td><td>WITH</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU11</td><td></td><td>0.903</td><td>0.016</td><td>57.308</td><td>0.000</td></tr><tr><td>TAU13</td><td>WITH</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU11</td><td></td><td>0.901</td><td>0.016</td><td>55.360</td><td>0.000</td></tr><tr><td>TAU12</td><td></td><td>0.936</td><td>0.013</td><td>74.179</td><td>0.000</td></tr><tr><td>TAU14</td><td>WITH</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU11</td><td></td><td>0.917</td><td>0.015</td><td>61.799</td><td>0.000</td></tr><tr><td>TAU12</td><td></td><td>0.911</td><td>0.015</td><td>60.303</td><td>0.000</td></tr><tr><td>TAU13</td><td></td><td>0.930</td><td>0.014</td><td>68.512</td><td>0.000</td></tr><tr><td colspan="2">R-SQUARE</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">Observed</td><td></td><td></td><td></td><td>Two-Tailed</td></tr><tr><td colspan="2">Variable</td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>P-Value</td></tr><tr><td colspan="2">Y11</td><td>0.887</td><td>0.012</td><td>75.082</td><td>0.000</td></tr><tr><td colspan="2">Y12</td><td>0.887</td><td>0.012</td><td>75.082</td><td>0.000</td></tr><tr><td colspan="2">Y13</td><td>0.887</td><td>0.012</td><td>75.082</td><td>0.000</td></tr><tr><td colspan="2">Y14</td><td>0.887</td><td>0.012</td><td>75.082</td><td>0.000</td></tr><tr><td colspan="2">Y21</td><td>0.799</td><td>0.017</td><td>47.315</td><td>0.000</td></tr><tr><td colspan="2">Y22</td><td>0.799</td><td>0.017</td><td>47.315</td><td>0.000</td></tr><tr><td colspan="2">Y23</td><td>0.799</td><td>0.017</td><td>47.315</td><td>0.000</td></tr><tr><td colspan="2">Y24</td><td>0.799</td><td>0.017</td><td>47.315</td><td>0.000</td></tr><tr><td colspan="2">Y31</td><td>0.790</td><td>0.017</td><td>45.214</td><td>0.000</td></tr><tr><td colspan="2">Y32</td><td>0.790</td><td>0.017</td><td>45.214</td><td>0.000</td></tr><tr><td colspan="2">Y33</td><td>0.790</td><td>0.017</td><td>45.214</td><td>0.000</td></tr><tr><td colspan="2">Y34</td><td>0.790</td><td>0.017</td><td>45.214</td><td>0.000</td></tr></table>

Based on the parameter estimates, the $C V ( Y _ { i t } )$ , $I S ( Y _ { i t } )$ , and $R e l ( Y _ { i t } )$ coefficients can be computed for the non-reference indicators. A convenient way to obtain the above coefficients directly in Mplus along with standard errors and test statistics is through the MODEL CONSTRAINT option. For this purpose, the relevant variance components first have to be given labels in the regular model specification (the loadings have already been labeled as l2 and l3 and the common state factor variance has been labeled as VAR_TAU in the MODEL statement shown above): 

```asm
MODEL:  
    ..  
Y11-Y14 (e1); ! measurement error variances  
Y21-Y24 (e2); 
```

```txt
Y31-Y34 (e3);  
IS2*10 (IS2VAR);! IS factor variances  
IS3*0.3 (IS3VAR); 
```

In the next step, the relevant formulas for computation of the $C V ( Y _ { i t } )$ , $I S ( Y _ { i t } )$ , and $R e l ( Y _ { i t } )$ coefficients are implemented in MODEL CONSTRAINT by defining these coefficients as new parameters for each variable. As I have shown before, the $R e l ( Y _ { i t } )$ coefficients are output directly by Mplus as part of standardized solution under R-SQUARE. Nonetheless, I defined the reliability coefficients here as the sum of $C V ( Y _ { i t } ) + I S ( Y _ { i t } )$ to check whether I implemented the formulas for the $C V ( Y _ { i t } )$ and $I S ( Y _ { i t } )$ coefficients correctly in MODEL CONSTRAINT. 

model constraint:   
new(CV2t CV3t IS2t IS3t REL2t REL3t);   
! convergent validity coefficients   
CV2t $=$ ((12\*\*2)\*VAR_TA)/(12\*\*2)\*VAR_TA + IS2VAR + e2);   
CV3t $=$ ((13\*\*2)\*VAR_TA)/(13\*\*2)\*VAR_TA + IS3VAR + e3);   
! indicator-specificity coefficients   
IS2t $=$ IS2VAR/(12\*\*2)\*VAR_TA + IS2VAR + e2);   
IS3t $=$ IS3VAR/(13\*\*2)\*VAR_TA + IS3VAR + e3);   
! reliability coefficients   
REL2t $=$ CV2t + IS2t;   
REL3t $=$ CV3t + IS3t; 

In this case, the computations are straightforward because of the equality restrictions on the loadings, state factor variances, and measurement error variances. Because these parameters are held equal across time in the model, the CV(Y ), $I S ( Y _ { i t } )$ , and $R e l ( Y _ { i t } )$ coefficients are also time-invariant for a given variable. Therefore, these coefficients have to be computed only once for each variable (for non–time-invariant parameters, more coefficients would have to be defined than in this simplified example, but the principal steps remain the same). 

In order to compute the CV and IS coefficients for the latent state variables $\tau _ { i t }$ (rather than the measured variances $Y _ { i t } )$ , one would simply exclude the error variables $\scriptstyle ( { \mathtt { e 2 } }$ and ${ \tt e 3 }$ ) from the denominator in the above equations. The $C V ( Y _ { i t } )$ , $I S ( Y _ { i t } )$ , and $R e l ( Y _ { i t } )$ coefficients are output as new/additional parameters in the Mplus unstandardized MODEL RESULTS section: 

```txt
MODEL RESULTS Estimate S.E. Est./S.E. Two-Tailed P-Value New/Additional Parameters CV2T 0.683 0.025 27.143 0.000 CV3T 0.501 0.035 14.186 0.000 
```

<table><tr><td>IS2T</td><td>0.116</td><td>0.016</td><td>7.071</td><td>0.000</td></tr><tr><td>IS3T</td><td>0.289</td><td>0.028</td><td>10.241</td><td>0.000</td></tr><tr><td>REL2T</td><td>0.799</td><td>0.017</td><td>47.315</td><td>0.000</td></tr><tr><td>REL3T</td><td>0.790</td><td>0.017</td><td>45.214</td><td>0.000</td></tr></table>

It can be seen that $6 8 . 3 \%$ of the variability in the second indicator $Y _ { 2 t }$ was accounted for by the reference state factor $\tau _ { { 1 t } } \left[ C V ( Y _ { 2 t } ) = . 6 8 3 \right]$ , whereas $1 1 . 6 \%$ in the variability of the same indicator was accounted for by the indicator-specific factor $I S _ { 2 }$ $[ I S ( Y _ { 2 t } ) = 0 . 1 1 6 ]$ . The remaining $2 0 . 1 \%$ of the variability in $Y _ { 2 t }$ was due to measurement error (unreliability). Regarding the third indicator $Y _ { 3 t } ,$ $5 0 . 1 \%$ of the measured variability was due to the reference state factor $\tau _ { \mathrm { l } t }$ $[ C V ( Y _ { 3 t } ) =$ .501], $2 8 . 9 \%$ was due to the $I S _ { 3 }$ factor $[ I S ( Y _ { 3 t } ) = 0 . 2 8 9 ]$ , and the remaining $2 1 \%$ to measurement error. This indicates that the third variable contained more unique variance than the second one (relative to the reference indicator $Y _ { 1 t } )$ . The reliability estimates for $Y _ { 2 t } \left[ R e l ( Y _ { 2 t } ) = . 7 9 9 \right]$ $Y _ { 2 t }$ and $Y _ { 3 t }$ $Y _ { 3 t } \ [ R e l ( Y _ { 3 t } ) = . 7 9 0 ]$ were exactly identical to the Mplus R-SQUARE estimates, indicating that our $C V ( Y _ { i t } )$ and $I S ( Y _ { i t } )$ computations were correct. 

# 4.3.5 Summary

The LS model that I discussed in Section 4.2 is only appropriate for indicators that are strictly unidimensional (e.g., two independent cortisol measurements from the same saliva samples or strictly parallel achievement tests with homogeneous item types). Such indicators are rare in the social sciences. Most indicators are based on questionnaire or test items that contain some degree of specific indicator variance. The LS-IS model is designed to accommodate for the fact that indicators may not measure exactly the same construct. The LS-IS model allows researchers to determine not only the degree of ME and reliability, but also the degree of convergent validity (homogeneity) versus indicator specificity (heterogeneity) of the measures. That is, the LS-IS model can be used to examine the extent to which measures reflect the same construct versus different facets of a construct (or even different constructs). It often fits longitudinal social science data very well. 

# 4.4 CHAPTER SUMMARY

An important prerequisite for a meaningful interpretation of changes across time is that indicators show ME across time, that is, that their origin and units of measurement remain constant over time. Only by using multiple indicators 

can a researcher study whether the origin of measurement (as reflected in the intercepts) and units of measurement (as reflected in the loadings) are timeinvariant. Single-indicator models only allow study of whether measurement error variances remain the same across time. 

When ME is violated, true changes in constructs across time may be confounded with changes in the measurement properties (e.g., changes in the difficulty of a scale). In this chapter, I outlined a strategy for testing different levels of ME across time (i.e., configural, weak, strong, and strict ME). This strategy begins with a configural ME version of either the LS or LS-IS model and subsequently considers more and more constrained nested model versions with timeinvariant loadings, intercepts, and/or measurement error variances. Both the LS and LS-IS models allow researchers to focus on measurement-related issues before moving on to more complex longitudinal models such as autoregressive, state–trait, or growth models (see Chapter 5). 

The LS model assumes that indicators are homogeneous (unidimensional), whereas the LS-IS model allows for indicator-specific (method) effects. A useful modeling strategy is to begin with a comparison of the configural ME versions of the LS and LS-IS models in the first step of a longitudinal analysis. Depending on which of the two models fits the data better, subsequent tests of ME would then be based on either the LS or LS-IS model. 

Both the LS and LS-IS models can be used to test various hypotheses about structural model parameters (LS variable means, variances, and covariances). In the LS-IS model, these parameters are specific to the indicator that is selected as reference. Researchers should thus carefully select an appropriate reference indicator based on theory and/or conduct sensitivity analyses by comparing different versions of the LS-IS model with different reference indicators to determine the impact of choosing one reference variable over another. For heterogeneous indicators, the LS-IS approach can reveal important information about the extent to which different indicators measure the same or different constructs. 

Many of the models that I discuss in Chapter 5 are closely related to the LS and LS-IS models and/or can be seen as special cases of these models. It is useful to begin a multiple-indicator longitudinal analysis with the LS and/or LS-IS model because these models are less restricted than subsequent, more specialized models and thus allow testing ME independent of additional restrictions in the structural model. A decline in model fit when moving from the LS or LS-IS models to one of the more specialized models described in Chapter 5 can provide further insights into the longitudinal process under study (e.g., the longitudinal course of a construct may not be well described by a process of trait stability, but instead by a process of trait changes). 

# 4.5 RECOMMENDED READINGS



Eid, M., Schneider, C., & Schwenkmezger, P. (1999). Do you feel better or worse? The validity of perceived deviations of mood states from mood traits. European Journal of Personality, 13, 283–306. 





Meredith, W. (1993). Measurement invariance, factor analysis, and factorial invari‑ ance. Psychometrika, 58, 525–543. 





Millsap, R. E. (2011). Statistical approaches to measurement invariance. New York: Routledge. 





Widaman, K. F., & Reise, S. P. (1997). Exploring the measurement invariance of psy‑ chological instruments: Applications in the substance use domain. In K. J. Bry‑ ant, M. Windle, & S. G. West (Eds.), The science of prevention: Methodological advances from alcohol and substance abuse research (pp. 281–324). Washing‑ ton, DC: American Psychological Association. 



# NOTES



1. Exceptions are measures (observed indicators $Y _ { i t } )$ that meet the tau-equivalence assumption of classical test theory. Tau-equivalent measures by definition have the same origin and units of measurement. With tau-equivalent measures, all intercepts may be fixed to zero and all loadings may be fixed to unity so that the common latent true score variable (1) is uniquely defined to be equal to each observed variable’s true score variable and (2) shares the origin and units of measurement that are common to all indicators. 





2. Notice that another option in certain cases is to rescale the measured variables to a common metric, for example, the T- and z-score variables to IQscore variables. In this case, the tau-equivalence model (see the previous footnote) with equal loadings and intercepts across indicators or the essential tau-equivalence model (e.g., Steyer, 1989) with equal loadings across indicators may apply. 





3. Formal tests of changes in the amount of variance that is due to errors of measurement should be based on the estimated measurement error variances $V a r ( \varepsilon _ { i t } )$ as shown in Box 4.5 [Point (4)]. This is because the error variances $V a r ( \varepsilon _ { i t } )$ represent unstandardized parameters, whereas the reliability coefficient represents a standardized measure of measurement precision (squared correlation coefficient $R _ { Y _ { i t } } ^ { 2 \ \cdot }$ ). Tests of invariance should be conducted based on unstandardized parameters for which the variables are in their raw metric and not standardized to a common variance of 1. Nonetheless, informally comparing the reliability coefficients for a given measure across time can provide valuable information 



regarding potential changes in a measure’s reliability. Note that the reliability coefficient can change across time because of a change in the amount of error variance, a change in the amount of latent state variance, a change in factor loadings, or a combination of such changes. 

4. In some cases, ME cannot be established for all indicators. Under certain conditions, partial ME is sufficient for a meaningful comparison of latent variable parameters across time. Byrne, Shavelson, and Muthén (1989) as well as Little (2013) discussed the issue of partial ME in detail. 

# 5

# Multiple‑Indicator Longitudinal Models

# 5.1 INTRODUCTION

In Chapter 4, I showed how one key limitation of single-indicator longitudinal models (described in Chapters 2 and 3) can be addressed by using a design with multiple indicators. Specifically, I showed how measurement equivalence (ME) can be tested by statistically comparing different versions of a latent state (LS) model. In this chapter, I present additional, more specialized models for multiple-indicator longitudinal data: latent state change models, latent autoregressive/cross-lagged models, latent state–trait models, latent trait-change models, and multiple-indicator latent growth curve models. Some of these models can be seen as special cases of the LS and LS-IS models presented in Chapter 4. In addition, most of the models presented in this chapter have counterparts for singleindicator data that I discussed in Chapter 3. Where such connections exist, I point them out in my description of the models. Below, I review the limitations of single-indicator models that can be addressed with the multiple-indicator models presented in this chapter. 

Some single-indicator models overestimate the amount of variance due to random errors of measurement because they confound systematic state residual (situation and/or person $\times$ situation interaction) variance with unsystematic measurement error variance. Moreover, given that single-indicator models use only one measured variable per time point, potential discrepancies between indicators of a given construct (i.e., indicator-specific or method effects) cannot be examined. 

Another issue with some single-indicator models (e.g., the simplex and trait–state–error [TSE] models) is that they require fairly restrictive assumptions (e.g., regarding the equality of certain parameters across time) and that they may become empirically underidentified under a variety of conditions. This can result in estimation problems such as non-convergence, improper or biased parameter estimates, and large standard errors. Certain single-indicator models appear to work only when a researcher has access to a large number of waves and a large sample size (e.g., the TSE model discussed in Section 3.4). Singleindicator models also do not allow researchers to test for ME across time, that is, whether an observed variable’s factor loading and intercept are time-invariant. 

In cases in which more than one measure is available for a construct, multiple-indicator models are preferred because they are more flexible and address many of the shortcomings of single-indicator models. Some multipleindicator models allow separating all relevant variance components, including variable-specific (method) effects (i.e., trait, state residual, method, and measurement error) while requiring less restrictive assumptions than single-indicator models. As I show in this chapter, multiple-indicator designs also make it possible to separate trait changes from fluctuations due to state variability processes and measurement error. 

Multiple-indicator models are based on more pieces of information (observed variable means, variances, and covariances) and therefore tend to be less prone to problems of empirical underidentification compared to complex single-indicator models such as the simplex and TSE models. In general, multiple-indicator models require fewer time points, appear to result in fewer estimation problems, produce more stable results (Cole et al., 2005), and show greater statistical power for detecting interindividual differences in true changes over time (von Oertzen, Hertzog, Lindenberger, & Ghisletta, 2010). Finally, all multiple-indicator models allow researchers to conduct detailed tests of ME across time. I begin my discussion of additional multiple-indicator models with latent state change models, which are directly linked to the LS models presented in Chapter 4. 

# 5.2 LATENT STATE CHANGE MODELS

# 5.2.1 Introduction

Why do some people change more than others? Longitudinal researchers are often interested in analyzing and explaining interindividual differences in intraindividual changes across time. Latent state change score (LSC) models (McArdle, 2009; Raykov, 1993; Steyer, Eid, & Schwenkmezger, 1997) allow analyzing 

changes in the true state scores across time. This has the advantage that measurement error is taken into account, which can lead to bias in change score variables that are based on the difference between two measured (observed) variables. 

Recall that in Chapter 3, I introduced an LSC score version of the simplex model, also described in Chapter 3. Following the exact same principle, we can reformulate the LS or LS-IS model (see Chapter 4) in such a way that changes across time in the latent states can be directly expressed in terms of latent state difference (change score) variables. For the sake of generality, I present a change score version of the LS-IS model, which is less restrictive than then LS model. For homogeneous indicators, the same principles can be applied to the LS model without indicator-specific factors. 

# 5.2.2 Model Description

Recall the measurement equation in the LS-IS model: 

$$
Y _ {i t} = \left\{ \begin{array}{l} \tau_ {1 t} + \varepsilon_ {1 t} \text {f o r} i = 1 \\ \alpha_ {i t} + \lambda_ {i t} \cdot \tau_ {1 t} + I S _ {i} + \varepsilon_ {i t} \text {f o r} i \neq 1 \end{array} \right.
$$

In the LSC approach, difference score variables are included based on the reference latent state variables $\tau _ { \mathrm { l } t } .$ This can be done in different ways that lead to statistically equivalent models. In the so-called baseline change version of the LSC approach (Steyer, Partchev, & Shanahan, 2000), difference score variables are formulated relative to the initial time point (Time 1, the “baseline”): 

$$
\tau_ {1 t} = \tau_ {1 1} + (\tau_ {1 t} - \tau_ {1 1}) \text {f o r} t \geq 2
$$

Each of the change score variables $( \tau _ { 1 t } - \tau _ { 1 1 } )$ reflects interindividual differences in intraindividual changes between Time t and Time 1. 

In the neighbor change version (Steyer et al., 2000), change score variables are formulated to reflect changes between adjacent (“neighboring”) occasions of measurement: 

$$
\tau_ {1 t} = \tau_ {1 (t - 1)} + \left(\tau_ {1 t} - \tau_ {1 (t - 1)}\right) \text {f o r} t \geq 2
$$

Notice that in the neighbor change version, each of the change score variables $( \tau _ { 1 t } \mathrm { ~ - ~ } \tau _ { 1 ( t \mathrm { ~ - ~ } 1 ) } )$ reflects interindividual differences in intraindividual changes between Time $t$ and Time t – 1. Below I describe the neighbor change version 

in more detail as it seems to be more practical for most applications. The neighbor change version also parallels the single-indicator change score model that I described in Chapter 3. 

In the LSC approach, change score variables can be correlated with preceding state variables, other change score variables, and external variables (if included in the analysis). As in the LSC model that I presented in Chapter 3, change score variables can be regressed on previous states to obtain residualized change score variables. In contrast to the single-indicator change score model that I presented in Chapter 3, the multiple-indicator LSC model is less restrictive in that it allows all change score variables (or their residuals) to be correlated. 

In the neighbor change model, the latent state difference score variables can be regressed on the immediately preceding state variable, leading to the following structural equation (see also Figure 5.1): 

$$
\left(\tau_ {1 t} - \tau_ {1 (t - 1)}\right) = \gamma_ {0 t} + \gamma_ {1 t} \cdot \tau_ {1 (t - 1)} + \varsigma_ {1 t}
$$

where $\boldsymbol { \gamma } _ { 0 t }$ is a fixed latent intercept, $\gamma _ { 1 t }$ is a fixed slope (path or regression) coefficient, and $\varsigma _ { 1 t }$ is a latent residual change variable with a mean of zero that is uncorrelated with $\tau _ { 1 ( t - 1 ) }$ . The change score residual variable $\varsigma _ { \mathrm { l } t }$ reflects interindividual differences in true state changes that cannot be predicted from the previous state through a linear regression. It can therefore be interpreted as a variable representing residualized state change, where residualized means “adjusted for a potential linear relationship with the previous state.” 

The LSC model has the same number of parameters as its corresponding LS or LS-IS model. Moreover, the LSC model and its corresponding LS/LS-IS 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/68a2c061617cc821ef08c908687bec7dee83ba72d0b32dab7c9d401d037c17fd.jpg)



FIGURE 5.1. Path diagram of the structural model pertaining to a latent state change score (LSC) model for four time points. $\tau _ { 1 } =$ latent state factor at Time 1; $( \tau _ { t } - \tau _ { t - 1 } ) =$ latent state change score variable; $\varsigma _ { t } =$ latent change score residual variable; $\gamma _ { 0 t } = \mathrm { c o n - }$ stant regression intercept coefficient; $\gamma _ { 1 t } =$ constant regression slope coefficient. Residual covariances are not shown in the figure.


version are equivalent models that show an identical fit for a given set of data. The LSC model with IS factors and regression of change score variables on previous state variables estimates the following parameters: 

•	 the reference state factor mean at Time 1, $E ( \tau _ { 1 1 } )$ , 

•	 the reference state factor variance at Time 1, Var $( \tau _ { 1 1 } )$ 

• $n - 1$ latent regression intercept coefficients $\boldsymbol { \gamma } _ { 0 t }$ 

$n - 1$ latent regression slope coefficients $\gamma _ { 1 t } ,$ 

• $n - 1$ latent residual variances $V a r ( \varsigma _ { 1 t } )$ 

• $0 . 5 ( n - 1 ) ( n - 2 )$ residual covariances $C o v ( \varsigma _ { 1 t } , \varsigma _ { 1 s } )$ , $t \neq s$ 

• $m - 1$ indicator-specific factor variances $V a r ( I S _ { i } )$ , 

• $0 . 5 ( m - 1 ) ( m - 2 )$ indicator-specific factor covariances $C o v ( I S _ { i } , I S _ { j } )$ , $i \neq j$ 

• $n ( m - 1 )$ constant intercepts ${ \mathfrak { a } } _ { _ { \mathrm { i } t } }$ (the intercept pertaining the reference indicator is fixed to 0 on each measurement occasion), 

• $n ( m - 1 )$ constant factor loadings $\lambda _ { _ { i t } }$ (the loading pertaining the reference indicator is fixed to 1 on each measurement occasion), and 

• $n \cdot m$ measurement error variances $V a r ( \varepsilon _ { i t } )$ 

Therefore, the LSC-IS model in general (i.e., without any invariance restrictions) has $3 n m + 0 . 5 ( n ^ { 2 } - n ) + m - 1 + 0 . 5 ( m ^ { 2 } - 3 m + 2 )$ free model parameters. Notice that the number of parameters is the same as in the corresponding LS-IS model described in Section 4.3, hence, the LSC-IS model also has 45 parameters and 45 df in our example with three measures and four time points. 

In practice, the interpretation of the parameter estimates in an LSC model typically makes sense only when at least (partial or full) strong ME can be established (i.e., time-invariant loadings $\lambda _ { i }$ and intercepts ${ \bf { a } } _ { _ { i } } )$ . The reduction in the number of parameters under strong ME is analogous to the LS and LS-IS models. In our example, the LSC-IS model with strong ME has 33 free parameters and 57 df (as did the LS-IS model described earlier). 

# 5.2.3 Variance Decomposition and Coefficients

The observed variable variance decomposition is analogous to the decompositions in the LS/LS-IS models. The latent change score variance decomposition is analogous to the decomposition in the single-indicator change score model that I described in Chapter 3. 

# 5.2.4 Mplus Application

The Mplus specification of the LSC structural model and its interpretation parallels the specification of latent change score variables based on the simplex model as demonstrated in Chapter 3 (except that in the LSC model, the change score variables or their residuals can be correlated with each other) and is therefore not repeated here. However, I provide the full Mplus input and output files for the multiple-indicator LSC model as part of the supplementary materials on the companion website. 

# 5.2.5 Summary

In the same way as for the simplex model described in Chapter 3, we can reformulate an LS model with strong ME as an equivalent latent change score model. The LSC model has the advantage that true interindividual differences in intraindividual changes across time can be examined directly through latent variables that explicitly represent such changes in the true scores over time—either relative to a baseline time point or between adjacent measurement occasions. Using latent change (a.k.a. latent difference) score variables instead of observed difference score variables has the advantage that measurement error is taken into account, which can cause bias in observed variable change score analyses. Correlates, predictors, and/or outcomes of change can be included in the model to study the causes and/or consequences of change processes. For example, researchers may ask why some people’s cognitive abilities change more than others’ and/or whether changes in cognitive abilities in old age cause depression or other negative outcomes. Such questions can be addressed with LSC models that include external predictor/outcome variables. When using multiple indicators, an LSC model can be identified already for just two time points, whereas single-indicator LSC models require at least four measurement occasions. 

One downside of LSC models in general is that they use difference score variables that are based on latent state variables. According to LST-R theory, latent state variables $\tau _ { \mathrm { l } t }$ may contain both trait effects $( \boldsymbol { \xi } _ { 1 t } )$ and state residual (situation and person $\times$ situation interaction) effects $( \zeta _ { 1 t } )$ : 

$$
\tau_ {1 t} = \xi_ {1 t} + \zeta_ {1 t}
$$

As a consequence, state change variables $( \tau _ { 1 t } - \tau _ { 1 ( t - 1 ) } )$ may reflect either changes in traits, changes in situation and/or person $\times$ situation influences, or a combination of both: 

$$
\left(\tau_ {1 t} - \tau_ {1 (t - 1)}\right) = \left(\xi_ {1 t} - \xi_ {1 (t - 1)}\right) + \left(\zeta_ {1 t} - \zeta_ {1 (t - 1)}\right)
$$

These two components of change cannot be separated in LSC models. In Section 5.5, I discuss trait-change models that allow disentangling trait changes from state residual influences. 

# 5.3 THE LATENT AUTOREGRESSIVE/CROSS‑LAGGED STATES MODEL

# 5.3.1 Introduction

A person’s current behavior is often a very good predictor of his or her future behavior. In longitudinal structural equation models, this principle is often expressed in terms of an autoregressive structure—that is, allowing the current score to predict the future score. For example, a person’s current level of cognitive functioning is usually a good predictor of that person’s future cognitive abilities. In addition, other influences exist that may change the person’s cognitive abilities over time, for example, aging processes or nutrition. Statistically, such influences can be reflected in so-called cross-lagged variable effects. For example, above and beyond predicting individuals’ cognitive abilities from their previous level of cognitive functioning, a researcher may examine whether dietary factors (e.g., the use of artificial sweeteners) also have an impact on cognitive functioning at later time points. 

We already learned about autoregressive structural models in Chapter 3. Recall that in Section 3.2, I introduced the simplex model, which specifies a first-order autoregressive structure among latent state variables $\tau _ { t }$ . In addition, the TSE model described in Chapter 3 includes an autoregressive structure among occasion residual variables. 

Although I did not describe this in detail, I mentioned that a simplex model can be estimated simultaneously for two constructs, adding cross-lagged variable effects to the model. The exact same principle can be applied to an LS or LS-IS model (see Chapter 4). That is, the latent variable (structural) model of an LS or LS-IS model can be modified in such a way that the $\tau _ { t }$ variables are connected through an autoregressive structure (rather than simply estimating all state factor covariances). Moreover, multiconstruct models can be specified in which both autoregressive and cross-lagged effects can be analyzed. Multipleindicator designs have several advantages in the study of autoregressive/crosslagged effects that I describe in detail below. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/b440c6a1ef975a499b6c2a7b1f5ac48b129bc5f3e883fa08dcddf8be23578983.jpg)



FIGURE 5.2. Path diagram of the structural model pertaining to a latent autoregressive states (LAS) model for four time points. $\tau _ { t } =$ latent state factor; $\zeta _ { t } =$ latent state residual variable; $\boldsymbol { \beta } _ { 0 t } =$ constant regression intercept coefficient; $\beta _ { 1 t } =$ constant regression slope coefficient.


# 5.3.2 Model Description

One way to restrict the latent variable structure of the LS or LS-IS model is by assuming a first-order autoregressive process in which adjacent latent state variables are connected through bivariate latent regression paths as follows (see also Figure 5.2): 

$$
\tau_ {t} = \beta_ {0 t} + \beta_ {1 t} \cdot \tau_ {t - 1} + \zeta_ {t}
$$

where $\beta _ { 0 t }$ indicates a constant latent intercept and $\beta _ { 1 t }$ indicates a constant latent path (regression slope) coefficient. $\zeta _ { t }$ is a latent state residual variable with a mean of zero that is uncorrelated with $\tau _ { t \mathrm { ~ - ~ } 1 }$ . I refer to this model as a firstorder latent autoregressive state (LAS) model. Its latent variable autoregressive structure exactly parallels the structural model in the simplex approach that I presented in Chapter 3. (However, as I discuss in detail in Section 5.3.4, by using a multiple-indicator measurement model, the LAS model offers a lot more flexibility than the simplex model.) 

The latent variable covariance structure is more restricted in the LAS model than in the LS model because not all covariances between the latent state variables are freely estimated in the LAS model. Instead of estimating all $0 . 5 ( { n } ^ { 2 } - { n } )$ state factor covariances $C o v ( \tau _ { t } , \tau _ { s } )$ , the LAS model estimates only $n - 1$ latent path coefficients $\beta _ { 1 t }$ to represent the latent covariance structure. As an example, with four measurement occasions, the LS model estimates $0 . 5 \cdot ( 1 6 - 4 ) = 6$ state factor covariances. For the same design, the LAS model only estimates $4 - 1 = 3$ path coefficients $\beta _ { 1 t }$ to represent the latent covariance structure. 

In summary, the structural (latent variable) portion of the LAS model contains the following parameters: 

•	 the state factor mean $E ( \tau _ { 1 } )$ at Time 1, 

•	 the state factor variance $V a r ( \tau _ { 1 } )$ at Time 1, 

• $n - 1$ state residual factor variances Var $( \zeta _ { t } )$ for all t, $s = 2$ , . . . , n, 

• $n - 1$ latent intercept constants $\beta _ { 0 t } ,$ and 

• $n - 1$ latent path (regression slope) constants $\beta _ { 1 t . }$ 

Notice that the latent variance and mean structures of the LAS model have the same number of parameters as in the LS model. Instead of estimating n latent state factor variances $V a r ( \tau _ { t } )$ , the LAS model estimates the state factor variance at Time 1 $[ V a r ( \tau _ { 1 } ) ]$ plus $n - 1$ state residual factor variances $V a r ( \zeta )$ . Instead of estimating n latent state factor means $E ( \tau _ { t } )$ , the LAS model estimates the state factor mean at Time 1 $[ E ( \tau _ { 1 } ) ]$ plus $n - 1$ latent intercepts $\beta _ { 0 t } .$ . In contrast, the latent covariance structure in the LAS model is restricted by the first-order autoregressive process. This explains why the LAS model has fewer parameters than the corresponding LS model. 

The number of parameters in the measurement portion of the LAS model depends on whether the LS or LS-IS model is chosen as the basis for specifying the autoregressive structure. For strictly unidimensional indicators, the LS measurement structure can be used, which adds the following parameters (assuming no specific ME restrictions): 

• $n ( m - 1 )$ constant intercepts ${ \tt a } _ { i t }$ (one intercept per measurement occasion is fixed to 0 for identification), 

• $n ( m - 1 )$ constant factor loadings $\lambda _ { i t }$ (one loading per measurement occasion is fixed to 1 for identification), and 

•	 nm measurement error variances $V a r ( \varepsilon _ { i t } )$ . 

In summary, the LAS model for homogeneous indicators without specific ME restrictions has $n + 3 n m - 1$ parameters. In our example with three measures and four measurement occasions, we have $4 + 3 \cdot 4 \cdot 3 - 1 = 3 9$ parameters. This is three parameters less than in the LS model for the same design, because three fewer latent covariances are estimated. With three measures and four time points, we saw earlier that we have 90 pieces of known information and so the LAS model in this case has 51 df. 

In most social science applications, indicator-specific effects are present (i.e., indicators are not perfectly unidimensional), and so the LS-IS measurement model is more realistic. When using the LS-IS measurement model (and 

# BOX 5.1. Defining the LAS Model Based on LST‑R Theory

The definition of the LAS autoregressive structural model with latent state residuals $\zeta _ { t }$ follows the same logic as that for the single- indicator latent autoregressive (simplex) model presented in Chapter 3 (Box 3.1). The definition of the indicator- specific factors $I S _ { i }$ parallels the definition of these factors in the LS-IS model (see Chapter 4, Section 4.3). As usual, we assume that error variables are uncorrelated with other error variables as well as with the other latent variables in the model. 

again no specific ME restrictions), the LAS model has the following additional free parameters: 

• $m - 1$ indicator- specific factor variances $V a r ( I S _ { i } )$ , 

• $0 . 5 ( m - 1 ) ( m - 2 )$ indicator- specific factor covariances $C o v ( I S _ { i } , I S _ { j } ) _ { \ }$ $i \neq j$ 

• $n ( m - 1 )$ constant intercepts ${ \tt a } _ { i t }$ (the intercept pertaining to the reference indicator is fixed to 0 on each measurement occasion), 

• $n ( m - 1 )$ constant factor loadings $\lambda _ { _ { i t } }$ (the loading pertaining to the reference indicator is fixed to 1 on each measurement occasion), and 

•	 nm measurement error variances Var $( \varepsilon _ { i t } )$ . 

In summary, the LAS with LS-IS measurement structure has $n + 0 . 5 m ^ { 2 } -$ $1 . 5 m + m - 1 + 3 n m$ free parameters. In our example with three measures and four measurement occasions, we have $4 + 4 . 5 - 4 . 5 + 2 + 3 6 = 4 2$ parameters and 48 df. In Box 5.1, I explain how the LAS-IS model can be defined based on LST-R theory. 

# 5.3.3 Variance Decomposition and Coefficients

The variance decomposition as well as the definition and computation of the reliability, convergent validity, and indicator- specificity coefficients in the LAS-IS model are analogous to the LS-IS model (see Section 4.3). The variance decomposition of the latent state variables as well as the definition and computation of the consistency and occasion- specificity coefficients in the LAS-IS model are analogous to the simplex model (see Section 3.2). 

# 5.3.4 Other Features of the Model

The autoregressive process in the LAS model is identical to the structural model in the simplex model that I discussed in Chapter 3. I therefore do not repeat it here but focus instead on issues that are unique to the LAS model as well as on the multiconstruct extension of this model. 

The key difference between the simplex model and the LAS model is that the simplex model uses only a single observed variable at each time point, whereas the LAS model uses multiple indicators. As a consequence, the LAS model is identified already with just two time points (provided that there are three or more indicators at each time point or two indicators and a nonzero $\beta _ { 1 t }$ coefficient). In contrast, the simplex model requires four time points to be identified. Another advantage of the LAS model is that it does not require equality restrictions on the measurement error variances $V a r ( \varepsilon _ { i t } )$ or the latent state residual variances $V a r ( \zeta )$ to be identified even with fewer than four time points. 

Moreover, the LAS model is not restricted to a first-order autoregressive process. A first-order autoregressive process is one in which a latent state variable at Time t is regressed only on the immediately preceding latent state variable at Time $t - 1$ as described by the structural equation $\tau _ { t } = \mathsf { \beta } _ { 0 t } + \mathsf { \beta } _ { 1 t } \cdot \tau _ { t - 1 } +$ $\zeta _ { t } .$ In contrast, so-called higher-order autoregressive processes can also be studied in this model. That is, additional autoregressive paths from previous measurement occasions other than the immediately preceding time point are identifiable in this model, for example, $\tau _ { t } = \beta _ { 0 t } + \beta _ { 1 t } \cdot \tau _ { t - 1 } + \beta _ { 2 t } \cdot \tau _ { t - 2 } + \zeta .$ I do not discuss higher-order autoregressive models in detail in this book, as such extensions are rather straightforward and their implementation should be clear based on the description of the simpler first-order autoregressive model. 

Like the simplex model, the LAS model reflects the idea that previous behavior is often a very good predictor of subsequent behavior. In a first-order LAS model, the standardized path coefficients $\beta _ { 1 t } ^ { \mathsf { S } }$ indicate the strength of association (correlation) between adjacent LS variables and can be seen as measures of covariance stability. I discussed other forms of stability in detail for the simplex model in Chapter 3 and this discussion applies in the same way to the LAS model. 

# 5.3.5 Multiconstruct Extension

The LAS model can be expanded by adding a second construct (or more) that is also measured by multiple indicators and by including so-called cross-lagged paths between constructs (see Figure 5.3). Cross-lagged paths characterize 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/d829ba18fedb5d0b3958128e6c6438e95446177436cd5b4eef4405edb7f09c69.jpg)



FIGURE 5.3. Path diagram of the structural model pertaining to a latent autoregressive/ cross-lagged states (LACS) model for two constructs and four time points. $\tau _ { c t } =$ latent state factor pertaining to construct $c$ at Time t; $\zeta _ { c t } =$ latent state residual variable; $\beta _ { 0 c t } =$ constant regression intercept coefficient; $\beta _ { { \scriptscriptstyle 1 c t } } =$ constant autoregressive slope coefficient; $\beta _ { 2 c t } =$ constant cross-lagged slope coefficient. All latent state residual variables that share the same time point t can be correlated.


longitudinal relationships between different constructs and, under certain conditions, may represent the causal effects of one variable on another across time (Steyer et al., 2015). I refer to such an expanded model as a latent autoregressive/ cross-lagged states (LACS) model. This model can be described by the following structural equation: 

$$
\boldsymbol {\tau} _ {c t} = \beta_ {0 c t} + \beta_ {1 c t} \cdot \boldsymbol {\tau} _ {c (t - 1)} + \beta_ {2 e t} \cdot \boldsymbol {\tau} _ {e (t - 1)} + \zeta_ {c t}
$$

Notice that I added the new subscripts to indicate two different constructs, $c$ and $e$ , where c, $e = 1 .$ , . . . , o. Each latent state variable at Time $t$ is now predicted by two latent state variables that are measured at the previous time point $t - 1$ . The first predictor state variable $\tau _ { c ( t - 1 ) }$ pertains to the same construct c as the state variable $\tau _ { c t }$ that is being predicted. The second predictor state variable $\tau _ { e ( t - 1 ) }$ pertains to a different construct e. Hence, the regression slope coefficient $\beta _ { 1 c t }$ characterizes the autoregressive effect while also taking into account the cross-lagged regression $( \boldsymbol { \beta } _ { 2 e t } )$ of construct e on construct c. 

In contrast to the single-construct LAS model, the regression coefficients in the LACS model are partial regression coefficients. This is because there is now more than one predictor variable in the structural model and the predictor 

variables (states) may be correlated. Therefore, adjustments are made in the estimation of the autoregressive and cross-lagged path coefficients to account for the linear relationship (correlation) between constructs at the previous time point. This is the exact same principle as in conventional multiple regression analysis with multiple correlated predictor variables (e.g., Cohen, Cohen, West, & Aiken, 2003). 

This means that standardized regression coefficients usually cannot be interpreted as correlations in the LACS model (this would only be possible in the special situation in which the latent state variables that serve as predictors in the equation are uncorrelated, this is typically unlikely to be the case). The regression slope coefficients in the LACS model thus reflect the impact of a given state variable on $\tau _ { c t } ,$ , while statistically controlling for the linear relationship with the second state predictor variable in the equation. 

The LACS model can be used to study the extent to which an LS variable pertaining to one construct, say c, allows predicting a subsequent state variable pertaining to a different construct e, above and beyond the autoprediction (autoregressive effect). Given that the autoregressive effect is often strong, being able to show that a cross-lagged effect is present can be an important finding in a longitudinal study. 

Initial latent state variables pertaining to different constructs can be correlated as shown in Figure 5.3. In addition, correlations between latent state residuals at the same time point are allowed and may reflect shared occasionspecific (situational and/or person $\times$ situation interaction) influences that are often present in social science data. 

# 5.3.6 Mplus Application

To save space, I present a simplified, simulated Mplus example with two constructs $( \tau _ { 1 t } \dot { . }$ cognitive abilities; $\tau _ { 2 t } .$ : subjective well-being) and just two measurement occasions $\mathrm { \Delta } N = 3 0 0 \mathrm { \Omega }$ . The hypothesis here may be that cognitive functioning in old age has a positive effect on subjective well-being. That is, individuals with higher cognitive abilities may report higher subjective well-being than individuals with lower cognitive functioning due to the fact that higher cognitive abilities allow individuals to stay more actively connected to their social environment, conduct complex tasks independently, and so on. 

In my presentation of the Mplus application, I focus on the structural model in the LACS model because the measurement model is identical to the measurement model in the LS or LS-IS models described in Chapter 4. Below is that portion of the Mplus MODEL statement that concerns the structural model (i.e., the autoregressive/cross-lagged effects and state residual covariances). (In the online 

supplemental materials, an extended example with four measurement occasions and the corresponding LS-IS measurement model can be found.) 

```txt
MODEL:  
TAU21 on TAU11 TAU12;  
TAU22 on TAU21 TAU11;  
TAU12 with TAU22;  
[TAU11* TAU21* TAU12* TAU22*]; 
```

In the on statements, I specified both the autoregressive and cross-lagged paths. The statement TAU12 with TAU22 refers to the residual covariance $C o v ( \zeta _ { 1 2 } , \zeta _ { 2 2 } )$ . This is because both $\tau _ { 1 2 }$ and $\tau _ { 2 2 }$ are endogenous variables in this model, and so their residual covariance rather than covariance is estimated (see Box 3.3 for details on exogenous vs. endogenous variables in structural equation models and Mplus). This statement is required because Mplus would not estimate the residual covariance $C o v ( \zeta _ { 1 2 } , \zeta _ { 2 2 } )$ by default. Notice that the latent covariance at Time 1 [i.e., $C o v ( \tau _ { 1 1 } , \tau _ { 2 1 } ) ]$ as well as the residual variances $V a r ( \zeta _ { c t } )$ are estimated by default and do not have to be explicitly specified in the input file. 

The last line of code refers to the latent means $E ( \tau _ { 1 1 } )$ and $E ( \tau _ { 2 1 } )$ at Time 1 (because $\tau _ { \mathrm { 1 1 } }$ and $\tau _ { 2 1 }$ are exogenous variables in the model, they can have estimated means as in the LS and LS-IS models) and the intercepts $\beta _ { 0 1 2 }$ and $\beta _ { 0 2 2 }$ at Time 2 (because $\tau _ { 1 2 }$ and $\tau _ { 2 2 }$ are endogenous variables in the model, they do have intercepts instead of means as estimated parameters). Again, these statements are needed because those parameters are not estimated by default in Mplus. Below are Mplus output excerpts that contain the key structural parameter estimates in the LACS model: 

<table><tr><td colspan="5">MODEL RESULTS</td></tr><tr><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-Tailed P-Value</td></tr><tr><td colspan="5">TAU12 ON</td></tr><tr><td>TAU11</td><td>0.848</td><td>0.045</td><td>18.940</td><td>0.000</td></tr><tr><td>TAU21</td><td>-0.183</td><td>0.151</td><td>-1.214</td><td>0.225</td></tr><tr><td colspan="5">TAU22 ON</td></tr><tr><td>TAU21</td><td>0.790</td><td>0.070</td><td>11.297</td><td>0.000</td></tr><tr><td>TAU11</td><td>0.481</td><td>0.019</td><td>24.749</td><td>0.000</td></tr><tr><td colspan="5">TAU111 WITH</td></tr><tr><td>TAU121</td><td>21.756</td><td>3.748</td><td>5.804</td><td>0.000</td></tr><tr><td colspan="5">TAU12 WITH</td></tr><tr><td>TAU22</td><td>2.773</td><td>2.019</td><td>1.373</td><td>0.170</td></tr><tr><td colspan="5">Means</td></tr><tr><td>TAU11</td><td>100.046</td><td>0.840</td><td>119.041</td><td>0.000</td></tr><tr><td>TAU21</td><td>9.977</td><td>0.252</td><td>39.649</td><td>0.000</td></tr><tr><td>Intercepts</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU12</td><td>-2.676</td><td>4.115</td><td>-0.650</td><td>0.515</td></tr><tr><td>TAU22</td><td>2.257</td><td>1.812</td><td>1.245</td><td>0.213</td></tr><tr><td>Variances</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU11</td><td>195.839</td><td>17.586</td><td>11.136</td><td>0.000</td></tr><tr><td>TAU21</td><td>15.270</td><td>1.640</td><td>9.314</td><td>0.000</td></tr><tr><td>Residual Variances</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU12</td><td>50.026</td><td>6.959</td><td>7.189</td><td>0.000</td></tr><tr><td>TAU22</td><td>7.042</td><td>1.229</td><td>5.728</td><td>0.000</td></tr><tr><td colspan="5">STANDARDIZED MODEL RESULTS (STDYX Standardization)</td></tr><tr><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-TailedP-Value</td></tr><tr><td>TAU12 ON</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU11</td><td>0.873</td><td>0.027</td><td>32.193</td><td>0.000</td></tr><tr><td>TAU21</td><td>-0.053</td><td>0.043</td><td>-1.217</td><td>0.224</td></tr><tr><td>TAU22 ON</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU21</td><td>0.349</td><td>0.030</td><td>11.687</td><td>0.000</td></tr><tr><td>TAU11</td><td>0.760</td><td>0.025</td><td>30.530</td><td>0.000</td></tr><tr><td>TAU111 WITH</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU121</td><td>0.398</td><td>0.055</td><td>7.240</td><td>0.000</td></tr><tr><td>TAU112 WITH</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU122</td><td>0.148</td><td>0.100</td><td>1.474</td><td>0.141</td></tr><tr><td>Residual Variances</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU12</td><td>0.271</td><td>0.036</td><td>7.440</td><td>0.000</td></tr><tr><td>TAU22</td><td>0.090</td><td>0.017</td><td>5.362</td><td>0.000</td></tr><tr><td>R-SQUARE</td><td></td><td></td><td></td><td></td></tr><tr><td>Latent</td><td></td><td></td><td></td><td rowspan="2">Two-TailedP-Value</td></tr><tr><td>Variable</td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td></tr><tr><td>TAU12</td><td>0.729</td><td>0.036</td><td>20.000</td><td>0.000</td></tr><tr><td>TAU22</td><td>0.910</td><td>0.017</td><td>54.340</td><td>0.000</td></tr></table>

It can be seen that the autoregressive paths $\tau _ { c 1 } \to \tau _ { c 2 }$ for both constructs are statistically significant, as we would expect for most social science constructs. In addition, the cross-lagged path from cognitive abilities at Time 1 $( \tau _ { 1 1 } )$ to subjective well-being at Time 2 $\beta _ { 1 2 2 } ^ { \mathrm { s t a n d a r d i z e d } } = 0 . 7 6$ $p < . 0 0 1$ 22 122 ; this effect is printed under TAU22 ON Td path from subjective well-being at Time 1 $( \tau _ { 2 2 } )$ is also significant $( \beta _ { 1 2 2 } = 0 . 4 8 1$ , $S E = 0 . 0 1 9$ 1).  to , $( \tau _ { 2 1 } )$ cognitive abilities at Time 2 $( \tau _ { 1 2 } )$ is not statistically significant $( \beta _ { 1 1 2 } = - 0 . 1 8 3$ $S E = 0 . 1 5 1$ , $\beta _ { 1 2 2 } ^ { \mathrm { s t a n d a r d i z e d } } = - 0 . 0 5 3$ , $p = . 2 2 5$ ; printed under TAU12 ON TAU21). 

The cross-lagged paths indicate that, as was hypothesized, higher cognitive abilities are associated with higher subjective well-being scores at the second time point, even when controlling for the autoregressive effect of subjective 

well-being on itself. In contrast, higher subjective well-being scores are not predictive of subsequent cognitive abilities at Time 2 above and beyond the autoregression. (Keep in mind that the data used in this example are simulated and that even in real data, cross-lagged effects may not be indicative of causal effects.) 

At Time 1, the latent state variables representing cognitive abilities and subjective well-being true scores are moderately positively correlated $( \Phi _ { 1 1 , 2 1 } = . 3 9 8$ $p < . 0 0 1 )$ . The latent state residuals at Time 2 are not significantly correlated $( \Phi _ { 1 2 , 2 2 } = . 1 4 8$ , $p = . 1 4 1 )$ . This indicates that the cognitive ability and subjective well-being state scores do not share any occasion-specific influences at Time 2. In total, $7 2 . 9 \%$ of the true variability in cognitive ability scores and $9 1 \%$ of the true variability in subjective well-being scores at Time 2 are accounted for in the model as shown by the estimated latent variable $R ^ { 2 }$ values. 

# 5.3.7 Summary

Autoregressive/cross-lagged models are intuitive longitudinal models, as they reflect the idea that previous behavior is usually a strong predictor of future behavior. In addition, they allow studying how external variables may lead to changes in a construct through cross-lagged effects. The LACS model allows estimating such effects while correcting for random measurement error and controlling for the (usually substantial) effects of the autoregression. The LA(C) S (latent autoregressive [cross-lagged] states) models presented in this section represent multiple-indicator extensions of the simplex approach presented in Chapter 3, which can also be used to study autoregressive and cross-lagged effects. 

The use of multiple indicators makes the LA(C)S models more flexible than the simplex model in at least four ways. First, the LA(C)S models are generally identifiable even when there are only two measurement occasions (some additional restrictions apply in cases in which there are only two indicators per construct and time points and latent variables are not substantially correlated). Second, the LA(C)S models do not require the same equality constraints regarding the measurement error or latent state residual variances that are needed for identification in the simplex approach (again, additional restrictions do apply in designs with only two measures and weakly correlated latent variables). Third, the LA(C)S models also allow for the estimation of higher-order autoregressive effects as well as correlated state residuals at the same measurement occasion. Fourth, the multiple-indicator LA(C)S approach allows examining method effects (indicator heterogeneity), for example, by specifying indicator-specific residual factors as in the LS-IS approach. 

One limitation of the LA(C)S approach described here parallels a limitation previously discussed for the latent state change (LSC) score model (see Section 5.2). The LACS model considers stability and changes in latent state variables $\tau _ { t } .$ , which may contain both trait $( \xi )$ and state residual $( \zeta _ { t } )$ components. Therefore, like the LSC model, the $\mathrm { L A } ( C ) S$ approach may confound stability and/or changes in traits with stability and/or changes in situation/person $\times$ situation interaction effects. Later in this chapter, I describe latent trait-change models that allow disentangling trait changes from state residual effects. As a first step toward this separation of trait and state residual effects, I now introduce latent state–trait models, which include not only latent state and measurement error variables, but also latent trait and latent state residual variables. Subsequently, I show how specific longitudinal designs allow extending classical latent state– trait models in such a way that changes in latent trait variables can be analyzed separately from state residual influences. 

# 5.4 LATENT STATE–TRAIT MODELS

# 5.4.1 Introduction

Social science researchers are sometimes interested in determining to which extent constructs represent stable traits versus fluctuating states. Likewise, in measurement, we may be interested in finding out the extent to which our measures reflect something that is state-like versus trait-like and separate variance components due to trait, state residual, and measurement error components. In Chapter 3, I discussed Kenny and Zautra’s (1995) TSE model. This model allows examining the trait, occasion residual (situation and/or person $\times$ situation interaction), measurement error, and other components of social science measurements. As I explained in Chapter 3, though creative and theoretically appealing, the TSE model is often difficult to fit in empirical applications due to issues of empirical underidentification, which may result in nonconvergence or other estimation problems. 

Many of the problems of the TSE model can be explained by the fact that the model uses only a single indicator (measured variable) at each time point and hence often lacks sufficient information to identify all parameters of interest. In this section, I describe various latent state–trait (LST) models that use multiple indicators at each time point. By using multiple indicators, we gain flexibility in the modeling—there is a diverse set of multiple-indicator LST models available to address various purposes. Multiple-indicator LST models in general make less restrictive assumptions. They are less prone to empirical underidentification and other problems of the TSE model, and they appear to 

be more stable generally across a range of situations (Cole et al., 2005). In addition, some multiple-indicator LST models allow examining indicator-specific or method effects as well. 

Most multiple-indicator LST models were first presented by Rolf Steyer and colleagues in the late 1980s and early 1990s. I begin with a simple but prototypical multiple-indicator LST model that was one of the first LST models ever described (e.g., Steyer et al., 1989, 1992), the so-called singletrait–multistate model. 

# 5.4.2 The Singletrait–Multistate Model

# 5.4.2.1 Introduction

The singletrait–multistate (STMS) model can be seen as a special case of the LS model in which the covariances between the latent state factors $\tau _ { t }$ are restricted to follow a unidimensional structure (i.e., all latent state factors are assumed to measure the same underlying common latent trait factor). By adding a common trait factor $\xi ,$ , the STMS model makes it possible to separate trait and state residual variance components from random measurement error variance. An STMS model can be formulated as either a second-order (hierarchical) factor model or a nested (bifactor) model. In the main text, I focus on the hierarchical factor specification because, historically, it was the first version of the STMS approach that was presented in the literature (Steyer et al., 1989). An alternative bifactor specification is described in Box 5.4 later in this chapter. 

# 5.4.2.2 Model Description

The hierarchical STMS model has the same measurement model as the LS model in which each observed variable $Y _ { i t }$ reflects a time-specific latent state variable $\tau _ { t }$ and measurement error $\varepsilon _ { i t }$ : 

$$
Y _ {i t} = \alpha_ {i t} + \lambda_ {i t} \cdot \tau_ {t} + \varepsilon_ {i t}
$$

As in the LS model, potential differences in scaling and/or differences in item difficulty or item discrimination between measured variables can be reflected in the constant intercept ${ \bf \mathfrak { a } } _ { i t }$ and/or slope coefficients (factor loadings) $\lambda _ { _ { i t } }$ . 

The structural (latent variable) portion of the STMS model differs from the structural portion in the LS model. Recall that in the basic LS model, the latent variable covariance and mean structure is unrestricted (saturated). That is, LS 

variables $\tau _ { t }$ in this model are allowed to freely correlate with all other latent state variables. In addition, their means and variances can be freely estimated at each time point. 

In contrast, in the STMS model, the covariance (and potentially also the mean structure) of the latent state variables $\tau _ { t }$ is constrained to follow a unidimensional second-order factor structure with a single second-order trait factor $\xi$ (see Figure 5.4). The second-order factor $\xi$ in Figure 5.4 represents the common trait (person) component of the first-order state factors. The time-specific latent residual variables $\zeta _ { t }$ represent the state residual components in the sense of LST-R theory and reflect situation and/or person $\times$ situation interaction effects. Hence, the STMS model decomposes each latent state variable as follows: 

$$
\tau_ {t} = \xi + \zeta_ {t}
$$

The complete decomposition of the measured variables in the STMS model can thus be written as 

$$
\begin{array}{l} Y _ {i t} = \alpha_ {i t} + \lambda_ {i t} \cdot (\xi + \zeta_ {t}) + \varepsilon_ {i t} \\ = \alpha_ {i t} + \lambda_ {i t} \cdot \xi + \lambda_ {i t} \cdot \zeta_ {t} + \varepsilon_ {i t} \\ \end{array}
$$

Note that in the hierarchical version of the STMS model, it is implied that the measured variables have the same loading $\lambda _ { _ { i t } }$ on both the common trait $\xi$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/a9c408c10393acc54d64a5ee1efdae7e5a2f78d455dd54a61532254c9c358c7e.jpg)



FIGURE 5.4. Path diagram of the structural model pertaining to a singletrait– multistate (STMS) model for four time points. $\tau _ { t } =$ latent state factor; $\xi =$ common latent trait factor; $\zeta _ { t } =$ latent state residual variable.


and occasion-specific state residual factor $\zeta _ { t } .$ . This is different in an alternative bifactor STMS model version (see Box 5.4 on pages 179–180). 

Imposing a second-order factor structure means that the covariances and means of the latent state variables are no longer unrestricted as in the LS model. Instead, they are constrained to follow a unidimensional (single higher-order factor) structure. Specifically, the STMS model implies that all LS factor means and covariances are equal in the population, respectively. Therefore, the STMS model can be understood as a special (restricted) case of the LS model in which the latent state variables are assumed to be unidimensional with equal means and equal covariances across time. 

Changes in indicator-specific traits across time (i.e., changes in $\xi _ { i t }$ vs. $\boldsymbol { \xi } _ { i s } )$ are only possible through time-varying intercepts ${ \mathfrak { a } } _ { i t }$ and/or loadings $\lambda _ { _ { i t } }$ . In practice, however, these parameters are often assumed to be time-invariant in LST analyses (implying strong ME). Time-invariant intercepts and loadings imply no trait changes at all across time in the STMS model (Geiser et al., 2015). 

Another way to view the STMS model is as an extension of the random intercept model presented in Chapter 2. Recall that the random intercept model also uses a single-trait factor $\xi$ to account for covariance stability across time. However, in the random intercept model, there are no state residual factors $\zeta _ { t }$ . This is because the random intercept model uses only a single indicator per measurement occasion, which makes it impossible to separate trait and state residual components without further assumptions. Hence, the STMS model has the advantage that it allows analyzing both, a common trait factor and timespecific state residual factors. As a consequence, we no longer have to assume that constructs are strictly trait-like (as is the case in the random intercept model), and we can now properly separate trait variance from state residual and measurement error variance. This allows us to more accurately estimate the reliabilities of our measures, which tend to be underestimated in the random intercept model (which confounds state residual and measurement error variance components). 

In summary, the STMS model (without any invariance restrictions) estimates the following parameters: 

•	 one trait factor mean $E ( \xi )$ 

•	 one trait factor variance Var $( \xi )$ , 

•	 n state residual factor variances $V a r ( \zeta )$ $( \zeta _ { t } )$ , 

• $n ( m - 1 )$ constant intercepts ${ \tt a } _ { i t }$ (the intercept pertaining to the reference indicator is fixed to 0 on each measurement occasion), 

• $n ( m - 1 )$ constant factor loadings $\lambda _ { i t }$ (the loading pertaining to the reference indicator is fixed to 1 on each measurement occasion), and 

•	 nm measurement error variances Var $( \varepsilon _ { i t } )$ . 

Therefore, the STMS model in general (i.e., without any invariance restrictions) has $2 - n + 3 n m$ free model parameters. For our example with three measures $( m = 3 )$ ) and four time points $( n = 4 )$ , we obtain $2 - 4 + 3 \cdot 4 \cdot 3 = 3 4$ free model parameters. With three measures and four time points, we have 90 pieces of known information, and so the general STMS model has 56 df. In Box 5.2, I explain how the STMS model can be defined based on LST-R theory. 

# BOX 5.2. Defining the STMS Model Based on LST‑R Theory

Using concepts of LST-R theory, the STMS model can be defined based on the following assumptions: 

1. Occasion- specific congenericity of latent state variables: All latent state variables measured at the same time point are positive linear functions of each other, such that $\tau _ { i t } = \mathbf { a } _ { i j t } + \lambda _ { i j t } \cdot \tau _ { j t }$ for all $i , j = 1 .$ , . . . , m and $t = 1$ $\mathbf { \varepsilon } \cdot \mathbf { \varepsilon } \cdot \mathbf { \varepsilon } , n$ . This assumption is equivalent to assuming a common latent state factor $\tau _ { t }$ at each time point such that $\boldsymbol { \tau } _ { i t } = \mathbf { a } _ { i t } + \boldsymbol { \lambda } _ { i t } \cdot \boldsymbol { \tau } _ { t }$ . 

2. Equivalence of latent trait variables: In LST-R theory, each latent state variable is decomposed into a trait and a state residual component such that $\tau _ { t } = \xi _ { t } + \zeta _ { t } .$ In the STMS model, it is assumed that all trait components $\xi _ { { t } }$ are identical: $\boldsymbol { \zeta } _ { t } = \boldsymbol { \xi } _ { s } = \boldsymbol { \xi }$ for all t, $s = 1$ , . . . , n.* 

3. Linear independence of latent and error variables: It is assumed that $C o v ( \xi ,$ $\zeta _ { t } ) = C o \nu ( \xi , \varepsilon _ { \scriptscriptstyle i t } ) = C o \nu ( \zeta _ { t } , \varepsilon _ { \scriptscriptstyle i s } ) = 0$ and $C o v ( \varepsilon _ { i t } , \varepsilon _ { j s } ) = 0$ for $( i , t ) \neq ( j , s )$ . In addition, by definition of LST-R theory, $C o v ( \check { \zeta _ { t } } , \zeta _ { s } ) = 0$ for $t \neq s$ . 

The assumption of occasion- specific congenericity again implies unidimensionality of the measured variables $Y _ { i t }$ at a given time point. The assumption of equivalence of latent trait variables means that trait components remain stable across time and affect all states in the same way. The linear independence assumptions simplify the variance decomposition and often make sense in empirical applications. 

# 5.4.2.3 Variance Decomposition and Coefficients

The latent variables $\xi$ and $\zeta _ { t }$ are assumed to be uncorrelated in the STMS model. Furthermore, all error variables $\varepsilon _ { i t }$ are typically assumed to be uncorrelated with all latent variables and with one another. As a consequence, the following additive variance decompositions hold in the STMS model: 

$$
\begin{array}{l} \operatorname {V a r} \left(\tau_ {i t}\right) = \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} \left(\tau_ {t}\right) \\ = \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} (\xi) + \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} (\zeta_ {t}) \\ \end{array}
$$

$$
\begin{array}{l} \operatorname {V a r} \left(Y _ {i t}\right) = \operatorname {V a r} \left(\tau_ {i t}\right) + \operatorname {V a r} \left(\varepsilon_ {i t}\right) \\ = \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} \left(\tau_ {t}\right) + \operatorname {V a r} \left(\varepsilon_ {i t}\right) \\ = \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} (\xi) + \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} (\zeta_ {t}) + \operatorname {V a r} (\varepsilon_ {i t}) \\ \end{array}
$$

Based on the additive variance decomposition, coefficients can be defined that allow quantifying to which degree the latent state and/or observed variables reflect trait effects (consistency, Con) or situation/person $\times$ situation interaction effects (occasion specificity, Osp). Furthermore, a reliability coefficient (Rel) can be defined for the observed variables: 

$$
\begin{array}{l} C o n (\tau_ {i t}) = \operatorname {V a r} (\xi) / \operatorname {V a r} (\tau_ {i t}) \\ O s p \left(\tau_ {i t}\right) = \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} \left(\zeta_ {t}\right) / \operatorname {V a r} \left(\tau_ {i t}\right) \\ C o n \left(Y _ {i t}\right) = \lambda_ {i t} ^ {2} \cdot V a r (\xi) / V a r \left(Y _ {i t}\right) \\ O s p \left(Y _ {i t}\right) = \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} \left(\zeta_ {t}\right) / \operatorname {V a r} \left(Y _ {i t}\right) \\ R e l \left(Y _ {i t}\right) = V a r \left(\tau_ {i t}\right) / V a r \left(Y _ {i t ^ {\prime}}\right) \\ = \left[ \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} (\xi) + \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} (\zeta_ {t}) \right] / \operatorname {V a r} (Y _ {i t}) \\ = 1 - \left[ \operatorname {V a r} \left(\varepsilon_ {i t}\right) / \operatorname {V a r} \left(Y _ {i t}\right) \right] \\ = C o n \left(Y _ {i t}\right) + O s p \left(Y _ {i t}\right) \\ \end{array}
$$

These coefficients allow researchers to examine the extent to which the constructs under study are trait-like versus state-like as well as the extent to which the measures are free of measurement error. The Con coefficients give the proportion of latent state or observed variance that is due to trait (person) effects. The occasion-specificity Osp coefficients give the proportion of latent state or observed variance that is due to situation and/or person $\times$ situation interaction effects. The Rel coefficient gives the proportion of observed variance that reflects true score (systematic) variance, that is, reliable trait and state residual variance combined. 

Mplus by default only prints the reliability coefficients for the observed variables (under R-SQUARE Observed Variable) as well as the $C o n ( \tau _ { t } )$ 

# BOX 5.3. Some Guidelines for the Interpretation of the Con, Osp, and Rel Coefficients

LST models such as the STMS model are often used in practice to determine the extent to which the chosen measures of a construct under study reflect something that is more trait-like (stable across time; e.g., intelligence) versus more state-like (fluctuating; e.g., mood). Higher Con coefficients indicate that measures reflect a more trait-like construct. Higher Osp coefficients point to a more state-like construct. Although no fixed rules exist as to when a construct should be considered a “trait” versus a “state,” we might say that measures for which more than $5 0 \%$ of their true state variance is due to trait effects [i.e., $C o n ( \tau _ { t } ) >$ .5] can be viewed as more trait-like than state-like. Conversely, measures whose underlying true state score variables contain more than $5 0 \%$ state residual variance [i.e., $O s p ( \tau _ { t } ) > . 5 ]$ can be considered more state-like than trait-like. The interpretation of the reliability coefficient $R e l ( Y _ { i t } )$ is the same as in models of classical test theory as well as other longitudinal models discussed in this book. Higher values of $R e l ( Y _ { i t } )$ indicate higher precision of the measures. Values close to 1.0 are desirable. Commonly, measures whose $R e l ( Y _ { i t } )$ values exceed .8 are seen as having good reliability, whereas measures whose $R e l ( Y _ { i t } )$ values exceed .9 are seen as having excellent reliability. 

and $O s p ( \tau _ { t } )$ coefficients for the common latent state variables. [The $C o n ( \tau _ { t } )$ coefficients are printed under R- SQUARE Latent Variable, whereas the $O s p ( \tau _ { t } )$ coefficients are given as the standardized residual variances for the $\tau _ { t }$ variables.] In the Mplus application section below, I demonstrate how the Con and $O s p$ coefficients for the observed variables $Y _ { i t }$ as well as all latent state variables $\tau _ { i t }$ can be computed manually in Mplus using the MODEL CONSTRAINT option. In Box 5.3, I provide guidelines regarding the interpretation of the Con, Osp, and Rel coefficients. 

# 5.4.2.4 Mplus Application

For the application of the STMS model, I used the same hypothetical 3-variable, 4-wave cognitive ability data set that I generated to illustrate the LS model in Chapter 4. The data were generated so that the latent state variables had equal means and equal covariances in the population and were thus in line with both an LS and STMS model; this may or may not be the case in actual empirical applications. 

In my specification of the STMS model, I assumed strict ME, as this level of ME was supported in the LS analyses reported in Chapter 4. I also assumed that the state residual variances $V a r ( \zeta )$ were time-invariant such that $V a r ( \zeta _ { t } ) =$ $V a r ( \zeta _ { s } ) = V a r ( \zeta )$ for all t, s. These restrictions are not required, and they may not be supported in every empirical application. The Mplus MODEL statement appears below: 

```txt
MODEL:  
TAU1 by Y11  
Y21 (12)  
Y31 (13);  
TAU2 by Y12  
Y22 (12)  
Y32 (13);  
TAU3 by Y13  
Y23 (12)  
Y33 (13);  
TAU4 by Y14  
Y24 (12)  
Y34 (13);  
[Y11@0 Y12@0 Y13@0 Y14@0];  
[Y21 Y22 Y23 Y24] (a2);  
[Y31 Y32 Y33 Y34] (a3);  
Y11-Y14 (e1);  
Y21-Y24 (e2);  
Y31-Y34 (e3);  
KSI by TAU1-TAU4@1;  
[KSI];  
KSI (KSIVAR);  
TAU1-TAU4 (ZETAVAR); 
```

It can be seen that the Mplus specification of the measurement (first-order) part of the model exactly parallels the specification of the LS model with strict ME (equal factor loadings, intercepts, and measurement error variances). The structural or latent variable (second-order) part of the model specifies that the trait factor $\xi$ is measured by the first-order latent state factors $\tau _ { t } ,$ where each unstandardized second-order factor loading is set equal to unity (KSI by TAU1-TAU4@1;). The trait factor mean is estimated by specifying [KSI];. Furthermore, the trait factor variance (which is estimated by default in Mplus) is given the label (KSIVAR), so that this parameter can be used for computing the Con, Ospe, and Rel coefficients through the MODEL CONSTRAINT option (see discussion below). The latent state residual variances $V a r ( \zeta )$ were set equal across time for simplicity in this example (this restriction is not generally necessary, but if tenable, it simplifies the computation of the Con and Ospe coefficients in the STMS model). 

# BOX 5.4. Specifying an STMS Model as a Bifactor Model

An STMS model that is in line with LST-R theory can also be specified as a bifactor (nested factor) model. The hierarchical (second- order factor) specification of the STMS model discussed in the main text is not generally equivalent to the bifactor specification described in this box. Instead, the bifactor specification is generally less restrictive than the hierarchical specification and may thus be preferred in certain practical situations. In the bifactor specification of the STMS model, the latent state factors $\tau _ { t }$ are omitted and each measured variable directly loads onto the common trait factor $\xi$ as well as an occasion- specific state residual factor $\zeta _ { t } .$ In this specification, the factor loadings can differ for the trait and state residual factors such that the following measurement equation is obtained: 

$$
Y _ {i t} = \alpha_ {i t} + \lambda_ {i t} \cdot \xi + \delta_ {i t} \cdot \zeta_ {t} + \varepsilon_ {i t}
$$

Here, $\delta _ { i t }$ denotes the factor loading on the state residual factors. Note that $\delta _ { i t }$ can differ from the trait loading $\lambda _ { i t }$ for a given variable. This is not allowed in the hierarchical STMS specification. Time invariance of the ${ \bf \mathfrak { a } } _ { i t } .$ , $\lambda _ { i t } ,$ and $\delta _ { i t }$ parameters is typically assumed in this model. 

The Mplus specification of the bifactor STMS model version with timeinvariant intercepts and loadings is given below: 

```txt
MODEL:  
KSI by Y11  
Y21 (12)  
Y31 (13);  
Y12@1  
Y22 (12)  
Y32 (13);  
Y13@1  
Y23 (12)  
Y33 (13);  
Y14@1  
Y24 (12)  
Y34 (13);  
ZETA1 by Y11  
Y21 (d2)  
Y31 (d3);  
ZETA2 by Y12  
Y22 (d2)  
Y32 (d3); 
```

(continued on page 180) 

```txt
ZETA3 by Y13  
Y23 (d2)  
Y33 (d3);  
ZETA4 by Y14  
Y24 (d2)  
Y34 (d3);  
[Y11@0 Y12@0 Y13@0 Y14@0];  
[Y21 Y22 Y23 Y24] (a2);  
[Y31 Y32 Y33 Y34] (a3);  
Y11-Y14 (e1);  
Y21-Y24 (e2);  
Y31-Y34 (e3);  
[KSI];  
KSI (KSIVAR);  
ZETA1-ZETA4 (ZETAVAR);  
ZETA1-ZETA4 with KSI@0 ZETA1-ZETA4@0; 
```

The STMS model with strict ME and equal latent state residual variances fits the data well, $\chi ^ { 2 } ( 8 0 , N = 3 0 0 ) = 7 3 . 5 3 9$ , $p = . 6 8$ , $R M S E A = 0 . 0 0$ , $C F I = 1 . 0 0$ , $S R M R = 0 . 0 3$ . This indicates that the means and covariances of the LS variables in this example are in line with a unidimensional (single higher- order factor) structure. Recall that the STMS model with all second- order factor loadings fixed to 1 implies equal means and equal covariances of all latent state variables in the population. This condition was met here. Selected standardized parameter estimates are printed below (the full Mplus output is available from the companion website [see the box at the end of the table of contents]): 

```txt
STANDARDIZED MODEL RESULTS (STDYX Standardization) Two-Tailed P-Value  
Estimate S.E. Est./S.E.  
TAU1 BY  
Y11 0.942 0.006 166.722 0.000  
Y21 0.891 0.009 98.162 0.000  
Y31 0.889 0.009 96.735 0.000  
TAU2 BY  
Y12 0.942 0.006 166.722 0.000  
Y22 0.891 0.009 98.162 0.000  
Y32 0.889 0.009 96.735 0.000  
TAU3 BY  
Y13 0.942 0.006 166.722 0.000  
Y23 0.891 0.009 98.162 0.000  
Y33 0.889 0.009 96.735 0.000 
```

<table><tr><td colspan="6">TAU4 BY</td></tr><tr><td>Y14</td><td></td><td>0.942</td><td>0.006</td><td>166.722</td><td>0.000</td></tr><tr><td>Y24</td><td></td><td>0.891</td><td>0.009</td><td>98.162</td><td>0.000</td></tr><tr><td>Y34</td><td></td><td>0.889</td><td>0.009</td><td>96.735</td><td>0.000</td></tr><tr><td colspan="6">KSI BY</td></tr><tr><td>TAU1</td><td></td><td>0.957</td><td>0.005</td><td>190.996</td><td>0.000</td></tr><tr><td>TAU2</td><td></td><td>0.957</td><td>0.005</td><td>190.996</td><td>0.000</td></tr><tr><td>TAU3</td><td></td><td>0.957</td><td>0.005</td><td>190.996</td><td>0.000</td></tr><tr><td>TAU4</td><td></td><td>0.957</td><td>0.005</td><td>190.996</td><td>0.000</td></tr><tr><td colspan="6">Means</td></tr><tr><td>KSI</td><td></td><td>7.396</td><td>0.325</td><td>22.784</td><td>0.000</td></tr><tr><td colspan="6">Intercepts</td></tr><tr><td>Y11</td><td></td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y12</td><td></td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y13</td><td></td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y14</td><td></td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y21</td><td></td><td>-1.300</td><td>0.115</td><td>-11.290</td><td>0.000</td></tr><tr><td>Y22</td><td></td><td>-1.300</td><td>0.115</td><td>-11.290</td><td>0.000</td></tr><tr><td>Y23</td><td></td><td>-1.300</td><td>0.115</td><td>-11.290</td><td>0.000</td></tr><tr><td>Y24</td><td></td><td>-1.300</td><td>0.115</td><td>-11.290</td><td>0.000</td></tr><tr><td>Y31</td><td></td><td>-6.292</td><td>0.207</td><td>-30.401</td><td>0.000</td></tr><tr><td>Y32</td><td></td><td>-6.292</td><td>0.207</td><td>-30.401</td><td>0.000</td></tr><tr><td>Y33</td><td></td><td>-6.292</td><td>0.207</td><td>-30.401</td><td>0.000</td></tr><tr><td>Y34</td><td></td><td>-6.292</td><td>0.207</td><td>-30.401</td><td>0.000</td></tr><tr><td colspan="6">Variances</td></tr><tr><td>KSI</td><td></td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td colspan="6">Residual Variances</td></tr><tr><td>Y11</td><td></td><td>0.112</td><td>0.011</td><td>10.505</td><td>0.000</td></tr><tr><td>Y12</td><td></td><td>0.112</td><td>0.011</td><td>10.505</td><td>0.000</td></tr><tr><td>Y13</td><td></td><td>0.112</td><td>0.011</td><td>10.505</td><td>0.000</td></tr><tr><td>Y14</td><td></td><td>0.112</td><td>0.011</td><td>10.505</td><td>0.000</td></tr><tr><td>Y21</td><td></td><td>0.207</td><td>0.016</td><td>12.797</td><td>0.000</td></tr><tr><td>Y22</td><td></td><td>0.207</td><td>0.016</td><td>12.797</td><td>0.000</td></tr><tr><td>Y23</td><td></td><td>0.207</td><td>0.016</td><td>12.797</td><td>0.000</td></tr><tr><td>Y24</td><td></td><td>0.207</td><td>0.016</td><td>12.797</td><td>0.000</td></tr><tr><td>Y31</td><td></td><td>0.210</td><td>0.016</td><td>12.877</td><td>0.000</td></tr><tr><td>Y32</td><td></td><td>0.210</td><td>0.016</td><td>12.877</td><td>0.000</td></tr><tr><td>Y33</td><td></td><td>0.210</td><td>0.016</td><td>12.877</td><td>0.000</td></tr><tr><td>Y34</td><td></td><td>0.210</td><td>0.016</td><td>12.877</td><td>0.000</td></tr><tr><td>TAU1</td><td></td><td>0.085</td><td>0.010</td><td>8.822</td><td>0.000</td></tr><tr><td>TAU2</td><td></td><td>0.085</td><td>0.010</td><td>8.822</td><td>0.000</td></tr><tr><td>TAU3</td><td></td><td>0.085</td><td>0.010</td><td>8.822</td><td>0.000</td></tr><tr><td>TAU4</td><td></td><td>0.085</td><td>0.010</td><td>8.822</td><td>0.000</td></tr><tr><td colspan="6">R-SQUARE</td></tr><tr><td>Observed</td><td></td><td></td><td></td><td></td><td>Two-Tailed</td></tr><tr><td>Variable</td><td>Estimate</td><td></td><td>S.E.</td><td>Est./S.E.</td><td>P-Value</td></tr><tr><td>Y11</td><td>0.888</td><td></td><td>0.011</td><td>83.361</td><td>0.000</td></tr><tr><td>Y12</td><td>0.888</td><td></td><td>0.011</td><td>83.361</td><td>0.000</td></tr></table>

<table><tr><td>Y13</td><td>0.888</td><td>0.011</td><td>83.361</td><td>0.000</td></tr><tr><td>Y14</td><td>0.888</td><td>0.011</td><td>83.361</td><td>0.000</td></tr><tr><td>Y21</td><td>0.793</td><td>0.016</td><td>49.081</td><td>0.000</td></tr><tr><td>Y22</td><td>0.793</td><td>0.016</td><td>49.081</td><td>0.000</td></tr><tr><td>Y23</td><td>0.793</td><td>0.016</td><td>49.081</td><td>0.000</td></tr><tr><td>Y24</td><td>0.793</td><td>0.016</td><td>49.081</td><td>0.000</td></tr><tr><td>Y31</td><td>0.790</td><td>0.016</td><td>48.367</td><td>0.000</td></tr><tr><td>Y32</td><td>0.790</td><td>0.016</td><td>48.367</td><td>0.000</td></tr><tr><td>Y33</td><td>0.790</td><td>0.016</td><td>48.367</td><td>0.000</td></tr><tr><td>Y34</td><td>0.790</td><td>0.016</td><td>48.367</td><td>0.000</td></tr><tr><td>Latent</td><td></td><td></td><td></td><td>Two-Tailed</td></tr><tr><td>Variable</td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>P-Value</td></tr><tr><td>TAU1</td><td>0.915</td><td>0.010</td><td>95.498</td><td>0.000</td></tr><tr><td>TAU2</td><td>0.915</td><td>0.010</td><td>95.498</td><td>0.000</td></tr><tr><td>TAU3</td><td>0.915</td><td>0.010</td><td>95.498</td><td>0.000</td></tr><tr><td>TAU4</td><td>0.915</td><td>0.010</td><td>95.498</td><td>0.000</td></tr></table>

It can be seen that all observed variables $Y _ { i t }$ had high standardized loadings on their respective state factors, indicating decent reliabilities. The actual reliability coefficients (the standardized loadings squared) are printed under R-SQUARE Observed Variable and are all ≥ .79. The latent state variables $\tau _ { t }$ also had high standardized loadings (.957) on the second-order trait factor $\xi .$ . This reflects the fact that all LS factors were highly correlated (as shown in the application of the LS model to the same data above) and indicates that the construct under study was mostly trait-like. 

The squared standardized state factor loadings are equal to the $C o n ( \tau _ { t } )$ coefficients and are printed under R-SQUARE Latent Variable. All $C o n ( \tau _ { t } )$ coefficients are equal to .915, indicating high consistency across time. The $O s p ( \tau _ { t } )$ coefficients are equal to $1 - C o n ( \tau _ { t } ) = . 0 8 5$ and are given as standardized residual variances for the $\tau _ { t }$ variables in Mplus. They indicate low occasion specificity of the states. In summary, $9 1 . 5 \%$ of the latent state variability at each time point reflected trait variance, whereas only $8 . 5 \%$ reflected state residual (situation and/or person $\times$ situation interaction) variance. 

Mplus does not print the $C o n ( Y _ { i t } )$ and $O s p ( Y _ { i t } )$ coefficients for the observed variables by default. However, these coefficients can be manually computed using the MODEL CONSTRAINT option. For this purpose, the factor loadings, measurement error variances, trait variance, and state residual variances have to be labeled in the Mplus MODEL statement as shown above. Then, these parameters can be used in MODEL CONSTRAINT to define the Con, Ospe, and Rel coefficients as “new” parameters [the Rel coefficients are defined here merely to check whether the $C o n ( Y _ { i t } )$ and $O s p ( Y _ { i t } )$ coefficients properly add up to the reliability coefficients that Mplus gives under R-SQUARE Observed Variable]: 

```matlab
MODEL:  
...  
MODEL CONSTRAINT:  
NEW(CONY1 CONY2 CONY3  
OSPEY1 OSPEY2 OSPEY3  
RELY1 RELY2 RELY3);  
CONY1 = KSVAR/(KSVAR + ZETAVAR + e1);  
CONY2 = (12**2) * KSVAR / ((12**2) * KSVAR + (12**2) * ZETAVAR + e2);  
CONY3 = (13**2) * KSVAR / ((13**2) * KSVAR + (13**2) * ZETAVAR + e3);  
OSPY1 = ZETAVAR/(KSVAR + ZETAVAR + e1);  
OSPY2 = (12**2) * ZETAVAR / ((12**2) * KSVAR + (12**2) * ZETAVAR + e2);  
OSPY3 = (13**2) * ZETAVAR / ((13**2) * KSVAR + (13**2) * ZETAVAR + e3);  
RELY1 = CONY1 + OSPEY1;  
RELY2 = CONY2 + OSPEY2;  
RELY3 = CONY3 + OSPEY3; 
```

In our example, it is sufficient to define each coefficient only once for each variable, because of the restrictions that imply strict ME and equal state residual variances across time. Because of these restrictions, the coefficients are time-invariant for each measured variable. In the more general case, in which measurement error or state residual variances may vary across time, more than one coefficient would need to be computed for each measured variable. After re-running the Mplus input file with the newly added MODEL CONSTRAINT command, the Con, Ospe, and Rel coefficients are printed under NEW/Additional Parameters in the Mplus MODEL RESULTS section: 

```powershell
MODEL RESULTS Estimate S.E. Est./S.E. Two-Tailed P-Value New/Additional Parameters CONY1 0.813 0.015 54.862 0.000 CONY2 0.726 0.020 36.944 0.000 CONY3 0.723 0.020 36.600 0.000 OSPEY1 0.075 0.008 9.076 0.000 OSPEY2 0.067 0.007 9.529 0.000 OSPEY3 0.067 0.007 9.531 0.000 RELY1 0.888 0.011 83.361 0.000 RELY2 0.793 0.016 49.081 0.000 RELY3 0.790 0.016 48.367 0.000 
```

Notice that the reliability estimates match the estimates given in the Mplus default output. This shows us that our $C o n ( Y _ { i t } )$ and $O s p ( Y _ { i t } )$ computations were accurate. As expected based on the $C o n ( \tau _ { t } )$ and $O s p ( \tau _ { t } )$ estimates already discussed above, the measures reflected mostly trait variance (Con coefficients ≥ .723) rather than state residual variance as indicated by the much higher Con as compared to the corresponding Ospe coefficients (Ospe coefficients ≤ .075). We can thus conclude that the construct under study in this example is for 

the most part trait-like (there is little fluctuation of true individual differences across time). 

# 5.4.2.5 Summary

The STMS model is a prototypical LST model that allows decomposing the observed score variability into trait, state residual, and measurement error components. The STMS model can be seen as a special case of the LS model, in which the LS variables are restricted to have equal means and equal covariances across time. It can also be seen as a multiple-indicator extension of the random intercept model (Chapter 2), in which state residual latent variables have been added to account for potential situation and/or person $\times$ situation interaction effects in addition to stable trait and random measurement error influences. 

In contrast to the LAS model (which also represents a special case of the LS model), the STMS model restricts the mean and covariance structure of the LS variables in a different way. The LAS model assumes that the state covariances follow an autoregressive structure. For example, in a first-order autoregressive process, it is implied that covariances between states become smaller as the time interval becomes larger. 

In contrast, the STMS model with a stable trait $\xi$ requires all pairs of LS variables to have the same covariance in the population, regardless of how closely they are spaced in time. Hence, the LAS and STMS models imply a different longitudinal process. The first-order LAS model implies that the influence of the (initial) trait diminishes over time, whereas the STMS model with equal trait factor loadings implies that the trait influence stays the same over time and that states can vary only because of momentary situation or person $\times$ situation interaction influences, but not because of trait changes or changing trait influences. 

The STMS model with equal loadings thus assumes a longitudinal process of trait stability (i.e., individual trait scores do not change across time). The model furthermore assumes that there may be true fluctuations of state scores around the stable trait scores (“state variability”). That is, individual’s true scores may vary across time. However, according to the model, such intraindividual variation in true scores could only be due to situational influences and/or person $\times$ situation interactions (not trait changes). Later in this chapter, I discuss several LST-R models that relax the assumption of no trait change across time. 

A state variability process with a stable trait component is reasonable for many social science constructs (e.g., mood, anxiety, depression), especially when those constructs are examined over a rather short period of time. Through the Con and Ospe coefficients (which can be calculated based on the estimated 

parameters of the model), the STMS model allows quantifying to which extent a given set of measures reflects a trait- versus state-like construct. This can be an important step in construct validation as well as theory testing. The STMS model also allows estimating the reliability of the measures at each time point. 

One limitation of the STMS model is that it implies perfect latent state mean and covariance stability and that the entire stability in the latent states is explained by the trait factor. This could be viewed as a process of “long-term” stability in the trait scores. In practice, however, there often is short-term stability in the states in addition to long-term trait stability. That is, adjacent latent 

# BOX 5.5. STMS Models without versus with Autoregressive Effects

Recall that in my discussion of the TSE model in Chapter 3, I highlighted the fact that one of the strengths of the TSE model is that it accounts for so- called carryover effects between adjacent situations by means of including autoregressive effects $( \delta _ { \mathrm { l } } )$ between adjacent occasion residual latent variables. The STMS model that I described in the text assumes that there are no autoregressive effects among either latent state or latent state residual variables. In fact, it can be seen as one of the strengths of multiple- indicator LST models that they do not require the presence of an autoregressive structure to be mathematically identified (the single- indicator TSE model described in Chapter 3 becomes underidentified when the autoregressive parameter $\delta _ { \mathrm { l } }$ goes to zero). Multipleindicator LST models thus have a special advantage in studies that use long time intervals between measurement occasions (e.g., one measurement occasion per year across five years) for which autoregressive effects may not be observed. In such situations, the TSE model would likely fail due to empirical underidentification, whereas multiple- indicator LST models without autoregression could still be estimated. 

When the time lag between measurement occasions is smaller (e.g., one or more measurement occasions per day or week), autoregressive effects are likely to be present. If such effects are present, the STMS model described in the text would be misspecified. As a consequence, it may not fit well and/or return biased parameter estimates (e.g., an overestimated latent trait factor variance). Steyer and Schmitt (1994) as well as Cole and colleagues (Cole et al., 2005; LaGrange & Cole, 2008) presented different versions of the STMS model with autoregressive effects among either latent state or latent state residual/occasion residual variables. Prenoveau (2016) discussed the Mplus specification of these model versions in detail so that I do not include a detailed discussion here. The online supplemental materials feature an Mplus input file for a multitrait– multistate model with autoregression that I describe briefly in Box 5.8. 

state variables are often more strongly correlated than state variables that are further spaced out in time. This phenomenon is at odds with the equal state covariances implication of the STMS model. In addition, the STMS model with equal loadings and intercepts does not allow for mean changes in the states across time. In Box 5.5, I provide references to STMS models with autoregression that address this limitation. 

The STMS model has one other important limitation: It requires unidimensionality of the indicators that are measured at the same time point. That is, the measured variables at a given point in time are assumed to measure perfectly correlated latent state variables $\tau _ { i t }$ at a given measurement occasion that are only allowed to differ in scaling $( { \bf \alpha } _ { a _ { i t } }$ and $\lambda _ { i t } )$ . In practice, indicators often measure latent state variables that differ beyond scaling. Slight differences in item wording, the use of both positively and negatively keyed items, multifaceted constructs, or method effects can cause violations of the homogeneity assumption made in the STMS model. I discussed this same issue previously in Chapter 4 for the LS model. The following extended LST models address this limitation. 

# 5.4.3 The STMS Model with Indicator‑Specific Residual Factors

# 5.4.3.1 Introduction

One way to address the issue of indicator heterogeneity in LST analyses is to pursue an approach similar to the LS-IS approach that I described in Chapter 4, Section 4.3. In this approach, so-called indicator-specific (IS) residual or method factors are added to the model for all but one reference indicator (Eid et al., 1999). I refer to this extended model as the STMS-IS model. As in the LS-IS approach, the IS factors in the STMS-IS model reflect variability in the nonreference indicators that is not shared with the reference indicator. 

Below, I focus on the specification and interpretation of the STMS-IS model. In Chapter 4, Section 4.3, I provided insights into the issue of selecting an appropriate reference indicator within the LS-IS approach. The same recommendations apply to the STMS-IS model as well, so that I do not reiterate them here. 

# 5.4.3.2 Model Description

Without loss of generality, I again select the first indicator $( i = 1 )$ as the reference indicator. For the reference indicator, no IS factor is included. For all remaining 

indicators, indicator-specific factors $I S _ { i }$ are specified. In summary, the STMS-IS model can be described by the following measurement equation: 

$$
Y _ {i t} = \left\{ \begin{array}{l} \tau_ {1 t} + \varepsilon_ {1 t} \text {f o r} i = 1 \\ \alpha_ {i t} + \lambda_ {i t} \cdot \tau_ {1 t} + I S _ {i} + \varepsilon_ {i t} \text {f o r} i \neq 1 \end{array} \right.
$$

Note that the measurement equation is identical to the measurement equation in the LS-IS model (compare Section 4.3). The structural (latent variable) model in the STMS-IS model parallels the structural model in the STMS model without IS factors: 

$$
\tau_ {1 t} = \xi_ {1} + \zeta_ {1 t}
$$

The latent state variables pertaining to the reference indicator $( \tau _ { 1 t } )$ are decomposed into a commont trait $( \xi _ { 1 } )$ factor that is specific to the reference variable and state residual components $( \zeta _ { 1 t } )$ . By inserting the structural model equation into the time-specific measurement equation, we obtain the complete decomposition of the measured variables in the STMS-IS model: 

$$
Y _ {i t} = \left\{ \begin{array}{l} \xi_ {1} + \zeta_ {1 t} + \varepsilon_ {1 t} \text {f o r} i = 1 \\ \alpha_ {i t} + \lambda_ {i t} \cdot \xi_ {1} + \lambda_ {i t} \cdot \zeta_ {1 t} + I S _ {i} + \varepsilon_ {i t} \text {f o r} i \neq 1 \end{array} \right.
$$

Notice that all indicators now load onto the trait and state residual variables that are specific to the reference indicator. In addition, the non-reference indicators load onto their own indicator-specific factor $I S _ { i }$ with a fixed loading of $+ 1$ . In summary, the STMS model (without any invariance restrictions) estimates the following parameters: 

•	 one reference trait factor mean $E ( \xi _ { 1 } )$ 

•	 one reference trait factor variance Var $( \xi _ { 1 } )$ , 

•	 n reference state residual factor variances Var $( \zeta _ { 1 t } )$ , 

• $m - 1$ indicator-specific factor variances Var(ISi), 

• $0 . 5 ( m - 1 ) ( m - 2 )$ indicator-specific factor covariances $C o v ( I S _ { i } , I S _ { j } ) , i \colon$ $i \neq j$ 

• $n ( m - 1 )$ constant intercepts ${ \mathfrak { a } } _ { { \mathfrak { i } } t }$ (the intercept pertaining the reference indicator is fixed to 0 on each measurement occasion), 

• $n ( m - 1 )$ constant factor loadings $\lambda _ { _ { i t } }$ (the loading pertaining the reference indicator is fixed to 1 on each measurement occasion), and 

•	 nm measurement error variances $V a r ( \varepsilon _ { i t } )$ . 

# BOX 5.6. Defining the STMS‑IS Model Based on LST‑R Theory

The STMS-IS model can be seen as a combination between the LS-IS and STMS models. The assumptions that define the model based on LST-R theory are thus the same as the ones that I discussed above for the LS-IS and STMS models. As in the LS-IS approach, a reference measure is selected, and indicator- specific factors $I S _ { \mathrm { { i } } }$ are defined as linear regression residual factors for all non- reference indicators. Moreover, all reference trait variables are assumed to be identical, leading to a single- trait factor as in the STMS approach. The $I S _ { i }$ factors are assumed to be uncorrelated with all trait, state residual, and error variables. Trait, state residual, indicator- specific, and measurement error variables are assumed to be uncorrelated. The only correlations allowed are those between different $I S _ { i }$ factors. 

Therefore, the STMS-IS model in general (i.e., without any invariance restrictions) has $2 - n + 3 n m + m - 1 + 0 . 5 ( m ^ { 2 } - 3 m + 2 )$ free model parameters. For our example with three measures $( m = 3 )$ ) and four time points $( n = 4 )$ ), we obtain $2 - 4 + 3 \cdot 4 \cdot 3 + 2 + 1 = 3 7$ free model parameters. With three measures and four time points, we have 90 pieces of known information, and so the general STMS model has 53 df. In Box 5.6, I explain how the STMS-IS model can be defined based on the concepts of LST-R theory. 

# 5.4.3.3 Variance Decomposition and Coefficients

The latent variables $\xi _ { 1 }$ , $\zeta _ { 1 t } ,$ and $I S _ { i }$ are uncorrelated in the STMS-IS model. Furthermore, all error variables $\varepsilon _ { i t }$ are assumed to be uncorrelated with all latent variables and with one another. As a consequence, the following additive variance decompositions hold in the STMS-IS model: 

$$
V a r (\tau_ {i t}) = \left\{ \begin{array}{l} V a r (\xi_ {1}) + V a r (\zeta_ {1 t}) \text {f o r} i = 1 \\ \lambda_ {i t} ^ {2} \cdot V a r (\xi_ {1}) + \lambda_ {i t} ^ {2} \cdot V a r (\zeta_ {1 t}) + V a r (I S _ {i}) \text {f o r} i \neq 1 \end{array} \right.
$$

$$
\operatorname {V a r} (Y _ {i t}) = \left\{ \begin{array}{l} \operatorname {V a r} (\xi_ {1}) + \operatorname {V a r} (\zeta_ {1 t}) + \operatorname {V a r} (\varepsilon_ {1 t}) \text {f o r} i = 1 \\ \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} (\xi_ {1}) + \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} (\zeta_ {1 t}) + \operatorname {V a r} (I S _ {i}) + \operatorname {V a r} (\varepsilon_ {i t}) \text {f o r} i \neq 1 \end{array} \right.
$$

As in the STMS model, coefficients can be defined that allow quantifying to which degree the latent state and/or observed variables reflect trait effects (consistency, Con) or situation/person $\times$ situation interaction effects 

(occasion specificity, Osp). Furthermore, a reliability coefficient (Rel) can be defined for the observed variables. 

In contrast to the STMS model, the STMS-IS model allows decomposing the total consistency (Con) into two parts (Geiser & Lockhart, 2012): one part that is shared with the reference measure (common consistency, CCon) and one part that is unique to a (non-reference) measure (unique consistency, UCon): 

$$
C _ {o n} = C C _ {o n} + U C _ {o n}
$$

where 

$$
\begin{array}{l} C C o n \left(\boldsymbol {\tau} _ {i t}\right) = \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} \left(\xi_ {1}\right) / \operatorname {V a r} \left(\boldsymbol {\tau} _ {i t}\right) \\ U C o n \left(\tau_ {i t}\right) = V a r \left(I S _ {i}\right) / \text {V a r} \left(\tau_ {i t}\right) \\ C C o n \left(Y _ {i t}\right) = \lambda_ {i t} ^ {2} \cdot V a r \left(\xi_ {1}\right) / V a r \left(Y _ {i t}\right) \\ U C o n \left(Y _ {i t}\right) = V a r \left(I S _ {i}\right) / V a r \left(Y _ {i t}\right) \\ \end{array}
$$

Whereas the CCon coefficient indicates the proportion of trait variance that is shared with the reference indicator, UCon indicates the proportion of trait variance that is explained by the indicator-specific factor $I S _ { i }$ , which can be seen as an indicator-specific residual trait factor. The Con coefficient gives the total amount of trait variability, that is, variability that is due to either $\xi _ { 1 }$ or $I S _ { i }$ . 

The occasion specificity and reliability coefficients are defined in the same way as in the STMS model: 

$$
\begin{array}{l} O s p \left(\tau_ {i t}\right) = \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} \left(\zeta_ {t}\right) / \operatorname {V a r} \left(\tau_ {i t}\right) \\ O s p \left(Y _ {i t}\right) = \lambda_ {i t} ^ {2} \cdot \operatorname {V a r} \left(\zeta_ {t}\right) / \operatorname {V a r} \left(Y _ {i t}\right) \\ R e l \left(Y _ {i t}\right) = \left[ \lambda_ {i t} ^ {2} \cdot V a r \left(\xi_ {1}\right) + \lambda_ {i t} ^ {2} \cdot V a r \left(\zeta_ {t}\right) + V a r \left(I S _ {i}\right) \right] / V a r \left(Y _ {i t}\right) \\ = V a r \left(\tau_ {i t}\right) / V a r \left(Y _ {i t}\right) \\ = 1 - \left[ \operatorname {V a r} \left(\varepsilon_ {i t}\right) / \operatorname {V a r} \left(Y _ {i t}\right) \right] \\ = C C o n \left(Y _ {i t}\right) + U C o n \left(Y _ {i t}\right) + O s p \left(Y _ {i t}\right) \\ \end{array}
$$

The occasion-specificity Osp coefficients again give the proportion of latent state or observed variance that is due to situation and/or person $\times$ situation interaction effects. As usual, the Rel coefficient gives the proportion of observed variance that reflects true score (systematic) variance, that is, the sum of all systematic sources of variance. 

Mplus by default only prints the reliability coefficients for the observed variables (under R-SQUARE Observed Variable) as well as the $C o n ( \tau _ { 1 t } )$ 

and $O s p ( \tau _ { 1 t } )$ coefficients for the reference latent state variables. [The $C o n ( \tau _ { 1 t } )$ coefficients are printed under R-SQUARE Latent Variable, whereas the $O s p ( \tau _ { 1 t } )$ coefficients are given as the standardized residual variances for the $\tau _ { \mathrm { l } t }$ variables.] In the complete Mplus input file for the STMS-IS model that is available from the companion website (see the box at the end of the table of contents), I demonstrate how all other coefficients described above can be computed manually in Mplus using the MODEL CONSTRAINT option. 

# 5.4.3.4 Mplus Application

I applied the STMS-IS model to the same data set that I used to illustrate the LS-IS model in Chapter 4 (three cognitive ability tests measured on four measurement occasions). The Mplus MODEL command for the STMS-IS model represents a blend of the LS-IS and STMS MODEL statements and is therefore not printed here to avoid redundancies. It is, however, available from the companion website (see the box at the end of the table of contents), including the relevant MODEL CONSTRAINT commands for obtaining the CCon, UCon, Con, and Osp coefficients. 

The STMS-IS model with strict ME and equal latent state residual variances fits the LS-IS data well, $\chi ^ { 2 } ( 7 7 , N = 3 0 0 ) = 7 1 . 9 8 8$ , $p = . 6 4$ , $R M S E A = 0 . 0 0$ , CFI $= 1 . 0 0$ , $S R M R = 0 . 0 3 6$ . Notice that the STMS-IS model is more parsimonious than the LS-IS model with strict ME and equal LS factor variances, which had only 69 df. This is because the LS-IS model estimates four latent state factor means, four latent state factor variances, and all six covariances between LS factors. In contrast, the STMS-IS model only estimates one trait factor mean, one trait factor variance, and four latent state residual factor variances. Therefore, the STMS-IS model here has eight more df than the LS-IS model. Below, I focus on the estimated CCon, UCon, Con, and Osp coefficients in the STMS-IS model, which were obtained through MODEL CONSTRAINT. The full Mplus output file is available from the companion website (see the box at the end of the table of contents). 

<table><tr><td colspan="5">MODEL RESULTS</td></tr><tr><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-Tailed P-Value</td></tr><tr><td>...</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="5">New/Additional Parameters</td></tr><tr><td>CCONTAU1</td><td>0.916</td><td>0.011</td><td>87.148</td><td>0.000</td></tr><tr><td>CCONTAU2</td><td>0.782</td><td>0.024</td><td>32.083</td><td>0.000</td></tr><tr><td>CCONTAU3</td><td>0.580</td><td>0.038</td><td>15.288</td><td>0.000</td></tr><tr><td>UCONTAU1</td><td>0.000</td><td>0.000</td><td>0.000</td><td>1.000</td></tr><tr><td>UCONTAU2</td><td>0.146</td><td>0.021</td><td>6.844</td><td>0.000</td></tr><tr><td>UCONTAU3</td><td>0.366</td><td>0.038</td><td>9.674</td><td>0.000</td></tr><tr><td>CONTAU1</td><td>0.916</td><td>0.011</td><td>87.148</td><td>0.000</td></tr><tr><td>CONTAU2</td><td>0.928</td><td>0.008</td><td>109.706</td><td>0.000</td></tr><tr><td>CONTAU3</td><td>0.947</td><td>0.006</td><td>156.286</td><td>0.000</td></tr><tr><td>OSPTAU1</td><td>0.084</td><td>0.011</td><td>8.009</td><td>0.000</td></tr><tr><td>OSPTAU2</td><td>0.072</td><td>0.008</td><td>8.498</td><td>0.000</td></tr><tr><td>OSPTAU3</td><td>0.053</td><td>0.006</td><td>8.805</td><td>0.000</td></tr><tr><td>CCONY1</td><td>0.813</td><td>0.015</td><td>54.119</td><td>0.000</td></tr><tr><td>CCONY2</td><td>0.624</td><td>0.027</td><td>22.831</td><td>0.000</td></tr><tr><td>CCONY3</td><td>0.458</td><td>0.035</td><td>13.013</td><td>0.000</td></tr><tr><td>UCONY1</td><td>0.000</td><td>0.000</td><td>0.000</td><td>1.000</td></tr><tr><td>UCONY2</td><td>0.116</td><td>0.016</td><td>7.063</td><td>0.000</td></tr><tr><td>UCONY3</td><td>0.289</td><td>0.028</td><td>10.239</td><td>0.000</td></tr><tr><td>CONY1</td><td>0.813</td><td>0.015</td><td>54.119</td><td>0.000</td></tr><tr><td>CONY2</td><td>0.741</td><td>0.019</td><td>38.445</td><td>0.000</td></tr><tr><td>CONY3</td><td>0.747</td><td>0.018</td><td>41.026</td><td>0.000</td></tr><tr><td>OSPY1</td><td>0.075</td><td>0.009</td><td>8.056</td><td>0.000</td></tr><tr><td>OSPY2</td><td>0.057</td><td>0.006</td><td>8.952</td><td>0.000</td></tr><tr><td>OSPY3</td><td>0.042</td><td>0.005</td><td>9.017</td><td>0.000</td></tr><tr><td>RELY1</td><td>0.887</td><td>0.012</td><td>75.168</td><td>0.000</td></tr><tr><td>RELY2</td><td>0.798</td><td>0.017</td><td>47.023</td><td>0.000</td></tr><tr><td>RELY3</td><td>0.789</td><td>0.018</td><td>45.098</td><td>0.000</td></tr></table>

It can be seen that, overall, consistency estimates were high for all three measures [all $C o n ( \tau _ { i t } )$ coefficients $\geq$ .916], and occasion specificities were low [all $O s p ( \tau _ { i t } )$ coefficients $\leq . 0 8 4 ]$ , indicating that all measures reflected a strongly trait-like construct. The third measure showed a relatively high amount of unique (indicator-specific) consistency $[ U C o n ( \tau _ { 3 } ) = . 3 6 6 ]$ , indicating that its trait components differed considerably from the reference indicator. All measures were fairly reliable $[ R e l ( Y _ { i t } )$ estimates ≥ .789]. 

# 5.4.3.5 Summary

The STMS-IS model represents an extension of the STMS model in which indicator heterogeneity is modeled in the same way as in the LS-IS approach. The STMS-IS model is more general than the STMS model, which is only appropriate for strictly unidimensional measures (e.g., parallel cortisol measurements or very homogeneous test items). In most social science applications that use questionnaire data or somewhat heterogeneous test items, a certain degree of indicator-specific trait variance has to be expected. For less than perfectly unidimensional measures, the STMS-IS model is a good alternative to the more restrictive STMS model. In contrast to the LS-IS model, the STMS-IS model allows for a separation of trait and state residual components as in the STMS model. 

The $I S _ { i }$ factors in the STMS-IS approach can be interpreted as residual trait factors. These factors reflect unique trait variance that a given measure does not share with the reference measure. By including $I S _ { i }$ factors, the STMS-IS model allows for a more complex variance decomposition as well as the distinction between common, unique, and total consistency coefficients. The STMS-IS model therefore allows examining the convergent validity of trait effects relative to a reference measure. High values of the CCon coefficients indicate that measures show high convergent validity with regard to the trait that is being measured, whereas high UCon values indicate that the trait components reflected in different measures are rather distinct. In the next section, I present an alternative approach to modeling indicator heterogeneity in latent state–trait analyses. 

# 5.4.4 The Multitrait–Multistate Model

# 5.4.4.1 Introduction

Another, very efficient way of accounting for indicator heterogeneity in LST analyses is to specify separate (indicator-specific) trait factors for each indicator rather than a single-trait factor. Because of the use of multiple traits (one for each measured variable), this approach is often referred to as the multitrait–multistate (MTMS) model or LST model with indicator-specific traits (Eid, 1995, 1996; Geiser & Lockhart, 2012). 

# 5.4.4.2 Model Description

In the MTMS model (see Figure 5.5), no indicator-specific residual (IS) factors are specified. Instead, discrepancies between indicators (i.e., a lack of unidimensionality) are reflected in the fact that each indicator has its own indicatorspecific trait factor $\xi _ { i }$ . All indicator-specific trait factors are allowed to correlate. The correlations between trait factors are freely estimated and need not be perfect (1.0), as is implied in the STMS model without IS factors (see Section 5.4.2). The lower the correlations between indicator-specific traits in the MTMS model, the greater the degree of heterogeneity (method effects) of indicators. Conversely, high correlations between $\xi _ { i }$ factors (i.e., correlations around .8 or .9) indicate that indicators are to a large extent measuring the same trait (i.e., that they show high convergent validity). 

The indicator-specific trait factors $\xi _ { i }$ also have their own means $E ( \xi _ { i } )$ and variances $V a r ( \xi )$ as parameters to be estimated. As a consequence, variables can differ in their metrics (origin and units of measurement) in the MTMS model without estimating different measurement intercepts ${ \mathfrak { a } } _ { i t }$ or trait factor loadings 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/cb34c3a05b61d4e3cdf47ed0bf73feb755641401606576737474590a88f09120.jpg)



FIGURE 5.5. Path diagram of a multitrait–multistate (MTMS) model for three observed variable $Y _ { i t }$ that are measured on four time points. $\xi _ { \mathrm { i } } =$ indicator-specific latent trait factor; $\zeta _ { t } =$ latent state residual variable; $\varepsilon _ { i t } =$ measurement error variable; $\delta _ { \mathrm { i } } =$ constant state residual factor loading. All trait factors can be correlated.


$\lambda _ { { _ i t } }$ for different indicators. Instead, all intercepts are set to zero and all trait factor loadings are set to unity in the model. Time-invariant factor loadings $( \delta _ { i } )$ are only estimated for the state residual factors $\zeta _ { t }$ as expressed by the following MTMS measurement model equation: 

$$
Y _ {i t} = \boldsymbol {\zeta} _ {i} + \boldsymbol {\delta} _ {i} \cdot \boldsymbol {\zeta} _ {t} + \varepsilon_ {i t}
$$

For indicators that share the same units of measurement, researchers often choose to also fix the $\delta _ { i }$ loadings to unity for all indicators, as loadings in this case are unlikely to differ between indicators. Fixing all loadings to unity further increases model parsimony and is theoretically meaningful in cases in which indicators do not differ in their units of measurement. 

In summary, the MTMS model allows estimating the following parameters: 

•	 m trait factor means $E ( \xi _ { i } )$ , 

•	 m trait factor variances $V a r ( \xi )$ 

• $0 . 5 ( m ^ { 2 } - m )$ trait factor covariances $C o v ( \xi _ { i } , \xi _ { j } ) , i \neq j .$ 

•	 n state residual factor variances $V a r ( \zeta )$ , 

• $m - 1$ time-invariant state residual factor loadings $\delta _ { i }$ (often not needed for indicators that are measured in the same units of measurement), and 

•	 nm measurement error variances $V a r ( \varepsilon _ { i t } )$ . 

# BOX 5.7. Defining the MTMS Model Based on LST‑R Theory

Using concepts of LST-R theory, the MTMS model can be defined based on the following assumptions: 

1. Equivalence of indicator- specific latent trait variables:* In LST-R theory, each measured variable is decomposed into a trait, a state residual, and a measurement error variable, such that $Y _ { i t } = \xi _ { i t } + \zeta _ { i t } + \varepsilon _ { i t }$ . In the MTMS model, it is assumed that all latent trait variables $\xi _ { i t }$ that share the same index i are equivalent, such that $\boldsymbol { \zeta } _ { i t } = \boldsymbol { \zeta } _ { i s } = \boldsymbol { \zeta } _ { i }$ for $i = 1$ , . . . , m and t, $s =$ 1, . . . , n. 

2. Occasion- specific congenericity of latent state residual variables: All latent state residual variables that are measured at the same time point are assumed to be positive linear functions of each other, such that $\zeta _ { i t } = \delta _ { i j t }$ ⋅ $\zeta _ { j t }$ for i, j = 1, . . . , m and $t = 1 , \ldots , n$ $t = 1$ . This assumption is equivalent to assuming a common latent state residual factor $\zeta _ { t }$ at each time point such that $\zeta _ { i t } = \delta _ { i t } \cdot \zeta _ { t } .$ In practice, the factor loadings $\delta _ { i t }$ are often assumed to be time- invariant, in which case the index t can be dropped from these parameters (i.e., $\delta _ { \mathrm { { i } } }$ instead of $\delta _ { i t } )$ . 

3. Linear independence of latent and error variables: It is assumed that $C o v ( \xi _ { \mathrm { i } } ,$ $\zeta _ { t } ) = C o \nu ( \xi _ { i } , \varepsilon _ { j t } ) = C o \nu ( \zeta _ { t } , \varepsilon _ { i s } ) = 0$ and $C o v ( \varepsilon _ { i t } , \varepsilon _ { j s } ) = 0$ for $( i , t ) \neq ( j , s )$ . In addition, by definition of LST-R theory, $C o v ( \zeta _ { t } , \zeta _ { s } ) = 0$ for $t \neq s$ . 

The assumption of occasion- specific congenericity implies the homogeneity of indicator specific state residuals at a given time point. The assumption of equivalence of latent trait variables means that trait components remain stable across time and affect all states in the same way. The assumption of uncorrelated variables helps model identification and simplifies the variance decomposition. Some of the restrictions in Assumption 3 can be relaxed to obtain more complex LST models with autoregressive effects (see Box 5.8). 

*Assumption 2 can be replaced by weaker assumptions about the homogeneity of traits such as essential equivalence or congenericity of traits. As in the STMS and other LST models, these weaker assumptions lead to versions of the MTMS model in which trait scores can change over time (for more details, see Geiser et al., 2015). 

Note that only $m - 1$ time-invariant state residual factor loadings $\delta _ { i }$ need to be estimated because one loading has to be fixed for each state residual factor $\zeta _ { t }$ to identify the scale of this factor. This is illustrated in Figure 5.5, in which the loading of the first measured variable $( \mathrm { i } = \mathrm { l } )$ ) is fixed to 1.0 $( \delta _ { 1 } = 1 )$ at each time point. Without any further invariance restrictions, the MTMS model has $0 . 5 m ^ { 2 }$ $+ 1 . 5 m + m - 1 + n + n m$ free model parameters. For our 4 time points $\times 3$ measures design, we obtain $4 . 5 + 4 . 5 + 2 + 4 + 1 2 = 2 7$ free parameters. We have 90 pieces of information, and so the MTMS model here has 63 df. In Box 5.7, I show how the MTMS model can be defined based on LST-R theory. 

# 5.4.4.3 Variance Decomposition and Coefficients

In the MTMS model, the same coefficients for quantifying the trait- versus statelike nature of a construct, as well as the precision of measurement, can be examined as in the STMS model without method factors (Section 5.4.2). The variance decompositions are given by 

$$
\begin{array}{l} V a r \left(\tau_ {i t}\right) = V a r \left(\xi_ {i}\right) + \delta_ {i} ^ {2} \cdot V a r \left(\zeta_ {t}\right) \\ V a r (Y _ {i t}) = V a r (\tau_ {i t}) + V a r (\varepsilon_ {i t}) \\ = V a r (\xi_ {t}) + \delta_ {i} ^ {2} \cdot V a r (\zeta_ {t}) + V a r (\varepsilon_ {i t}) \\ \end{array}
$$

The consistency (Con), occasion-specificity $( O s p )$ , and reliability (Rel) coefficients have the same meaning and are calculated in a similar way as in the STMS model without method factors (see Section 5.4.2). The only differences are that (1) the trait variance components $V a r ( \xi _ { i } )$ are now indicator-specific, (2) no trait factor loadings $\lambda _ { { _ i t } }$ are included, and (3) state residual factor loadings are estimated and now denoted with $\delta _ { i }$ . Therefore, the computational formulas differ slightly: 

$$
C o n \left(\tau_ {i t}\right) = V a r \left(\xi_ {i}\right) / \left[ V a r \left(\xi_ {i}\right) + \delta_ {i} ^ {2} \cdot V a r \left(\zeta_ {t}\right) \right]
$$

$$
\begin{array}{l} O s p (\boldsymbol {\tau} _ {i t}) = \delta_ {i} ^ {2} \cdot V a r (\boldsymbol {\zeta} _ {t}) / [ V a r (\boldsymbol {\xi} _ {i}) + \delta_ {i} ^ {2} \cdot V a r (\boldsymbol {\zeta} _ {t}) ] \\ C o n \left(Y _ {i t}\right) = V a r \left(\xi_ {i}\right) / \left[ V a r \left(\xi_ {i}\right) + \delta_ {i} ^ {2} \cdot V a r \left(\zeta_ {t}\right) + V a r \left(\varepsilon_ {i t}\right) \right] \\ O s p (Y _ {i t}) = \delta_ {i} ^ {2} \cdot \operatorname {V a r} (\zeta_ {t} ^ {\prime}) / \left[ \operatorname {V a r} (\xi_ {i}) + \delta_ {i} ^ {2} \cdot \operatorname {V a r} (\zeta_ {t} ^ {\prime}) + \operatorname {V a r} (\varepsilon_ {i t}) \right] \\ R e l (Y _ {i t}) = [ V a r (\xi_ {i}) + \delta_ {i} ^ {2} \cdot V a r (\zeta_ {t}) ] / [ V a r (\xi_ {i}) + \delta_ {i} ^ {2} \cdot V a r (\zeta_ {t}) + V a r (\varepsilon_ {i t}) ] \\ = 1 - \left[ V a r (\varepsilon_ {i t}) / V a r (Y _ {i t}) \right] \\ = C o n \left(Y _ {i t}\right) + O s p \left(Y _ {i t}\right) \\ \end{array}
$$

The interpretation of the coefficients is the same as in the STMS and other LST models. Mplus by default only computes the reliability coefficients $R e l ( Y _ { i t } )$ . 

As usual, the $R e l ( Y _ { i t } )$ coefficients can be found under R-SQUARE Observed Variable when the standardized solution (STDYX) is requested. The computation of the remaining coefficients can again be automated in Mplus by using the MODEL CONSTRAINT option as I demonstrate in the following Mplus application. 

# 5.4.4.4 Mplus Application

For the Mplus illustration, I applied the MTMS model to the same data set that I used to illustrate the LS-IS and STMS-IS models, thus allowing for a direct comparison of the models. Following is the Mplus MODEL statement for the MTMS model: 

```txt
MODEL:  
KSI1 by Y11 Y12@1 Y13@1 Y14@1;  
KSI2 by Y21 Y22@1 Y23@1 Y24@1;  
KSI3 by Y31 Y32@1 Y33@1 Y34@1;  
ZETA1 by Y11  
Y21*0.437 (d2)  
Y31*0.037 (d3);  
ZETA2 by Y12  
Y22*0.437 (d2)  
Y32*0.037 (d3);  
ZETA3 by Y13  
Y23*0.437 (d2)  
Y33*0.037 (d3);  
ZETA4 by Y14  
Y24*0.437 (d2)  
Y34*0.037 (d3);  
[Y11-Y34@0];  
Y11-Y14 (e1);  
Y21-Y24 (e2);  
Y31-Y34 (e3);  
[KSI1-KSI3*];  
KSI1 (KSIVAR1);  
KSI2 (KSIVAR2);  
KSI3 (KSIVAR3);  
ZETA1-ZETA4*20 (ZETAVAR);  
KSI1-KSI3 with ZETA1-ZETA4@0;  
ZETA1-ZETA4 with ZETA1-ZETA4@0;  
MODEL CONSTRAINT:  
NEW(CONTAU1 CONTAU2 CONTAU3 OSPTAU1 OSPTAU2 OSPTAU3 CONY1 CONY2 CONY3 OSPY1 OSPY2 OSPY3 RELY1 RELY2 RELY3);  
CONTAU1 = KSIVAR1 / (KSIVAR1 + ZETAVAR); 
```

```matlab
CONTAU2 = KSIVAR2 / (KSIVAR2 + d2**2*ZETAVAR);  
CONTAU3 = KSIVAR3 / (KSIVAR3 + d3**2*ZETAVAR);  
OSPTAU1 = ZETAVAR / (KSIVAR1 + ZETAVAR);  
OSPTAU2 = d2**2*ZETAVAR / (KSIVAR2 + d2**2*ZETAVAR);  
OSPTAU3 = d3**2*ZETAVAR / (KSIVAR3 + d3**2*ZETAVAR);  
CONY1 = KSIVAR1 / (KSIVAR1 + ZETAVAR + e1);  
CONY2 = KSIVAR2 / (KSIVAR2 + d2**2*ZETAVAR + e2);  
CONY3 = KSIVAR3 / (KSIVAR3 + d3**2*ZETAVAR + e3);  
OSPY1 = ZETAVAR / (KSIVAR1 + ZETAVAR + e1);  
OSPY2 = d2**2*ZETAVAR / (KSIVAR2 + d2**2*ZETAVAR + e2);  
OSPY3 = d3**2*ZETAVAR / (KSIVAR3 + d3**2*ZETAVAR + e3);  
RELY1 = CONY1 + OSPY1;  
RELY2 = CONY2 + OSPY2;  
RELY3 = CONY3 + OSPY3; 
```

The first three lines of code assign the measured variables to their indicatorspecific trait factors, with all loadings fixed to 1.0. Next, the four state residual factors are defined with time-invariant loadings. Notice that I provided starting values for the estimated loadings to help with model convergence. This was necessary in this case because of the very different metrics of the observed variables. (I obtained the starting values from an analysis of the same model without the restriction of equal state residual factor variances across time, which showed no convergence problems.) 

Subsequently, I set all intercepts to zero (the model implies that there are no additive constants in the measurement equation) and constrained the measurement error variances to be time-invariant. Moreover, I requested the estimation of the three trait factor means, labeled the trait factor variances as KSIVAR1 through KSIVAR3 for use of these parameters in MODEL CONSTRAINT, set the state residual factor variances equal across time (and provided a starting value of 20 for that variance parameter), and fixed the covariances between trait factors and state residuals as well as between all state residual factors to zero. 

In the MODEL CONSTRAINT statement, I defined the Con, Osp, and Rel coefficients as new parameters. Notice that all coefficients are time-invariant in this case (and hence, I dropped the index t in the Mplus input) because of the invariance constraints on the latent state residual and measurement error variances. This significantly reduces the number of coefficients that need to be computed. 

Like the STMS-IS model, the MTMS model with strict ME and equal latent state residual factor variances also fits the LS-IS data very well, $\chi ^ { 2 } ( 7 5 , N = 3 0 0 )$ $= 6 7 . 9 5 3$ , $p = . 7 1$ , $R M S E A = 0 . 0 0$ , $C F I = 1 . 0 0$ , $S R M R = 0 . 0 3 5$ . Notice that the MTMS model has two df less than the STMS-IS model in the present application because the MTMS model estimates three trait factors (with 3 means, 3 

variances, and 3 covariances) in lieu of one trait factor (with 1 mean and 1 variance), two indicator-specific factors $I S _ { i }$ (with 2 variances and 1 covariance), and two intercepts ${ \bf q } _ { \mathrm { i } }$ . Hence, the STMS-IS approach is slightly more parsimonious than the MTMS approach. In practice, both approaches often fit similarly well. Below are Mplus output excerpts for the MTMS model. 

<table><tr><td colspan="6">MODEL RESULTS</td></tr><tr><td></td><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-TailedP-Value</td></tr><tr><td colspan="6">Means</td></tr><tr><td>KSI1</td><td></td><td>99.871</td><td>0.801</td><td>124.756</td><td>0.000</td></tr><tr><td>KSI2</td><td></td><td>45.947</td><td>0.520</td><td>88.339</td><td>0.000</td></tr><tr><td>KSI3</td><td></td><td>0.008</td><td>0.053</td><td>0.142</td><td>0.887</td></tr><tr><td colspan="6">Variances</td></tr><tr><td>KSI1</td><td></td><td>181.582</td><td>15.706</td><td>11.562</td><td>0.000</td></tr><tr><td>KSI2</td><td></td><td>74.771</td><td>6.633</td><td>11.272</td><td>0.000</td></tr><tr><td>KSI3</td><td></td><td>0.793</td><td>0.070</td><td>11.312</td><td>0.000</td></tr><tr><td>ZETA1</td><td></td><td>25.086</td><td>6.053</td><td>4.144</td><td>0.000</td></tr><tr><td>ZETA2</td><td></td><td>25.086</td><td>6.053</td><td>4.144</td><td>0.000</td></tr><tr><td>ZETA3</td><td></td><td>25.086</td><td>6.053</td><td>4.144</td><td>0.000</td></tr><tr><td>ZETA4</td><td></td><td>25.086</td><td>6.053</td><td>4.144</td><td>0.000</td></tr><tr><td colspan="6">STANDARDIZED MODEL RESULTS (STDYX Standardization)</td></tr><tr><td></td><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-TailedP-Value</td></tr><tr><td>KSI1BY</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y11</td><td></td><td>0.900</td><td>0.009</td><td>105.256</td><td>0.000</td></tr><tr><td>Y12</td><td></td><td>0.900</td><td>0.009</td><td>105.256</td><td>0.000</td></tr><tr><td>Y13</td><td></td><td>0.900</td><td>0.009</td><td>105.256</td><td>0.000</td></tr><tr><td>Y14</td><td></td><td>0.900</td><td>0.009</td><td>105.256</td><td>0.000</td></tr><tr><td>KSI2BY</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y21</td><td></td><td>0.863</td><td>0.011</td><td>76.757</td><td>0.000</td></tr><tr><td>Y22</td><td></td><td>0.863</td><td>0.011</td><td>76.757</td><td>0.000</td></tr><tr><td>Y23</td><td></td><td>0.863</td><td>0.011</td><td>76.757</td><td>0.000</td></tr><tr><td>Y24</td><td></td><td>0.863</td><td>0.011</td><td>76.757</td><td>0.000</td></tr><tr><td>KSI3BY</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y31</td><td></td><td>0.868</td><td>0.011</td><td>79.651</td><td>0.000</td></tr><tr><td>Y32</td><td></td><td>0.868</td><td>0.011</td><td>79.651</td><td>0.000</td></tr><tr><td>Y33</td><td></td><td>0.868</td><td>0.011</td><td>79.651</td><td>0.000</td></tr><tr><td>Y34</td><td></td><td>0.868</td><td>0.011</td><td>79.651</td><td>0.000</td></tr><tr><td>ZETA1BY</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y11</td><td></td><td>0.334</td><td>0.042</td><td>8.015</td><td>0.000</td></tr><tr><td>Y21</td><td></td><td>0.202</td><td>0.029</td><td>7.010</td><td>0.000</td></tr><tr><td>Y31</td><td></td><td>0.172</td><td>0.026</td><td>6.639</td><td>0.000</td></tr><tr><td>ZETA2BY</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y12</td><td></td><td>0.334</td><td>0.042</td><td>8.015</td><td>0.000</td></tr><tr><td>Y22</td><td></td><td>0.202</td><td>0.029</td><td>7.010</td><td>0.000</td></tr><tr><td>Y32</td><td></td><td>0.172</td><td>0.026</td><td>6.639</td><td>0.000</td></tr><tr><td colspan="6">ZETA3 BY</td></tr><tr><td>Y13</td><td></td><td>0.334</td><td>0.042</td><td>8.015</td><td>0.000</td></tr><tr><td>Y23</td><td></td><td>0.202</td><td>0.029</td><td>7.010</td><td>0.000</td></tr><tr><td>Y33</td><td></td><td>0.172</td><td>0.026</td><td>6.639</td><td>0.000</td></tr><tr><td colspan="6">ZETA4 BY</td></tr><tr><td>Y14</td><td></td><td>0.334</td><td>0.042</td><td>8.015</td><td>0.000</td></tr><tr><td>Y24</td><td></td><td>0.202</td><td>0.029</td><td>7.010</td><td>0.000</td></tr><tr><td>Y34</td><td></td><td>0.172</td><td>0.026</td><td>6.639</td><td>0.000</td></tr><tr><td colspan="6">KSI2 WITH</td></tr><tr><td>KSI1 WITH</td><td></td><td>0.919</td><td>0.012</td><td>73.575</td><td>0.000</td></tr><tr><td colspan="6">KSI3 WITH</td></tr><tr><td>KSI1</td><td></td><td>0.788</td><td>0.025</td><td>31.211</td><td>0.000</td></tr><tr><td>KSI2</td><td></td><td>0.806</td><td>0.025</td><td>32.285</td><td>0.000</td></tr><tr><td colspan="6">R-SQUARE</td></tr><tr><td colspan="5">Observed</td><td>Two-Tailed</td></tr><tr><td>Variable</td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td colspan="2">P-Value</td></tr><tr><td>Y11</td><td>0.922</td><td>0.027</td><td>34.725</td><td colspan="2">0.000</td></tr><tr><td>Y12</td><td>0.922</td><td>0.027</td><td>34.725</td><td colspan="2">0.000</td></tr><tr><td>Y13</td><td>0.922</td><td>0.027</td><td>34.725</td><td colspan="2">0.000</td></tr><tr><td>Y14</td><td>0.922</td><td>0.027</td><td>34.725</td><td colspan="2">0.000</td></tr><tr><td>Y21</td><td>0.786</td><td>0.019</td><td>41.430</td><td colspan="2">0.000</td></tr><tr><td>Y22</td><td>0.786</td><td>0.019</td><td>41.430</td><td colspan="2">0.000</td></tr><tr><td>Y23</td><td>0.786</td><td>0.019</td><td>41.430</td><td colspan="2">0.000</td></tr><tr><td>Y24</td><td>0.786</td><td>0.019</td><td>41.430</td><td colspan="2">0.000</td></tr><tr><td>Y31</td><td>0.783</td><td>0.018</td><td>43.237</td><td colspan="2">0.000</td></tr><tr><td>Y32</td><td>0.783</td><td>0.018</td><td>43.237</td><td colspan="2">0.000</td></tr><tr><td>Y33</td><td>0.783</td><td>0.018</td><td>43.237</td><td colspan="2">0.000</td></tr><tr><td>Y34</td><td>0.783</td><td>0.018</td><td>43.237</td><td colspan="2">0.000</td></tr></table>

The means and variances of the three trait factors differ strongly, reflecting the differences in the metric of the cognitive ability tests used in this example. In the STMS and STMS-IS models, these differences in the scaling of the measured variables were reflected in the intercepts ${ \bf { d } } _ { \mathrm { { i } } }$ and factor loadings $\lambda _ { i }$ . The variance of the first trait factor (KSI1) was estimated to be 181.582, which is a much larger value than the value estimated for the (time-invariant) state residual variance (25.086). These two variances are directly comparable because the loadings of the same indicator $( Y _ { 1 t } )$ were fixed to 1.0 on both factors. The large difference in the variances indicates that the construct is strongly trait-like. Notice that the remaining trait variances cannot be directly compared to the state residual variance because they are in different metrics. The standardized solution as well as the Con and Osp coefficients help us with this issue. 

In the standardized solution, we can see that all measures have stronger trait (KSI) than state residual (ZETA) loadings. This shows that all measures reflect a more trait- than state-like construct. The correlations between indicator- specific trait factors are strong (all $\Phi s \ge . 8 0 6 )$ , indicating that the measures reflect closely related latent trait components. The reliability estimates are time- invariant for each indicator (again, this is because of the equality constraints on the latent state residual and measurement error variances) and indicate decent reliabilities of the scores for all measures $[ R e l ( Y _ { i } ) \ge . 7 8 3 ]$ . 

The (time- invariant) Con and $O s p$ coefficients were computed manually through MODEL CONSTRAINT and thus appear under New/Additional Parameters: 

<table><tr><td colspan="5">New/Additional Parameters</td></tr><tr><td>CONTAU1</td><td>0.879</td><td>0.027</td><td>32.053</td><td>0.000</td></tr><tr><td>CONTAU2</td><td>0.948</td><td>0.014</td><td>65.560</td><td>0.000</td></tr><tr><td>CONTAU3</td><td>0.962</td><td>0.011</td><td>85.650</td><td>0.000</td></tr><tr><td>OSPTAU1</td><td>0.121</td><td>0.027</td><td>4.428</td><td>0.000</td></tr><tr><td>OSPTAU2</td><td>0.052</td><td>0.014</td><td>3.574</td><td>0.000</td></tr><tr><td>OSPTAU3</td><td>0.038</td><td>0.011</td><td>3.349</td><td>0.001</td></tr><tr><td>CONY1</td><td>0.810</td><td>0.015</td><td>52.628</td><td>0.000</td></tr><tr><td>CONY2</td><td>0.745</td><td>0.019</td><td>38.379</td><td>0.000</td></tr><tr><td>CONY3</td><td>0.754</td><td>0.019</td><td>39.825</td><td>0.000</td></tr><tr><td>OSPY1</td><td>0.112</td><td>0.028</td><td>4.008</td><td>0.000</td></tr><tr><td>OSPY2</td><td>0.041</td><td>0.012</td><td>3.505</td><td>0.000</td></tr><tr><td>OSPY3</td><td>0.029</td><td>0.009</td><td>3.319</td><td>0.001</td></tr><tr><td>RELY1</td><td>0.922</td><td>0.027</td><td>34.729</td><td>0.000</td></tr><tr><td>RELY2</td><td>0.786</td><td>0.019</td><td>41.431</td><td>0.000</td></tr><tr><td>RELY3</td><td>0.783</td><td>0.018</td><td>43.238</td><td>0.000</td></tr></table>

The coefficients again show that the construct under study is mostly traitlike with all three $C o n ( \tau _ { i } )$ coefficients ≥ .879. The estimates are close to the corresponding estimates obtained from the STMS-IS model, which makes sense 

# BOX 5.8. The MTMS Model with Autoregression

As I explained above, the STMS model can be extended to include autoregressive effects. The same is true for the MTMS model (see Figure 5.6). The definition of the MTMS model with autoregression based on LST-R theory as well as its variance decompositions and coefficients, are described in detail in Eid et al. (2017). A sample Mplus script for the estimation of the MTMS model with autoregression can be found in the online supplemental materials. 

given that both models fit the data very well. Notice that no distinction between common and unique consistency is possible in the MTMS model and that the $C o n ( \tau _ { i } )$ coefficients reflect the total consistency in each measure. 

# 5.4.4.5 Summary

In most LST analyses with multiple measures per time point, social science researchers have to deal with indicator-specific effects. Instead of including indicator-specific residual factors as in the STMS-IS approach, the MTMS model addresses this issue by allowing each measure to have its own trait factor with a separate mean and variance. Correlations between the indicator-specific trait factors can be estimated and indicate the degree of homogeneity (convergent validity) of the measures. Highly correlated traits indicate that measures are essentially measuring the same trait components. For perfectly correlated traits, the model reduces to the STMS model without method factors. When autoregressive effects are likely (e.g., due to small intervals between time points), the model can be specified with autoregressive paths among state/occasion residuals (see Box 5.8). 

The MTMS model offers greater flexibility than other LST models and often fits well in empirical applications. One advantage of the MTMS model is that it does not require the specification of a single common trait or selection of a reference variable to define a trait. The model can even be used for rather heterogeneous (“multifaceted”) constructs as long as the assumption of shared occasionspecific influences (common state residual factors) across facets is reasonable. An advantage of the MTMS model over the STMS-IS model is that the MTMS model does not require choosing a reference variable or including method (IS) factors. Therefore, the model, in some sense, is simpler and easier to specify. It also allows examining traits for each measure, whereas the STMS-IS model includes a trait factor only for the reference measure. 

Another advantage of the MTMS approach over the STMS-IS model is that the MTMS model shares the basic STMS model’s simplicity with regard to the variance decomposition. No extra $I S _ { i }$ (method) factors need to be specified and no additional variance components (due to indicator-specific/method effects) need to be computed in the MTMS model. One the other hand, this means that if a researcher is specifically interested in quantifying the variance components in each indicator that are due to unique trait effects (unique consistency) versus shared trait effects (common consistency), then the STMS-IS model may be a better choice. In cases in which all correlations between $\xi _ { i }$ factors are equal to 1.0, the MTMS model reduces to an STMS model without method factors. 

For very homogeneous measures, the MTMS model will sometimes return latent trait correlation estimates greater than 1.0 (“improper solutions”). In this case, Mplus will issue the following warning message but still provides the parameter estimates: 

```txt
WARNING: THE LATENT VARIABLE COVARIANCE MATRIX (PSI) IS NOT POSITIVE DEFINITE. THIS COULD INDICATE A NEGATIVE VARIANCE/RESIDUAL VARIANCE FOR A LATENT VARIABLE, A CORRELATION GREATER OR EQUAL TO ONE BETWEEN TWO LATENT VARIABLES, OR A LINEAR DEPENDENCY AMONG MORE THAN TWO LATENT VARIABLES. CHECK THE TECH4 OUTPUT FOR MORE INFORMATION. PROBLEM INVOLVING VARIABLE [variable name]. 
```

As long as the out-of-bounds correlation estimates are within sampling error of 1.0, this result is usually not problematic. It usually simply indicates an overparameterization of the model (too many trait factors). In this case, researchers can collapse some or all indicator-specific trait factors into one or more common traits. 

# 5.5 LATENT TRAIT‑CHANGE MODELS

# 5.5.1 Introduction

The LST models discussed in Section 5.4 are primarily concerned with shortterm variability processes in, for example, hormone levels, mood states, or emotions. A variability process involves reversible changes (“fluctuations”) in state scores due to situation or person $\times$ situation interaction effects (e.g., fluctuations in mood states). The trait scores themselves may not be affected by state variability processes. As a consequence, they are assumed to be stable in classical LST models such as the STMS and MTMS models without autoregression discussed in Sections 5.4.2 through 5.4.4. In LST models with autoregression (for an example, see Figure 5.6), trait scores can change across time (Eid et al., 2017). In this section, I describe models that allow modeling trait changes in a more explicit way. 

Trait changes are conceptually different from short-term state fluctuations in that they involve potentially more long-lasting or permanent modifications to individuals’ trait scores rather than just short-term variability in the state scores that are reversible. Longer lasting changes in individuals’ trait scores are of interest to many social science researchers. For example, we would like to know the extent to which people’s attitudes, personality traits, or abilities 

change in a more permanent way over time and whether trait changes can be caused by certain events or interventions. For example, critical life events (e.g., birth of a child, death of one’s partner) may lead to permanent changes in trait life satisfaction and other personality variables. In addition, trait changes are key, for example, to psychological interventions that usually aim at long-lasting changes in cognitions (e.g., obsessive thoughts), behaviors (e.g., compulsions), or feelings (e.g., anxiety). 

Of the multiple-indicator models presented so far, the LS, LSC, and LAS/ LACS models allowed for trait changes but did not permit the separation of such trait changes from short-term fluctuations due to situational and/or person $\times$ situation interaction (state residual) influences. Classical LST models such as the STMS or MTMS models with time-invariant intercepts and loadings imply a pure state variability process. In this process, variability in the true state scores can only be due to state residual influences; trait scores are assumed to remain stable over time. LST models with autoregression permit trait changes, albeit in a somewhat indirect way. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/465cdd8ada32033dd0fd5fb6f905f4aa17b560df500a6e7617c562c436439c76.jpg)



FIGURE 5.6. Path diagram of a multitrait–multistate (MTMS) model with autoregression for three observed variable $Y _ { i t }$ that are measured on four time points. $\xi _ { \mathrm { i 1 } } = \mathrm { i n i - }$ tial (Time-1) indicator-specific latent trait factor; $\zeta _ { t } =$ latent state residual variable; $O _ { t } =$ occasion residual variable; $\varepsilon _ { i t } =$ measurement error variable; $\delta _ { \mathrm { i } } =$ constant state residual factor loading; $\gamma _ { 1 t } =$ constant autoregressive slope coefficient.


In this section, I discuss models that are explicitly designed to analyze both long-term changes in latent trait scores and short-term state fluctuations. In this sense, the models presented in this section can be seen as hybrid models that combine the advantages of classical LST models (which separate trait, state residual, and measurement error influences) and trait-change models (which permit the analysis of changes in trait values). I begin with trait-change models that are suitable when researchers want to compare two or more specific time periods, for example, the period before versus the period after an event or intervention. Subsequently, I discuss multiple-indicator growth curve models, which do not require the presence of specifically defined time periods. 

# 5.5.2 The LST Trait‑Change Model

# 5.5.2.1 Introduction

One approach to examining changes in latent trait scores explicitly while still allowing for a separation between trait-change and state variability processes is to specify a combined LST trait-change (LST-TC) model (Eid & Hoffmann, 1998). In this model, one or more latent trait factors are specified (1) before and (2) after an intervention or event. Then, changes in the latent trait scores can be examined in addition to state residual variability as reflected in the latent state residual variables. 

# 5.5.2.2 Model Description

Figure 5.7 shows different versions of the structural (latent variable) portion of an LST-TC model for a longitudinal design with four time points. (The measurement model is again omitted in the figure for the sake of simplicity; an STMS, STMS-IS, or MTMS measurement model could be used.) The first two time points (Period 1) occurred before an event or intervention. The last two time points (Period 2) occurred after the event/intervention. It can be seen that there is a separate common trait factor $\xi _ { p }$ for each period $p$ $p = 1$ , . . ., r; here: $r = 2 \AA$ ) as well as a separate state residual factor $\zeta _ { { \scriptscriptstyle t p } }$ at each measurement occasion. Furthermore, the model includes measurement error variables $\varepsilon _ { i t p }$ for each indicator. Hence, the model is a combination of two STMS models, one for Period 1 and one for Period 2. 

In the most basic LST-TC model shown in Figure 5.7A, the period-specific trait factors $\xi _ { 1 }$ and $\boldsymbol { \xi } _ { 2 }$ each have their own mean and variance estimated as free parameters. (The alternative, equivalent change score and autoregressive model versions shown in Figures 5.7B and C are described in Box 5.10.) In 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/41f7bff1f44032ebe069fd0fa05a5b013c07460aff71cea4ae624f2d14071e1e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/b59462b19edee1e63d52001110e52f05aacfd092e1284d81d4fec3d05ccaa83e.jpg)



B


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/71a60771b45763967aaa8ed73b0d539d3fac3fe93d0220a19fd02414c7d19a80.jpg)



FIGURE 5.7. Path diagrams of the structural models pertaining to LST trait-change (LST-TC) models for four time points and two time periods $p$ . $\tau _ { t p } =$ period-specific latent state factor; $\xi _ { p } = $ period-specific common latent trait factor; $( \xi _ { 2 } - \xi _ { 1 } ) =$ latent trait-change score variable; $\zeta _ { t p } =$ latent state residual variable; $v _ { 2 }$ , $\omega _ { 2 } =$ latent residual variables; $\beta _ { 0 t }$ , $\gamma _ { 0 t } =$ constant regression intercept coefficients; $\beta _ { \mathrm { 1 } t } ,$ $\gamma _ { 1 t } =$ constant regression slope coefficients. A: Basic LST-TC model with correlated latent trait factors; B: latent trait-change score model; C: autoregressive traits model.


addition, their covariance/correlation can be estimated. Assuming strong ME, a researcher can examine trait changes by comparing the means $E ( \xi _ { p } )$ and variances $V a r ( \xi _ { p } )$ between two or more time periods. Moreover, the trait correlation $\Phi _ { 1 2 }$ indicates the extent to which the linear rank order of individual trait scores remained consistent across time. 

The STMS model with a single-trait factor (Section 5.4.2) can be seen as a special case of the LST-TC model in which the two period-specific trait factors have identical means and variances and are perfectly (1.0) correlated. Hence, the STMS model can serve as a baseline “no trait-change” model to be compared to the LST-TC model. If the STMS model fits no worse than the LST-TC model, it can be concluded that no trait changes occurred between the two time periods and that a single general trait factor is thus sufficient. 

The measurement portion of the LST-TC model is analogous to the measurement structure in the STMS model (assuming strong ME): 

$$
\begin{array}{l} Y _ {i t p} = \pmb {\alpha} _ {i} + \lambda_ {i} \cdot \tau_ {t p} + \varepsilon_ {i t p} \\ = \alpha_ {i} + \lambda_ {i} \cdot (\xi_ {p} + \zeta_ {t p}) + \varepsilon_ {i t p} \\ = \alpha_ {i} + \lambda_ {i} \cdot \xi_ {p} + \lambda_ {i} \cdot \zeta_ {t p} + \varepsilon_ {i t p} \\ \end{array}
$$

As in the STMS model, each state variable $\tau _ { t p }$ may reflect both trait $( \zeta _ { p } )$ and state residual $( \zeta _ { t p } )$ components. Therefore, the LST-TC model not only allows researchers to study trait changes, but also state variability processes (e.g., by computing consistency and occasion-specificity coefficients as shown in Section 5.4.2). 

In summary, the LST-TC model with strong ME across time allows estimating the following parameters (recall that $r$ here refers to the toal number of periods $p$ considered in the study): 

• $r$ trait factor means $E ( \xi _ { p } )$ 

• $r$ trait factor variances $V a r ( \xi _ { p } )$ , 

• $0 . 5 ( r ^ { 2 } - r )$ trait factor covariances $C o v ( \xi _ { p } , \xi _ { q } )$ , p, $q = 1$ , . . . , r, 

•	 n state residual factor variances $V a r ( \zeta _ { t p } )$ 

• $m - 1$ constant time-invariant intercepts ${ \bf \mathfrak { a } } _ { t }$ (the intercept pertaining to the reference indicator is fixed to 0 on each measurement occasion), 

• $m - 1$ constant time-invariant factor loadings $\lambda _ { { } _ { t } }$ (the loading pertaining to the reference indicator is fixed to 1 on each measurement occasion), and 

•	 nm measurement error variances $V a r ( \varepsilon _ { i t p } )$ . 

Therefore, the LST-TC model with strong ME across time has $0 . 5 r ^ { 2 } + 1 . 5 r +$ $2 m + n + n m - 2$ free model parameters. For our example with three measures ${ \mathrm { ~ } } m = 3 ,$ , four time points $( n = 4 )$ , and two time periods $( r = 2 )$ ), we obtain $2 +$ $3 + 6 + 4 + 1 2 - 2 = 2 5$ free model parameters. With three measures and four time points, we have 90 pieces of known information, and so the model has 65 df. In Box 5.9, I explain how the LST-TC model can be defined based on LST-R theory. 

# BOX 5.9. Defining the LST‑TC Model Based on LST‑R Theory

Using concepts of LST-R theory, the LST-TC model can be defined based on the following assumptions: 

1. Occasion- specific congenericity of latent state variables: All latent state variables measured at the same time point are positive linear functions of each other, such that τitp = $\tau _ { i t p } = \mathbf { a } _ { i j t p } + \lambda _ { i j t p } \cdot \tau _ { j t p }$ + λijtp for all $i , j = 1$ , . . . , m; $t = 1$ . . . , n; and $p = 1$ , . . . , $r .$ This assumption is equivalent to assuming a common latent state factor $\tau _ { t p }$ at each time point, such that: $\pmb { \tau } _ { i t p } = \mathbf { q } _ { i t p } +$ $\lambda _ { { \mathrm { i } } t p } \cdot \tau _ { t p }$ . 

2. Equivalence of period- specific latent trait variables: According to LST-R theory, each latent state variable is decomposed into a trait and a state residual component, such that $\tau _ { t p } = \xi _ { t p } + \zeta _ { t p }$ . In the LST-TC model, it is assumed that all trait components $\xi _ { { t p } }$ that share the same time period $p$ are identical: $\xi _ { t p } = \xi _ { s p } = \xi _ { p }$ for all t, $s = 1 , \ldots , n$ and $p = 1 , \ldots , r .$ $p = 1 ,$ 

3. Linear independence of latent and measurement error variables: It is assumed that $C o \nu ( \xi _ { p } , \zeta _ { t p } ) = C o \nu ( \xi _ { p } , \varepsilon _ { i t p } ) = 0$ , $C o \nu ( \zeta _ { t p } , \zeta _ { s q } ) = 0$ for $( t , p ) \neq ( s ,$ q), $C o \nu ( \zeta _ { t p } , \varepsilon _ { i s q } ) = C \overset { \cdot } { o } \nu ( \varepsilon _ { i t p } ^ { \cdot } , \varepsilon _ { j s q } ) = \overset { \cdot } { 0 }$ for $p$ , $q = 1$ , . . . , r, and $( i , t , p ) \neq ( j , s ,$ , $q )$ . 

The assumption of occasion- specific congenericity again implies unidimensionality of the measured variables $Y _ { i t p }$ at a given time point. The assumption of equivalence of latent trait variables means that trait components remain stable within each time period.* The assumption of uncorrelated variables helps model identification and simplifies the variance decomposition. 

# 5.5.2.3 Variance Decomposition and Coefficients

The variance decomposition and coefficients in the LST-TC model are analogous to the variance decomposition and coefficients in the STMS model, except for the time period $p$ that has to be taken into account in the LST-TC approach (i.e., variables pertaining to different time periods load onto different trait factors). Because of the similarity of the computations, I do not present separate formulas here but refer the reader to Section 5.4.2.3. Notice that another interesting feature of the LST-TC model is that changes in the amount of trait versus occasion-specific variance over time may also be examined in the model (Geiser, Griffin, & Shiffman, 2016). Such changes in consistency may be another relevant result of the event or intervention that took place between two time periods (e.g., individuals showing not just higher average trait mood, but also fewer “ups and downs” [higher consistency] in their mood states as a result of psychotherapy). 

# 5.5.2.4 Mplus Application

Imagine a researcher developed a training procedure for improving cognitive abilities. She wants to find out whether the new training leads to increases in average cognitive abilities at the trait level, that is, true trait changes rather than mere variations due to situational influences (state fluctuations). Assume she ran a single-group experiment in which $N = 3 0 0$ individuals’ cognitive abilities were tested with three cognitive ability tests twice before (Period 1) and twice after the training (Period 2). The researcher then applied the LST-TC model to examine changes at the trait level between the two time periods. 

Below are selected Mplus MODEL commands for the hypothetical scenario described above. Note that the first-order measurement model for the latent state factors $\tau _ { t }$ is the exact same as in the LS and STMS models with strong ME (time-invariant loadings and intercepts) and is therefore not repeated here (however, the complete example input file for the LST-TC can be found on the companion website [see the box at the end of the table of contents]). 

```c
MODEL:  
KSI1 by TAU1-TAU2@1;  
[KSI1] (E1);  
KSI2 by TAU3-TAU4@1;  
[KSI2] (E2);  
model constraint:  
new(E_C);  
E_C = E2 - E1; 
```

# BOX 5.10. Alternative Equivalent Ways to Specify the LST-TC Model

The LST-TC model can be formulated in different ways. I present a basic LST-TC model version with correlated trait factors in detail in the main text. In this box, I discuss two alternative, equivalent versions of the LST-TC model: a traitchange score and a trait autoregressive model. The trait-change score model version (see Figure 5.7B) has the advantage that it expresses trait changes directly in terms of a latent (change score) variable. The trait autoregressive model (see Figure 5.7C) is conceptually similar to the LAS model and can be expanded to a multiconstruct cross- lagged model. 

In the trait-change score model, the same principle as in LSC score models is applied to the trait factors. That is, the trait factor for Period 2 is decomposed into the Period-1 trait factor plus a trait- change score variable $( \xi _ { 2 } - \xi _ { 1 } )$ : 

$$
\xi_ {2} = \xi_ {1} + (\xi_ {2} - \xi_ {1})
$$

The trait- change score variable directly reflects interindividual differences in intraindividual trait changes. Again assuming that strong ME holds, the mean $E ( \xi _ { 2 } - \xi _ { 1 } )$ indicates trait mean changes across time. The variance $V a r ( \xi _ { 2 } - \xi _ { 1 } )$ provides information on interindividual differences in trait change across time. (To which extent did people differ in how much their trait values changed?) In analogy to LS change score models, the trait- change score variable $( \xi _ { 2 } - \xi _ { 1 } )$ can be regressed on the Period-1 trait factor, as shown in Figure 5.7B: 

$$
\left(\xi_ {2} - \xi_ {1}\right) = \gamma_ {0 2} + \gamma_ {1 2} \cdot \xi_ {1} + \varsigma_ {2}
$$

where $\varsigma _ { 2 }$ indicates a latent residual trait-change score variable. 

Through this regression, a potential relationship between initial trait scores and trait change can be examined and potentially statistically controlled for. For example, it may be of interest to examine whether patients with initially higher trait anxiety benefited more or less from a psychological intervention than patients with initially less severe trait anxiety. In quasi- experimental studies, it may be crucial to statistically control for preexisting interindividual differences in a construct when examining potential external predictors of interindividual differences in trait changes. 

Another equivalent way to reparametrize the basic LST-TC model shown in Figure 5.7A is to specify an autoregressive relationship between the two periodspecific trait factors (Steyer et al., 2015). This version of the model is shown in Figure 5.7C. Formally, the autoregressive parameterization is given by the following structural equation: 

$$
\xi_ {2} = \beta_ {0 2} + \beta_ {1 2} \cdot \xi_ {1} + \omega_ {2}
$$

where $\omega _ { 2 }$ indicates a trait residual variable. The autoregressive parameterization could be expanded to a cross- lagged model by adding one or more additional constructs to the model. 

We can see that, in contrast to the STMS model specification, we now use two trait factors, one for Period 1 (measured by TAU1 and TAU2) and one for Period 2 (measured by TAU3 and TAU4). The means of both trait factors are estimated by specifying the trait factor labels in brackets (e.g., [KSI1]), and each is given a label so that they can be used in MODEL CONSTRAINT. The other relevant parameters (the trait factor variances and their covariance) are estimated by default in Mplus. The MODEL CONSTRAINT option is used here to compute the trait mean difference E2 – E1 as a separate (“new”) parameter. This has the advantage that the mean difference can then be tested for statistical significance (Recall that the MODEL CONSTRAINT option provides a standard error and test of significance for each new parameter.) Below are Mplus output excerpts for the LST-TC model $\mathrm { \Delta N } = 3 0 0$ , simulated data): 

<table><tr><td colspan="5">MODEL RESULTS</td></tr><tr><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-TailedP-Value</td></tr><tr><td>Means</td><td></td><td></td><td></td><td></td></tr><tr><td>KSI1</td><td>99.813</td><td>0.825</td><td>120.950</td><td>0.000</td></tr><tr><td>KSI2</td><td>101.506</td><td>0.805</td><td>126.168</td><td>0.000</td></tr><tr><td>New/Additional Parameters</td><td></td><td></td><td></td><td></td></tr><tr><td>E_C</td><td>1.694</td><td>0.475</td><td>3.565</td><td>0.000</td></tr><tr><td colspan="5">STANDARDIZED MODEL RESULTS (STDYX Standardization)</td></tr><tr><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-TailedP-Value</td></tr><tr><td>KSI1 BY</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU1</td><td>0.943</td><td>0.012</td><td>80.858</td><td>0.000</td></tr><tr><td>TAU2</td><td>0.958</td><td>0.012</td><td>83.200</td><td>0.000</td></tr><tr><td>KSI2 BY</td><td></td><td></td><td></td><td></td></tr><tr><td>TAU3</td><td>0.967</td><td>0.011</td><td>87.880</td><td>0.000</td></tr><tr><td>TAU4</td><td>0.961</td><td>0.011</td><td>87.024</td><td>0.000</td></tr><tr><td>KSI1 WITH</td><td></td><td></td><td></td><td></td></tr><tr><td>KSI2</td><td>0.895</td><td>0.017</td><td>52.011</td><td>0.000</td></tr></table>

The results indicate that the Period-2 trait factor mean (101.506) was estimated to be slightly larger than the Period-1 trait factor mean (99.813), pointing to an increase in trait-level cognitive abilities from Period 1 to Period 2. The newly defined mean difference parameter E_C was estimated to be 1.694 (SE $= 0 . 4 7 5$ ) and was statistically significant $z = 3 . 5 6 5$ , $p < . 0 0 1$ ), indicating an increase in average trait scores.1 

The standardized model results show that the construct under study was mostly trait-like, as indicated by the strong standardized loadings (≥ .943) of 

the first-order state factors on the second-order trait factors. In other words, not much occasion-specific variance was present in the state scores. Furthermore, the correlation between the two period-specific trait factors was strong $( \phi =$ .895), indicating that the linear rank order of individuals’ trait scores remained highly consistent across the two time periods. 

# 5.5.2.5 Summary

The examination of potentially more long-lasting trait changes and the separation of such trait changes from short-term state variability processes and random fluctuations due to measurement error are of interest to many longitudinal researchers. The key idea of the LST-TC approach is to include separate trait factors for each of two or more distinct time periods. The period-specific trait factor means, variances, and covariances can then be examined, and potential changes in trait scores can be separated from short-term state fluctuations. Therefore, the approach allows disentangling more long-term trait changes from short-term situation-specific fluctuations and random measurement error. It can also be used to examine changes in consistency and occasion specificity of behavior as a result of an event or intervention (see Geiser et al., 2016, for an example). 

The time periods can be defined either by naturally occurring events (e.g., critical personal life events, natural disasters, political events) or planned interventions (e.g., training procedures, psychotherapy). The LST-TC approach requires at least two time points (measurement occasions) within at least two time periods to identify separate trait factors for each period. 

For ease of presentation, I focused on the STMS measurement approach to LST-TC modeling, which uses only a single, general trait factor for each period. The STMS approach assumes that indicators are homogeneous, which is often unrealistic in practice. Instead of an STMS measurement model, an STMS-IS or MTMS measurement model can be used in the LST-TC approach as well. In case an MTMS measurement model is used, a researcher can study trait changes separately for each indicator’s specific trait component. This may be particularly useful, as events or interventions may impact different facets of a construct differently. 

One general limitation of the LST-TC approach to modeling trait changes across time is that it requires a measurement design with at least one clearly defined event or intervention to obtain two or more discrete time periods to be compared. Therefore, the approach is less useful when a researcher simply wants to look at natural development across time (i.e., in studies in which there is no particular event or treatment). Another limitation is that the model requires at least four measurement occasions (two pre- and two post-event/interventions). 

Although having many measurement occasions is generally desirable in longitudinal research, many longitudinal studies are limited to fewer than four time points for a variety of reasons. The last model class that I discuss in this chapter addresses these limitations. 

# 5.5.3 Multiple‑Indicator Latent Growth Curve Models

# 5.5.3.1 Introduction

In Chapter 3, I described single-indicator latent growth curve (LGC) models as latent trait-change models. Recall that one limitation of single-indicator LGC models is that these models ignore the state residual (situational and/or person $\times$ situation interaction) component that is present in many social science constructs. Single-indicator LGC models confound reliable state residual (situational) variability with random measurement error, leading to an underestimation of indicator reliabilities when situational variability is present. In summary, single-indicator LGC models do not allow separating trait (and/or trait-change) components from state residual (situational and/or person $\times$ situation interaction) components. Moreover, single-indicator LGC models do not allow testing for ME across time (except for the equality of the measurement error variances, which can be tested). 

Multiple-indicator LGC (MI-LGC) models address these issues by using more than one measured variable at each time point. In contrast to the LST-TC models that I described in Section 5.5.2, MI-LGC models do not require a specific event or intervention to take place during the study and they can be specified with as few as three measurement occasions. A well-known MI-LGC model is the second-order LGC model (McArdle, 1988; Sayer & Cumsille, 2001; see Figure 5.8). Subsequently, more general MI-LGC models have been presented (Eid, Courvoisier, & Lischetzke, 2012; Tisak & Tisak, 2000). Bishop, Geiser, and Cole (2015) showed how the second-order LGC model and other MI-LGC models can be defined based on LST theory. In this section, I focus on a general MI-LGC model that uses indicator-specific growth factors. 

# 5.5.3.2 Model Description

Figure 5.9 shows an MI-LGC model with indicator-specific growth factors for modeling linear trait changes across time. This model was first presented by Eid et al. (2012) and has subsequently been labeled the indicator-specific growth (ISG) model (Bishop et al., 2015). The basic idea of the ISG model parallels the MTMS approach that I described in Section 5.4.4. Recall that in the MTMS approach, each measured variable has its own (indicator-specific) trait factor 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/d28bafa7683887b634ec0e6cca33f80822eb8777f8fb22379177fff7bf60250d.jpg)



FIGURE 5.8. Path diagram of the structural model pertaining of an STMS model with linear trait change (also known as second-order linear growth model; McArdle, 1988). $\xi _ { 1 } =$ latent trait factor at Time 1 (random intercept factor); $( \xi _ { 2 } - \xi _ { 1 } ) =$ latent trait-change score variable (random slope factor); $\zeta _ { t } =$ latent state residual variable.


$\xi _ { \mathrm { i } }$ to account for the fact that different indicators may not measure exactly the same trait. Correlations between the trait factors indicate the extent to which indicators are homogeneous versus represent distinct traits or facets of the same trait. The linear ISG model can be understood as a generalization of the MTMS model. In the ISG model, each indicator has its own (initial) trait factor $\xi _ { \mathrm { i l } }$ as well as its own trait-change (linear slope) factor $( \xi _ { i 2 } - \xi _ { i 1 } )$ . 

In Figure 5.9, trait change is assumed to be linear as implied by the factor loadings on the linear slope factors $( \xi _ { \mathrm { i } 2 } - \xi _ { \mathrm { i } 1 } )$ , which are fixed to $t - 1$ for all indicators. Hence, in contrast to the MTMS model, the ISG model allows for linear trait changes across time. Similar to the MTMS model, the trait factors $\xi _ { \mathrm { i l } }$ can all be correlated, indicating the extent to which the indicators share similar trait components at Time 1. The initial trait factors $\xi _ { \mathrm { i l } }$ can also correlate with the linear slope factors $( \xi _ { i 2 } - \xi _ { i 1 } )$ . These correlations indicate whether initial trait differences are related to individual differences in linear trait changes in the same and/or different measures. Moreover, all linear slope factors can be correlated. These correlations can be examined to study the extent to which trait changes in one indicator are related to changes in another indicator. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/fffa86d09f288dbed9ea7b3f1b04791b7a61b8022c4cb2b94eb8050cda79b9dc.jpg)



FIGURE 5.9. Path diagram of an indicator-specific linear growth curve (ISG) model for three observed variable $Y _ { i t }$ that are measured on four time points. $\xi _ { \mathrm { i } 1 } =$ indicatorspecific latent trait factor at Time 1 (random intercept factor); $( \xi _ { _ { 1 2 } } - \xi _ { _ { 1 1 } } ) =$ indicatorspecific latent trait-change score variable (random slope factor); $\zeta _ { t } =$ latent state residual variable; $\varepsilon _ { i t } =$ measurement error variable; $\ S _ { \mathrm { i } } =$ constant state residual factor loading. All factor loadings on the random intercept factors $\xi _ { \mathrm { i 1 } }$ are fixed to 1. All intercept and slope factors can be correlated.


In the same way as in the MTMS model, the ISG model also includes common state residual factors $\zeta _ { t }$ at each time point as well as measurement error variables $\varepsilon _ { i t } ^ { \phantom { } }$ . Therefore, the ISG model allows separating linear trait changes from occasion-specific variability and variance due to random measurement error. 

In summary, the ISG model combines features of the single-indicator linear LGC model with features of the MTMS model. When there is no linear trait change in any indicator, the ISG model reduces to the MTMS model. In cases in which there is only one measured variable, the model reduces to a singleindicator linear LGC model without state residual factors. 

Formally, the linear ISG model can be expressed by the following measurement equation: 

$$
Y _ {i t} = \xi_ {i 1} + (t - 1) \cdot (\xi_ {i 2} - \xi_ {i 1}) + \delta_ {i} \cdot \zeta_ {t} + \varepsilon_ {i t} \text {f o r a l l} t = 1, \dots , n
$$

where $\delta _ { i }$ denotes a constant time-invariant state residual factor loading parameter. 

The measurement equation shows that the linear ISG model simplifies to the MTMS model when $( \xi _ { i 2 } - \xi _ { i 1 } ) = 0$ (i.e., when there is no linear trait change). Moreover, when the variance of the slope factor is zero [i.e., $V a r ( \xi _ { i 2 } - \xi _ { i 1 } ) = 0 ]$ , but the mean of the slope factor differs from zero [i.e., $E ( \xi _ { i 2 } - \xi _ { i 1 } ) \neq 0 ]$ , the linear ISG model simplifies to a version of the MTMS model in which all individuals change linearly by the same amount $( t - 1 ) \cdot E ( \boldsymbol { \xi } _ { i 2 } - \boldsymbol { \xi } _ { i 1 } )$ . 

In summary, the linear ISG model estimates the following parameters: 

•	 m intercept trait factor means $E ( \xi _ { \mathrm { i l } } )$ , 

•	 m intercept trait factor variances $V a r ( \xi _ { \mathrm { i l } } )$ 

• $0 . 5 ( m ^ { 2 } - m )$ intercept trait factor covariances $C o v ( \xi _ { i 1 } , \xi _ { j 1 } ) , i \neq j$ 

•	 m linear slope factor means $E ( \xi _ { \scriptscriptstyle i 2 } - \xi _ { \scriptscriptstyle i 1 } )$ 

•	 m linear slope factor variances $V a r ( \xi _ { { \scriptscriptstyle \mathrm { i } } 2 } - \xi _ { { \scriptscriptstyle \mathrm { i } } 1 } )$ 

• $0 . 5 ( m ^ { 2 } - m )$ linear slope factor covariances $C o \nu [ ( \xi _ { i 2 } - \xi _ { i 1 } )$ $C o v [ ( \xi _ { i 2 } - \xi _ { i 1 } ) , ( \xi _ { j 2 } - \xi _ { j 1 } ) ] , i \neq j ,$ 

• $m ^ { 2 }$ intercept-slope factor covariances $C o v [ \xi _ { \mathrm { i l } }$ , $( \zeta _ { j 2 } - \zeta _ { j 1 } ) ]$ 

•	 n state residual factor variances Var $( \zeta _ { t } )$ , 

• $m - 1$ time-invariant state residual factor loadings $\delta _ { i } .$ , and 

•	 nm measurement error variances $V a r ( \varepsilon _ { i t } )$ . 

Note that as in the MTMS model, only $m - 1$ time-invariant state residual factor loadings $\delta _ { i }$ need to be estimated because one loading has to be fixed for each state residual factor $\zeta _ { t }$ to identify the scale of this factor. The linear ISG model thus has $3 m + 2 m ^ { 2 } + m - 1 + n + n m$ free model parameters. For our 4 time points $\times 3$ measures design, we obtain $9 + 1 8 + 2 + 4 + 1 2 = 4 5$ free parameters. We have 90 pieces of information, and so the linear ISG model here has 45 df. In Box 5.11, I show how the linear ISG model can be defined based on LST-R theory. 

# 5.5.3.3 Variance Decomposition and Coefficients

The linear ISG model implies the following variance decompositions: 

$$
\begin{array}{l} V a r \left(\tau_ {i t}\right) = V a r \left(\xi_ {i 1}\right) + (t - 1) ^ {2} \cdot V a r \left(\xi_ {i 2} - \xi_ {i 1}\right) + 2 \cdot (t - 1) \cdot C o v \left[ \xi_ {i 1}, \left(\xi_ {i 2} - \xi_ {i 1}\right) \right] \\ + \delta_ {i} ^ {2} \cdot \operatorname {V a r} (\zeta_ {t}) \\ \end{array}
$$

$$
\begin{array}{l} V a r \left(Y _ {i t}\right) = V a r \left(\tau_ {i t}\right) + V a r \left(\varepsilon_ {i t}\right) \\ = \operatorname {V a r} \left(\xi_ {i 1}\right) + (t - 1) ^ {2} \cdot \operatorname {V a r} \left(\xi_ {i 2} - \xi_ {i 1}\right) + 2 \cdot (t - 1) \cdot \operatorname {C o v} \left[ \xi_ {i 1}, \left(\xi_ {i 2} - \xi_ {i 1}\right) \right] \\ + \delta_ {i} ^ {2} \cdot \operatorname {V a r} \left(\zeta_ {t}\right) + \operatorname {V a r} \left(\varepsilon_ {i t}\right) \\ \end{array}
$$

# BOX 5.11. Defining the Linear ISG Model Based on LST‑R Theory

Using concepts of LST-R theory, we can define the linear ISG model based on the following assumptions: 

1. Linear trait change: $\begin{array} { r } { \xi _ { _ { i t } } = \xi _ { _ { i 1 } } + ( t - 1 ) \cdot ( \xi _ { _ { i 2 } } - \xi _ { _ { i 1 } } ) } \end{array}$ for all $i , j = 1 .$ , . . . , m and $t = 1$ , . . . , n. 

2. Occasion- specific congenericity of latent state residual variables: All latent state residual variables that are measured at the same time point are assumed to be positive linear functions of each other, such that $\zeta _ { i t } = \delta _ { i j t }$ ⋅ $\zeta _ { j t }$ for i, $j = 1$ , . . . , m and $t = 1$ , . . . , n. This assumption is equivalent to assuming a common latent state residual factor $\zeta _ { t }$ at each time point such that: $\zeta _ { i t } = \delta _ { i t } \cdot \zeta _ { t } .$ . Here, I assume that the factor loadings $\delta _ { i t }$ are time- invariant. Therefore, I deleted the index $t$ from these parameters (i.e., $\delta _ { \mathrm { i } }$ instead of $\delta _ { i t } )$ . 

3. Linear independence of latent trait-change and measurement error variables: It is assumed that $C o v [ ( \xi _ { \mathrm { i } 2 } , - \xi _ { \mathrm { i } 1 } )$ $C o v [ ( \xi _ { i 2 } , - \xi _ { i 1 } ) , \varepsilon _ { i t } ] = C o v ( \varepsilon _ { i t } , \varepsilon _ { j t } ) = 0 \ :$ . 

The assumption of occasion- specific congenericity again implies the homogeneity of indicator- specific state residuals at a given time point. The assumption of equivalence of latent trait variables means that trait components remain stable across time and affect all states in the same way. The third assumption specifies that trait- change variables are uncorrelated with error variables and that error variables at the same time point are uncorrelated. Notice that other correlations between trait/trait- change, state residual, and measurement error variables are zero by definition in LST-R theory, so that additional assumptions are not required (see Box 1.2 in Chapter 1). 

Notice that since the intercept and slope factors can be correlated in the model, their covariance $C o v [ \xi _ { \mathrm { i l } } .$ , $\left( \zeta _ { i 2 } - \zeta _ { i 1 } \right) ]$ has to be taken into account in the variance decompositions. This means that trait variance due to the initial (intercept) trait factor cannot be separated from trait variance due to the traitchange (slope) factor— unless intercept and slope factors happen to be uncorrelated. 

The consistency (Con), occasion- specificity $( O s p )$ , and reliability (Rel) coefficients are calculated in a similar way as in the MTMS model. The only difference is that both the intercept and slope factor variances as well as their covariance have to be included in the computations: 

$$
\begin{array}{l} C o n \left(\tau_ {i t}\right) = \left. \operatorname {V a r} \left(\xi_ {i 1}\right) + (t - 1) ^ {2} \cdot \operatorname {V a r} \left(\xi_ {i 2} - \xi_ {i 1}\right) + 2 \cdot (t - 1) \right. \\ \left. \cdot C o v \left[ \xi_ {i 1}, \left(\xi_ {i 2} - \xi_ {i 1}\right) \right] \right\} / V a r \left(\tau_ {i t}\right) \\ \end{array}
$$

$$
O s p \left(\tau_ {i t}\right) = \delta_ {i} ^ {2} \cdot \operatorname {V a r} \left(\zeta_ {t}\right) / \operatorname {V a r} \left(\tau_ {i t}\right)
$$

$$
\begin{array}{l} C o n \left(Y _ {i t}\right) = \left. \operatorname {V a r} \left(\xi_ {i 1}\right) + (t - 1) ^ {2} \cdot \operatorname {V a r} \left(\xi_ {i 2} - \xi_ {i 1}\right) + 2 \cdot (t - 1) \right. \\ \left. \cdot C o v \left[ \xi_ {i 1}, \left(\xi_ {i 2} - \xi_ {i 1}\right) \right] \right\} / V a r \left(Y _ {i t}\right) \\ \end{array}
$$

$$
O s p \left(Y _ {i t}\right) = \delta_ {i} ^ {2} \cdot \operatorname {V a r} \left(\zeta_ {t}\right) / \operatorname {V a r} \left(Y _ {i t}\right)
$$

$$
\begin{array}{l} R e l (Y _ {i t}) = \operatorname {V a r} (\tau_ {i t}) / \operatorname {V a r} (Y _ {i t}) \\ = 1 - \left[ \operatorname {V a r} \left(\varepsilon_ {i t}\right) / \operatorname {V a r} \left(Y _ {i t}\right) \right] \\ = C o n \left(Y _ {i t}\right) + O s p \left(Y _ {i t}\right). \\ \end{array}
$$

The Con coefficient here represents the proportion of variability that is due to differences in initial trait scores and/or trait changes. The Osp and Rel coefficients have the same interpretation as in previously described models. Mplus by default only prints the reliability coefficients $R e l ( Y _ { i t } )$ under R-SQUARE Observed Variable when the standardized solution (STDYX) is requested. The computation of the remaining coefficients can again be accomplished in Mplus by using the MODEL CONSTRAINT option, as I demonstrate in the following Mplus application. 

# 5.5.3.4 Mplus Application

Imagine a researcher wants to study the natural development of cognitive abilities across a period of four time points. That is, in contrast to the example used to illustrate the LST-TC model, there is no intervention (training) in this case. Rather, the researcher is simply interested in the extent to which cognitive abilities change naturally, for example, through maturation and/or retest effects. He tests a sample of $N = 3 0 0$ individuals and assumes that cognitive abilities increase linearly across time. Below is the Mplus MODEL statement for a linear ISG model: 

```objectivec
MODEL:  
KSI11 by Y11@1 Y12@1 Y13@1 Y14@1;  
KSI21 by Y21@1 Y22@1 Y23@1 Y24@1;  
KSI31 by Y31@1 Y32@1 Y33@1 Y34@1;  
KSILIN1 by Y12@1 Y13@2 Y14@3;  
KSILIN2 by Y22@1 Y23@2 Y24@3;  
KSILIN3 by Y32@1 Y33@2 Y34@3;  
[Y11-Y34@0];  
[KSI11-KSI31*];  
[KSILIN1-KSILIN3*]; 
```

```txt
ZETA1 by Y11@1  
Y21 (d2)  
Y31 (d3);  
ZETA2 by Y12@1  
Y22 (d2)  
Y32 (d3);  
ZETA3 by Y13@1  
Y23 (d2)  
Y33 (d3);  
ZETA4 by Y14@1  
Y24 (d2)  
Y34 (d3);  
KSI11-KSI31 KSILIN1-KSILIN3 with ZETA1-ZETA4@0;  
ZETA1-ZETA4 with ZETA1-ZETA4@0; 
```

In the first part of the MODEL command, I defined the indicator-specific intercept (KSIi1) and linear slope (KSILINi) factors. Subsequently, I fixed all observed variable constant intercepts to zero and requested that the latent trait (intercept and slope) factor means be estimated in the same way as in the singleindicator LGC and MTMS models. Next, I defined the state residual factors with time-invariant loadings $\delta _ { i }$ as in the MTMS model. Lastly, I fixed all covariances between state residual factors and trait factors as well as between state residual factors to zero. 

The Mplus output for the linear ISG model contained the following warning message about a nonpositive definite latent variable covariance matrix that I described briefly for the MTMS model in Section 5.4.4: 

```txt
WARNING: THE LATENT VARIABLE COVARIANCE MATRIX (PSI) IS NOT POSITIVE DEFINITE. THIS COULD INDICATE A NEGATIVE VARIANCE/RESIDUAL VARIANCE FOR A LATENT VARIABLE, A CORRELATION GREATER OR EQUAL TO ONE BETWEEN TWO LATENT VARIABLES, OR A LINEAR DEPENDENCY AMONG MORE THAN TWO LATENT VARIABLES. CHECK THE TECH4 OUTPUT FOR MORE INFORMATION. PROBLEM INVOLVING VARIABLE KSILIN3. 
```

This message can indicate that in the estimation of a model, one or more latent factor variances were estimated to be negative or that two or more latent variables have an estimated correlation that is greater than 1.0 or smaller than –1.0. Such “improper solutions” can have a variety of causes, some of which are rather benign (Chen, Bollen, Paxton, Curran, & Kirby, 2001). For example, in some situations individuals do not change over time with regard to one or more trait factors. In this case, the corresponding latent trait-change score variables will have means and variances of zero in the population. In a sample drawn from this population, the latent trait-change score variances may be estimated 

to be negative simply due to sampling fluctuations. In other words, the variance of such a factor would be zero within sampling error. In the present example, this was the case for the trait-change factor KSILIN3 pertaining to the third measure. That is, I simulated the example data in such a way that the KSILIN3 trait-change factor had a mean and variance of zero in the population.2 Below are selected unstandardized parameter estimates from the linear ISG model: 

<table><tr><td colspan="5">MODEL RESULTS</td></tr><tr><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-Tailed P-Value</td></tr><tr><td>Means</td><td></td><td></td><td></td><td></td></tr><tr><td>KSI11</td><td>99.670</td><td>0.849</td><td>117.367</td><td>0.000</td></tr><tr><td>KSI21</td><td>49.877</td><td>0.548</td><td>91.003</td><td>0.000</td></tr><tr><td>KSI31</td><td>0.000</td><td>0.058</td><td>0.004</td><td>0.997</td></tr><tr><td>KSILIN1</td><td>0.723</td><td>0.410</td><td>1.765</td><td>0.078</td></tr><tr><td>KSILIN2</td><td>1.098</td><td>0.226</td><td>4.868</td><td>0.000</td></tr><tr><td>KSILIN3</td><td>0.000</td><td>0.013</td><td>0.009</td><td>0.992</td></tr><tr><td>Variances</td><td></td><td></td><td></td><td></td></tr><tr><td>KSI11</td><td>185.180</td><td>17.838</td><td>10.381</td><td>0.000</td></tr><tr><td>KSI21</td><td>71.791</td><td>7.519</td><td>9.548</td><td>0.000</td></tr><tr><td>KSI31</td><td>0.841</td><td>0.085</td><td>9.838</td><td>0.000</td></tr><tr><td>KSILIN1</td><td>41.639</td><td>4.252</td><td>9.792</td><td>0.000</td></tr><tr><td>KSILIN2</td><td>10.591</td><td>1.361</td><td>7.780</td><td>0.000</td></tr><tr><td>KSILIN3</td><td>-0.002</td><td>0.006</td><td>-0.344</td><td>0.731</td></tr><tr><td>ZETA1</td><td>45.148</td><td>15.207</td><td>2.969</td><td>0.003</td></tr><tr><td>ZETA2</td><td>25.636</td><td>9.639</td><td>2.660</td><td>0.008</td></tr><tr><td>ZETA3</td><td>25.082</td><td>9.866</td><td>2.542</td><td>0.011</td></tr><tr><td>ZETA4</td><td>14.117</td><td>10.496</td><td>1.345</td><td>0.179</td></tr></table>

We can see that the trait-change factor mean of the first trait-change factor KSILIN1 was estimated to be $E ( \xi _ { 1 2 } - \xi _ { 1 1 } ) = 0 . 7 2 3$ and was not statistically significant $\mathit { S E } = 0 . 4 1$ , $z = 1 . 7 6 5$ , $p = . 0 7 8 )$ . We can conclude that individuals’ average trait-level performance on the first cognitive ability measure did not change significantly across time. However, the variance of the same factor was substantial, $V a r ( \xi _ { 1 2 } - \xi _ { 1 1 } ) = 4 1 . 6 3 9$ , $S E = 4 . 2 5 2$ . This indicates that although on average there were no trait changes with regard to the first measure, there was substantial variability in trait change across time in Measure 1. 

The second trait-change factor KSILIN2 showed both a significant mean $[ E ( \xi _ { 2 2 } - \xi _ { 2 1 } ) = 1 . 0 9 8$ , $S E = 0 . 2 2 6$ , $z = 4 . 8 6 8$ , $p < . 0 0 1 ]$ and a substantial variance estimate $[ V a r ( \xi _ { 2 2 } - \xi _ { 2 1 } ) = 1 0 . 5 9 1$ , $S E = 1 . 3 6 1 $ ]. We can conclude that, with regard to the second measure’s trait component, individuals on average changed linearly by 1.098 points per unit of time. There were also individual differences in change with regard to the second cognitive ability measure. 

Recall that the third trait-change factor KSILIN3 was involved in the Mplus warning message that I discussed above. Now we can see why: The variance of the KSILIN3 factor was estimated to be very small and negative, $V a r ( \xi _ { 3 2 }$ $- \xi _ { 3 1 } ) = - 0 . 0 0 2$ , $S E { = } 0 . 0 0 6$ . Furthermore, the mean of KSILIN3 was estimated to be zero and was not statistically significant, $E ( \xi _ { 3 2 } - \xi _ { 3 1 } ) = 0 . 0 0 0$ , $S E = 0 . 0 1 3$ , $z = 0 . 0 0 9$ , $p = . 9 9 2$ . Given that both the mean and variance of KSILIN3 were essentially zero, we can conclude that no true trait changes were present in the third cognitive ability measure. As a result, we can remove the $( { \xi } _ { 3 2 } - { \xi } _ { 3 1 } )$ factor from the model without a decline in model fit. 

The effect of the state residual factors can be examined by looking at the standardized factor loadings that are given below (note that the standardized trait and trait-change factor loadings are not as easily interpreted in the ISG model as the intercept and slope factors can be correlated): 

<table><tr><td colspan="2">STANDARDIZED MODEL</td><td>RESULTS (STDYX</td><td colspan="3">Standardization)</td></tr><tr><td></td><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-TailedP-Value</td></tr><tr><td>ZETA1</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y11</td><td></td><td>0.438</td><td>0.074</td><td>5.948</td><td>0.000</td></tr><tr><td>Y21</td><td></td><td>0.237</td><td>0.052</td><td>4.610</td><td>0.000</td></tr><tr><td>Y31</td><td></td><td>0.209</td><td>0.043</td><td>4.821</td><td>0.000</td></tr><tr><td>ZETA2</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y12</td><td></td><td>0.314</td><td>0.059</td><td>5.277</td><td>0.000</td></tr><tr><td>Y22</td><td></td><td>0.168</td><td>0.034</td><td>4.908</td><td>0.000</td></tr><tr><td>Y32</td><td></td><td>0.155</td><td>0.033</td><td>4.657</td><td>0.000</td></tr><tr><td>ZETA3</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y13</td><td></td><td>0.253</td><td>0.050</td><td>5.033</td><td>0.000</td></tr><tr><td>Y23</td><td></td><td>0.145</td><td>0.030</td><td>4.832</td><td>0.000</td></tr><tr><td>Y33</td><td></td><td>0.154</td><td>0.034</td><td>4.534</td><td>0.000</td></tr><tr><td>ZETA4</td><td>BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y14</td><td></td><td>0.154</td><td>0.057</td><td>2.687</td><td>0.007</td></tr><tr><td>Y24</td><td></td><td>0.094</td><td>0.038</td><td>2.490</td><td>0.013</td></tr><tr><td>Y34</td><td></td><td>0.114</td><td>0.044</td><td>2.607</td><td>0.009</td></tr></table>

We can see that the standardized state residual factor loadings are rather small, indicating that the construct under study was mostly trait-like. For a more detailed look at this issue, researchers can compute the consistency and occasion-specificity coefficients using the formulas presented above. As before, this can be done in Mplus via the MODEL CONSTRAINT option. Below is an example for the second measure at Time 3 $( Y _ { 2 3 } )$ : 

```txt
MODEL:  
. . .  
KSI21* (KSIVAR21);  
KSILIN2* (KSILIN2V); 
```

```txt
KSI21 with KSILIN2* (COV21);  
ZETA3* (ZETA3VAR);  
Y23* (EPS23VAR);  
...  
MODEL CONSTRAINT:  
NEW(TAU23VAR Y23VAR CONTAU23 OSPTAU23 CONY23 OSPY23 RELY23);  
TAU23VAR = KSIVAR21 + 4*KSILIN21 + 4*COV21 + d2**2*ZETA3VAR;  
Y23VAR = TAU23VAR + EPS23VAR;  
CONTAU23 = (KSIVAR21 + 4*KSILIN21 + 4*COV21) / TAU23VAR;  
OSPTAU23 = d2**2*ZETA3VAR / TAU23VAR;  
CONY23 = (KSIVAR21 + 4*KSILIN21 + 4*COV21) / Y23VAR;  
OSPY23 = d2**2*ZETA3VAR / Y23VAR;  
RELY23 = CONY23 + OSPY23; 
```

In the first step, I added labels in the general MODEL statement to all relevant parameters to be used in MODEL CONSTRAINT. In this case, the relevant parameters used in the formulas to compute consistency and occasion specificity are the intercept and slope factor variances, their covariance, the state residual factor variance, the state residual factor loading (which was already labeled previously as d2 to set this parameter equal across time in the original MODEL statement that I presented earlier), and the measurement error variance. For example, I labeled the relevant intercept factor variance Var $( \xi _ { 2 1 } )$ as KSIVAR21 in the general MODEL statement. 

In MODEL CONSTRAINT, I first defined the relevant true score variance $V a r ( \tau _ { 2 3 } )$ as TAU23VAR as well as the model-implied observed variance $V a r ( Y _ { 2 3 } )$ as (Y23VAR). Subsequently, I implemented the relevant formulas for the computation of consistency, occasion specificity, and reliability. As usual, the relevant newly computed coefficients are printed under NEW/ADDITIONAL Parameters in the Mplus output: 

```txt
New/Additional Parameters
```
... 
CONTAU23 0.975 0.010 95.854 0.000
OSPTAU23 0.025 0.010 2.433 0.015
CONY23 0.828 0.021 39.347 0.000
OSPY23 0.021 0.009 2.416 0.016
RELY23 0.849 0.020 41.411 0.000 
```

We can see that the consistency coefficients are large, whereas the occasionspecificity coefficients are quite small. The estimated reliability $[ R e l ( Y _ { 2 3 } ) = . 8 4 9 ]$ is identical to the $R ^ { 2 }$ value given by Mplus as part of the standardized solution as it should be (not shown here). This indicates that our MODEL CONSTRAINT computations were accurate. 

In summary, we can conclude from the results of the linear ISG model that average linear cognitive ability trait changes occurred only for the second measure. The means of the other two linear trait-change factors were not statistically significant, indicating no average linear change with regard to the trait components pertaining to Measures 1 and 3. However, both Measure 1 and Measure 2 showed substantial variability in linear trait changes over time, whereas Measure 3 did not show any trait changes across time. Situation and/or person $\times$ situation interaction influences (occasion-specific effects) were minimal as is expected for most tests of cognitive abilities. 

# 5.5.3.5 Summary

The linear ISG model allows researchers to study linear trait changes separately for each indicator, while at the same time accounting for potential situational and/or interactional components and measurement error influences. The model does not require the presence of a specific event or intervention, and it can be estimated with as few as three measurement occasions. A particular strength of the model is that it allows studying changes in different facets of a construct simultaneously. That is, the model does not require all indicators to show the same patterns of change. There may be facets or items that showed greater change than others. As shown in the example application, the model even allows for the possibility that one or more measures do not show trait changes at all. Moreover, the amount of variability in change may differ between indicators, and changes in the trait components of one measure may or may not be correlated with changes in another measure’s trait component. The possibility to account for indicator specificity in change is particularly useful for longitudinal researchers who suspect that, for example, a developmental process or intervention affects different facets or indicators of a construct separately. For example, aging processes may have less impact on overall life satisfaction than on physical health (as facets of a global well-being construct). 

One restriction is that the linear ISG model assumes either zero or strictly linear trait change for all measures. If the pattern of trait change is nonlinear, the model would be misspecified. In cases of misfit, a researcher may try including additional nonlinear (e.g., quadratic) components for some or all indicators or estimate the change function freely based on the data (as illustrated in Chapter 3, Section 3.5.3 for single-indicator data). The ISG model also assumes that, although indicators may reflect different traits and/or trait-change processes, they share the same occasion-specific (situation and/or person $\times$ situation interaction) influences at each time point within scaling differences (different state 

residual loadings are allowed). This assumption may be violated in practice, especially when indicators reflect rather distinct constructs. 

# 5.6 CHAPTER SUMMARY

Historically, longitudinal researchers have typically used measurement designs and statistical models for a single measured variable per construct at each time point. For example, until recently, it used to be standard practice to specify latent growth curve models exclusively with single indicators per construct. In this chapter, I emphasized the advantages of multiple-indicator designs and presented a variety of longitudinal models for such data. Most of the models presented in this chapter have counterparts for single-indicator data that I presented in Chapter 3. Table 5.1 summarizes key properties of the multipleindicator longitudinal models discussed in Chapters 4 and 5. In the next section, I discuss the advantages and limitations of multiple-indicator designs and models. 

# 5.6.1 Advantages of Multiple‑Indicator Models

# 5.6.1.1 Model Identification and df

With multiple indicators, the total amount of available information (observed means, variances, and covariances) that can be used to estimate model parameters of interest is much larger than in single-indicator designs. As a consequence, model identification does not rest on assumptions that are as strict as the assumptions made by a number of single-indicator models. For example, the simplex and TSE models that I presented in Chapter 3 require at least four measurement occasions as well as equality constraints on certain parameters to be identified. They also require the presence of certain data conditions (e.g., autoregressive effects $\neq 0$ ) to be identified. 

Their counterparts in the world of multiple-indicator models (i.e., the LAS and many LST models) can already be analyzed with as few as two or three time points and generally do not require equality restrictions on measurement error or latent state residual variances. Multiple-indicator models with three or more indicators also do not require the presence of autoregressive effects for model identification. 

As a result of a greater amount of available information, multiple-indicator models tend to have more df than the corresponding single-indicator models. 


mary and Comparison of Models for Multiple‑Indicator Longi


<table><tr><td>Model</td><td>No. of waves needed for identificationa</td><td>No. of free parameters (3 measures, 4 waves)</td><td>No. of latent factors</td><td>Longitudinal process</td><td>Variance components</td><td>Coefficients</td><td>Autoregressive process?</td></tr><tr><td>LS (Chapter 4)</td><td>2</td><td>42 (without invariance restrictions)</td><td>n states</td><td>Flexible</td><td>State, measurement error</td><td>Reliability</td><td>Not explicitly specified, but possible</td></tr><tr><td>LS-IS (Chapter 4)</td><td>2 (when IS factors are correlated)</td><td>45 (without invariance restrictions)</td><td>n states, m-1indicator-specific residual factors</td><td>Flexible</td><td>Reference state, indicator-specific factor, measurement error</td><td>Convergent validity, indicator specificity, reliability</td><td>Not explicitly specified, but possible</td></tr><tr><td>LSC-IS</td><td>2 (when IS factors are correlated)</td><td>45 (without invariance restrictions)</td><td>n states, n-1state change, n-1state change residuals, m-1indicator-specific residual factors</td><td>State change</td><td>Reference state, indicator-specific factor, measurement error, residual change</td><td>Convergent validity, indicator specificity, reliability, R2(for change score variables)</td><td>Yes (regression of change scores on previous states)</td></tr><tr><td>LAS</td><td>2</td><td>39 (without invariance restrictions)</td><td>n states, n-1state residuals</td><td>Autoregressive (first order)</td><td>Previous state, state residual, measurement error</td><td>Consistency, occasion specificity, reliability</td><td>Yes</td></tr><tr><td>STMS</td><td>2</td><td>34 (without invariance restrictions)</td><td>n states, 1 trait, n state residuals</td><td>State variability, trait stability</td><td>Trait, state residual, measurement error</td><td>Consistency, occasion specificity, reliability</td><td>Autoregression among states or state residuals can be added</td></tr></table>

<table><tr><td>STMS-IS</td><td>2 (when IS factors are correlated)</td><td>37 (without invariance restrictions)</td><td>n states, 1 trait, n state residuals, m - 1 indicator-specific residual factors</td><td>State variability, trait stability</td><td>Reference trait, reference state residual, indicator-specific factor, measurement error</td><td>Common consistency, unique consistency, occasion specificity, reliability</td><td>Autoregression among states or state residuals can be added</td></tr><tr><td>MTMS</td><td>2</td><td>33 (without invariance restrictions)</td><td>m traits, n state residuals</td><td>State variability, trait stability</td><td>Trait, state residual, measurement error</td><td>Consistency, occasion specificity, reliability</td><td>Autoregression among state residuals can be added</td></tr><tr><td>LST-TC</td><td>4</td><td>25 (assuming strong ME)</td><td>1 trait, 1 trait change, n state residuals</td><td>State variability, trait change between two time periods</td><td>Trait/ trait change, state residual, measurement error</td><td>Consistency, occasion specificity, reliability</td><td>Autoregression among traits and/or state residuals can be estimated</td></tr><tr><td>Linear ISG</td><td>3</td><td>45</td><td>m trait, m trait change, n state residuals</td><td>State variability, linear trait change</td><td>Trait/linear trait change, state residual, measurement error</td><td>Consistency, occasion specificity, reliability</td><td>Autoregression among state residuals can be added</td></tr></table>


e indicators per wave; many models are identifiable even with only two indicators and two waves un tistate indicator-specific MTMS = multitrait–multistate LST-TC = latent state–trait with trait change ISG = = latent state-indicator-specific; LSC = latent state change; LA(C)S = latent autoregressive (crosslagged) states; ST ;;; 


Therefore, the models can be seen as more parsimonious and/or as containing a greater number of testable restrictions (i.e., each df reflects a testable restriction for the mean or covariance structure of the measured variables). More testable restrictions imply that a model puts the data at hand at a harder test (the model is more likely to be falsified in an empirical application). This implies that multiple-indicator models allow for more stringent tests of social science theories about longitudinal processes. 

# 5.6.1.2 Fewer Estimation Problems

At least some single-indicator models are prone to issues of empirical underidentification that may result in convergence failures or improper solutions (e.g., negative variance estimates). One such model is the TSE model that I described in detail in Chapter 3. This model appears to work well in practice only under a fairly restricted set of conditions. Problems such as the ones encountered with the TSE model have been shown to be less common with corresponding multiple-indicator models (such as the trait–state occasion [TSO] model and other LST models with autoregression; see Cole et al., 2005). 

# 5.6.1.3 ME Testing

As I explained in detail in Chapter 4, multiple-indicator models have the important advantage that they allow researchers to test the degree of ME across time to ensure that changes across time can be meaningfully interpreted. Singleindicator models are limited in terms of tests of ME as they only allow testing whether the measurement error variance remained constant across time. 

# 5.6.1.4 Indicator Homogeneity versus Method Effects

Multiple-indicator models also allow researchers to study the degree of homogeneity (unidimensionality) of their measures and make it possible to quantify method (indicator-specific) effects. No such effects can be studied with singleindicator data. With multiple-indicator data, indicator heterogeneity can be modeled in several ways. I presented one approach that uses method (IS ) factors and one approach that uses indicator-specific trait (and/or trait change) factors. Both approaches can be formulated within the framework of LST-R theory. 

Gaining information on the homogeneity of the measures can be valuable for several reasons. First, such information can provide evidence for or against the convergent validity of the measures (i.e., do all measures of a construct really 

measure that construct?). A researcher may choose to discard and/or replace measures that show strong indicator specificity. 

Second, knowledge about the degree of indicator homogeneity can provide information on the nature of a construct and its facets. For example, how many facets does a construct have, and how strongly or weakly are they related? Do all facets change in the same way across time? Are the trait components of different facets related in the same way to external variables? Do measures pertaining to different facets share the same occasion-specific (state residual) influences? The MTMS approach (Section 5.4.4) as well as indicator-specific trait-change and growth curve models (Section 5.5) provide answers to these questions that single-indicator approaches would not be able to address. 

# 5.6.1.5 Modeling Autoregressive Effects (or Not)

Autoregressive effects are common in longitudinal data. Multiple-indicator models offer more flexibility in the modeling of such effects because they do not suffer from the same identification constraints as do single-indicator models. For example, LST models such as the STMS, STMS-IS, or MTMS models can all be specified with autoregressive effects. However, in contrast to the TSE model, these models do not depend on the presence of autoregressive effects to be mathematically identified. Hence, these models can also be used when lags between measurement occasions are so long that autoregressive effects may be zero or close to zero. In addition, they offer more flexibility in terms of including autoregressive effects either among latent state variables (Steyer & Schmitt, 1994) or among latent state residual/occasion residual variables (Cole et al., 2015; Eid et al., 2017). 

# 5.6.1.6 Greater Statistical Power to Detect Interindividual Differences in Change

Another advantage of multiple-indicator designs is that they have been shown to provide greater statistical power to detect interindividual differences in intraindividual change across time compared to single-indicator designs (von Oertzen et al., 2010). Such gains in power likely stem from the fact that multipleindicator designs contain more information than single-indicator designs. This implies that the use of a greater number of indicators can compensate to a certain extent for a smaller sample size. This makes multiple-indicator models especially attractive in situations in which researchers can use many measures but are able to recruit only a limited number of subjects. 

# 5.6.1.7 Separation of Trait, Trait‑Change, State Residual, and Measurement Error Components

In contrast to most single-indicator models (with the exception of the TSE model), a number of multiple-indicator models allow for a clear separation of variance components due to trait and/or trait change (person effects), state residual (situation and/or person $\times$ situation interaction) effects, and random measurement error. In this sense, multiple-indicator models are more in line with the basic ideas of LST-R theory according to which (1) measurement does not take place in a situational vacuum and (2) measurements tend to contain random error in addition to systematic sources of variability. In other words, person, situation, interaction, and error influences should be taken into account when modeling longitudinal data. 

On the practical side, the ability of multiple-indicator models to separate the above-mentioned variance components allows researchers to study change over time in a more fine-grained way. Multiple-indicator models make it possible to study simultaneously the extent to which one or more constructs show longterm trait changes versus more short-term state fluctuations (occasion-specific variability). In this way, researchers can find out more about the longitudinal course of constructs under study and examine, for example, whether interventions cause endurable trait changes or merely short-term state fluctuations. 

# 5.6.2 Limitations of Multiple‑Indicator Models

# 5.6.2.1 Need to Collect More Data

Although multiple-indicator designs have clear advantages over single-indicator designs, there are also some downsides. One obvious shortcoming of the multiple-indicator approach is that it requires researchers to collect data on more variables. Many longitudinal studies can only employ a limited number of items per scale for various reasons (e.g., time, money). In these situations, it may be difficult or even impossible to employ multiple-indicator models, and researchers therefore have to make use of approaches for single-indicator data as presented in Chapters 2 and 3. However, even with few items, multiple-indicator models can be used. A researcher could either conduct the analyses at the item level or construct item parcels to have multiple indicators available. 

# 5.6.2.2 Higher Complexity

Another issue with multiple-indicator models is that they are more complex. Researchers may be unsure about their correct specification, especially when 

multiple constructs and/or external covariates are involved. (Hopefully, this chapter provides a useful contribution to resolving this issue.) Related to this issue and as mentioned previously, multiple-indicator models almost always have a larger number of df compared to their single-indicator counterparts. Although implying greater parsimony and more stringent testability, more df also mean a greater likelihood of model misfit, as each df implies a testable (i.e., falsifiable) restriction for the mean and/or covariance structure of the observed variables. Given the greater overall model complexity of multiple-indicator models, it may be more difficult for a researcher to determine the sources of misfit (there may be more than one) and potential remedies. In my experience, model misfit is frequently related to the heterogeneity of indicators. In these cases, models with method or indicator-specific factors often provide a more reasonable model fit than models with general state or trait factors. In this chapter, I presented several models that take indicator heterogeneity into account (i.e., the LS-IS, STMS-IS, MTMS, and ISG models), and in my experience, these models often fit empirical data quite well. 

The increased complexity of multiple-indicator models also means that these models can be more difficult to communicate in empirical research presentations and papers (for guidelines, see Chapter 8, this volume). As of yet, not everybody is familiar with multiple-indicator models, and so more explanations may be needed when presenting empirical research using these models. Moreover, there are typically more parameter estimates to report, and therefore, the presentation of the results may also require more journal space than is usually needed for single-indicator longitudinal models. 

Despite these limitations, I believe that overall, the advantages of multipleindicator models clearly outweigh their limitations. Given a careful selection of measures, multiple-indicator models often fit empirical data quite well (particularly models such as the LS-IS, STMS-IS, MTMS or ISG models, which take indicator heterogeneity into account), and they offer a lot more flexibility in the modeling of longitudinal processes than do single-indicator models. In the next chapter, I discuss how longitudinal structural equation models can be analyzed in intensive longitudinal designs using long-format data. 

# 5.7 RECOMMENDED READINGS



Bishop, J., Geiser, C., & Cole, D. A. (2015). Modeling growth with multiple indicators: A comparison of three approaches. Psychological Methods, 20, 43–62. 





Eid, M., Courvoisier, D. S., & Lischetzke, T. (2012). Structural equation modeling of ambulatory assessment data. In M. R. Mehl & T. S. Connor (Eds.), Handbook 





of research methods for studying daily life (pp. 384–406). New York: Guilford Press. 





Little, T. D. (2013). Longitudinal structural equation modeling. New York: Guilford Press. 





Prenoveau, J. M. (2016). Specifying and interpreting latent state–trait models with autoregression: An illustration. Structural Equation Modeling, 23, 731–749. 





Steyer, R., Mayer, A., Geiser, C., & Cole, D. A. (2015). A theory of states and traits: Revised. Annual Review of Clinical Psychology, 11, 71–98. 



# NOTES



1. It is important to note that the experimental design used in the present example was rather weak as there was no control group. Hence, we cannot necessarily assume that the observed mean change was due to the training. Alternative explanations could be maturation or learning (retest) effects. A better design would be one with a control group and random assignment to groups. In this case, the same model could be used within a multigroup SEM framework (Jöreskog, 1971b; Steyer et al., 2015). 





2. Another possible cause of the warning message shown above is an out-of-bounds correlation estimate. In the MTMS and ISG models, often trait or trait-change factors will be highly correlated in the population, particularly when measures are highly homogeneous. In some cases, latent trait or trait-change correlations may be equal to 1.0 in the population (i.e., when measures have perfectly correlated trait or trait-change components). Samples drawn from the population may result in sample estimates greater than 1.0 due to sampling error. In these cases, researchers can combine the factors that are perfectly correlated. 



![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/e7adeca596dfd7a72a48988ca4c1c9c8c4f486535c42356c06998d741510ad94.jpg)


# Modeling Intensive Longitudinal Data

# 6.1 INTRODUCTION

More and more longitudinal studies employ designs with a large number of measurements that may be taken over a relatively short period of time. As an example, consider ecological momentary assessment (EMA) studies that track individuals’ mood levels several times a day over a period of 2 or more weeks (e.g., Eid et al., 2012; Shiffman, Stone, & Hufford, 2008). Such intensive longitudinal or time-series designs have great advantages because they allow researchers to collect a lot more longitudinal information. As a result, such studies allow examining variability and changes in a much more fine-grained way than do more traditional longitudinal studies in which only three or four measurements are taken per person. 

For example, intensive longitudinal studies allow uncovering cyclic variations in hormone levels and relating those variations to changes in emotions or cognitive (e.g., spatial) abilities. Moreover, intensive longitudinal designs allow studying the potential effects of specific week days on, for example, individuals’ mood levels as well as variations in mood levels. 

The increased amount of information gathered through intensive longitudinal designs does not come without challenges. As discussed in Chapter 7, longitudinal data are prone to dropout or nonresponse, resulting in missing observations. Intensive longitudinal designs may contain a lot of missing data. Moreover, time intervals in intensive longitudinal designs often vary both 

within and between individuals, resulting in the need to include a continuous time variable. 

Because of the complications associated with intensive longitudinal designs, I devote this chapter to modern statistical methods for analyzing intensive longitudinal data. I begin with a review of some of the key special features of intensive longitudinal data. Subsequently, I show how selected single- and multiple-indicator longitudinal models can be applied to intensive longitudinal data using the Mplus software. The final portion of this chapter deals with a new dynamic structural equation modeling (DSEM) framework (Asparouhov, Hamaker, & Muthén, 2018) that makes the analysis of intensive longitudinal data more flexible. 

# 6.2 SPECIAL FEATURES OF INTENSIVE LONGITUDINAL DATA

# 6.2.1 Introduction

Data sets resulting from intensive longitudinal designs typically differ in several ways from data sets obtained in “conventional” longitudinal studies with a smaller number of measurements. In this section, I review some of the special aspects of intensive longitudinal data as they are relevant for the application of longitudinal structural equation models (SEMs). 

# 6.2.2 Wide‑ versus Long‑Format Data

All longitudinal analyses that I have described so far in this book used data sets in so-called wide format as input for the statistical analyses. Wide format means that in the data set, each individual is represented by one (and only one) row and each variable at each time point is represented by a separate column. Given that in this data format each variable at each time point has its own column, we obtain a rather “wide” data set, particularly when there are many variables and/ or many measurement occasions in the study. 

To illustrate, consider the small hypothetical wide-format data set in Table 6.1. In this example, there are three individuals and two measured variables $( Y _ { 1 t }$ and $Y _ { 2 t } )$ , each of which is measured on three time points $( t = 1 , 2 , 3 )$ . As a result, the data set has three rows and seven columns. Wide-format data sets are practical when a researcher deals with a relatively small number of measurement occasions as in this example. With intensive longitudinal data, there are typically a lot more than three measurement occasions. When there are many time points, analyses using wide-format data often become impractical. For example, in an intensive longitudinal study with 30 measurement occasions, an analysis 


TABLE 6.1. Example of a Small Hypothetical Wide‑Format Longitudinal Data Set for Three Individuals, Two Measured Variables, and Three Time Points


<table><tr><td>Individual</td><td>Y11</td><td>Y21</td><td>Y12</td><td>Y22</td><td>Y13</td><td>Y23</td></tr><tr><td>1</td><td>10</td><td>12</td><td>9</td><td>8</td><td>11</td><td>11</td></tr><tr><td>2</td><td>7</td><td>Missing</td><td>9</td><td>8</td><td>10</td><td>8</td></tr><tr><td>3</td><td>12</td><td>11</td><td>Missing</td><td>Missing</td><td>12</td><td>10</td></tr></table>


Note. $Y _ { \mathrm { i } t } =$ measured variable $\overset { \cdot } { 1 } =$ indicator, $t =$ time point); “Missing” indicates a missing score. 


using the latent state (LS) model presented in Chapter 4 would have to specify 30 latent state variables (one for each measurement occasion) with all their loadings etc. 

As I show in this chapter, so-called long-format data can make the representation and analysis of intensive longitudinal data more convenient and compact. Table 6.2 illustrates the long-format approach to representing longitudinal data. Note that Table 6.2 shows the same data as Table 6.1. 

We can see that the data set in long format shown in Table 6.2 has more rows but fewer columns than the wide-format version presented in Table 6.1. This is because in Table 6.2, each individual is represented by as many rows as this individual contributes time points, making the data set longer (creating more rows). In contrast, each variable $Y _ { i t }$ is now represented by just one column, regardless 


TABLE 6.2. The Same Data as Shown in Table 6.1 Now Represented in Long Format


<table><tr><td>Individual</td><td>Time t</td><td>Y1t</td><td>Y2t</td></tr><tr><td>1</td><td>1</td><td>10</td><td>12</td></tr><tr><td>1</td><td>2</td><td>9</td><td>8</td></tr><tr><td>1</td><td>3</td><td>11</td><td>11</td></tr><tr><td>2</td><td>1</td><td>7</td><td>missing</td></tr><tr><td>2</td><td>2</td><td>9</td><td>8</td></tr><tr><td>2</td><td>3</td><td>10</td><td>8</td></tr><tr><td>3</td><td>1</td><td>12</td><td>11</td></tr><tr><td>3</td><td>3</td><td>12</td><td>10</td></tr></table>


Note. $Y _ { i t } =$ measured variable $( { \mathrm { i } } =$ indicator, $t =$ time point); “missing” indicates a missing score. 


of the number of time points, thus reducing the number of columns. Instead of including as many columns per variable as there are time points, the long-format structure uses a time variable to represent the time points for each individual (column Time t in Table 6.2). The time variable can be continuous (e.g., time in minutes, hours, days) or discrete (Time 1, Time 2, Time 3, . . . , Time n). 

Notice that missing observations are in part represented in a different, more compact way in the long-format version of the data set compared to the wide-format version. Individual #3 missed both variables at Time 2. As a consequence, this individual had “blank cells” for the columns labeled $Y _ { 1 2 }$ and $Y _ { 2 2 }$ in the wide-format version of the data. In contrast, in the long-format version, Individual #3 is simply missing the entire row for Time 2. In other words, the long-format version does not require a missing value code for time points that an individual misses entirely. 

Notice, however, that Individual #2 who missed just the second variable $( Y _ { 2 2 } )$ at Time 2 still has a blank cell that requires a missing value code even in the long-format version. This is because Individual #3 still provided data for the first variable $( Y _ { 1 2 } )$ at Time 2. 

The long-format version of the data is more practical for intensive longitudinal designs as it is more compact. It also makes clear that longitudinal studies implicitly deal with a multilevel (hierarchical) sampling design: Time points are nested within individuals. Because of this hierarchical data structure, multilevel statistical modeling techniques, including multilevel SEM (Muthén, 1994), can be used to analyze longitudinal data. As I show in this chapter, multilevel modeling is particularly useful for intensive longitudinal designs in which there are many measurement occasions per individual. 

# 6.2.3 Imbalanced Time Points

In intensive longitudinal designs, measurements are frequently imbalanced both between and within individuals. This means that the distances between measurements may not be the same between time points for different individuals. In addition, for a given individual, measurement occasions may have different time intervals between them. 

Long-format data sets are able to easily accommodate imbalanced time points because they allow for the inclusion of a continuous time variable (see above). In contrast, the wide-format approach is less flexible when it comes to modeling continuous time with many missing observations. This is because wide-format data require a separate column for each time point. This would result in many columns and many empty (missing) cells for designs with a continuous time metric and many different time points and would not be practical. 

# 6.2.4 Autoregressive Effects

Intensive longitudinal designs often imply that measurements are not only plentiful, but also closely spaced in time (e.g., multiple measurements of the same individuals within several hours of the same day). As a result of close temporal spacing, autoregressive effects are common in intensive longitudinal data, meaning that measurements that are adjacent or have small lags between them are more highly correlated than measurements with greater lags. In previous chapters, I showed how such effects can be modeled in simplex, ACL, and LST models using wide-format data. The DSEM approach that I discuss in Section 6.3.6 enables researchers to take autoregressive effects into account when modeling intensive longitudinal data. In the following section, I show how some of the longitudinal models that I described for wide-format data in previous chapters can be applied to intensive longitudinal data in a long format using multilevel modeling techniques. 

# 6.3 SPECIFYING LONGITUDINAL SEMs FOR INTENSIVE LONGITUDINAL DATA

# 6.3.1 Introduction

As I discussed in the previous sections, one key aspect of intensive longitudinal data is that such data are most conveniently arranged in long (as opposed to wide) format. Although wide-format data could be used in principle, it is often not practical, especially when the number of measurement occasions is large. When using data in long format, multilevel (a.k.a. hierarchical linear) statistical modeling techniques have to be used to properly analyze the data. This is because the long format results in a two- (or more) level structure in which time points (Level 1) are nested within individuals (Level 2). Below, I introduce the idea of multilevel modeling of longitudinal data based on a single-indicator design. Later on, I show how more complex models for multiple indicators can be specified using multilevel SEM techniques. A more detailed discussion of the general multilevel modeling approach with applications in Mplus can be found in Heck and Thomas (2015). 

# 6.3.2 The Random Intercept Model as a Multilevel Model

Recall that the first longitudinal model that I introduced in Chapter 2 was a single-indicator random intercept model. For convenience, this same model is again depicted in Figure 6.1A for a design with a single indicator that is measured 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/71c0baa1caf4ef6eaf8838f0f4eceb750086c7eeb320df48539be10b04568719.jpg)



FIGURE 6.1. Path diagram of the random intercept model for a single observed variable $Y _ { t }$ that is measured on four time points. $\xi =$ trait (random intercept) factor; $\varepsilon _ { t } =$ measurement error variable. A: Wide-format single-level confirmatory factor analysis version; B: Long-format multilevel regression analysis version.


on four measurement occasions. There is a single random intercept (or trait) factor $\xi$ that represents interindividual differences in true trait scores. In addition, residual variables $\varepsilon _ { t }$ represent random measurement error. 

Remember that the random intercept model is often used as a baseline “no change” model in longitudinal studies as it assumes constant trait scores within each individual. That is, the model implies that if measured scores $( Y _ { t } )$ change over time, this is solely due to the effects of random measurement error $( \varepsilon _ { t } )$ but not to changes in the true trait scores $( \xi )$ . Researchers may test the random intercept model in the first step of a longitudinal analysis to examine whether there have been any changes in a construct under study. More complex longitudinal models are only needed if the random intercept model can be rejected for a given data set. Here, I use the random intercept model as a simple model to introduce the basic concepts of multilevel modeling of longitudinal data in long format. 

As I mentioned above, longitudinal data have a hierarchical (a.k.a. nested) two-level structure in which time points (Level 1, intraindividual or within-person level) are nested within individuals (Level 2, interindividual or between-person level). Multilevel statistical models allow analyzing statistical models simultaneously for both levels. In conceptual terms, the Level-1 

model for two-level longitudinal data describes intraindividual (within-person) differences across time, whereas the Level-2 model describes interindividual (between-person) differences, for example, with regard to trait or trait-change scores. 

As an example, consider the multilevel version of the random intercept model which is depicted in the path diagram in Figure 6.1B. We can see that in the multilevel representation of the model, all time-specific variables (i.e., variables that carry a subscript t for time) as well as the time variable are modeled on Level 1 (the “within-person” level). In the random intercept model, time-specific variables are (1) the measured variables $Y _ { t }$ and (2) the measurement error variables $ { \varepsilon } _ { t }$ . These variables can show variation within persons (intraindividual differences) across time. In contrast, the latent trait (random intercept) variable in this model is timeunspecific and is therefore modeled on Level 2 (the “between-person” level). This is because there can be interindividual (between-person), but not intraindividual (within-person) differences in trait scores in the random intercept model (trait scores are assumed to be perfectly stable within individuals in this model). 

We can see that at Level 1, the measured variables are regressed on the time variable. The black dot at the end of the regression arrow (labeled ξ) indicates that the intercept of this regression is a random coefficient. “Random coefficient” means that the intercept is not a constant as in conventional regression analysis but rather a variable that can vary across individuals (Level-2 units). In terms of the Mplus modeling framework, the random intercept coefficient is a latent variable that has a mean and variance parameter at Level 2. In our case, the random intercept coefficient is identical to the common trait factor $\xi ,$ which is modeled at Level 2. 

Remember that one key assumption in the random intercept model is that there is no trait change across time. In Figure 6.1B, this is expressed by the fact that the linear slope coefficient in the regression of Y on time is set to zero. The model thus implies that the values of Y do not depend linearly on time. In other words, in the random intercept model, any variation in Y values across time can only be due to variation in measurement error scores as reflected in the error variance parameter $V a r ( \varepsilon )$ ; there is no variation in $\xi$ scores across time. At Level 2, we estimate the mean and variance of the $\xi$ factor, as shown in Figure 6.1B. 

In summary, the multilevel model version of the random intercept factor model provides the same parameters as the conventional single-factor CFA model, but implicitly assumes time-invariance of the measurement error variance parameter Var(ε). It is equivalent to a CFA version of the random intercept model in which the measurement error variances $V a r ( \varepsilon _ { t } )$ are set equal across time. Therefore, the multilevel version of the random intercept model only 

estimates three free parameters: the mean of the trait factor, $E ( \xi )$ , the variance of the trait factor, $V a r ( \xi )$ , and one measurement error variance, Var(ε). 

For illustrative purposes, I fit the multilevel version of the random intercept model to the same data set that I used in Chapter 2 to illustrate the model application to wide- format data $\mathrm { \Delta N } = 3 0 0$ , four measurement occasions, no missing data). Recall that in this data set, individuals’ IQ scores were examined across four measurement occasions. For the present illustration, I transformed the data from wide to long format in the same Mplus input file that is used to specify the model (for more details on wide-to-long data transformations in Mplus, see Box 6.1): 

```txt
TITLE: Random intercept model specified as a multilevel model  
DATA: File = CH2.2_Random_Intercept.dat; 
```

# BOX 6.1. Wide‑to‑Long Data Transformation of Data in Mplus

In Mplus, the DATA WIDETOLONG command can be used to transform a data set that is in wide format to long format. Below I discuss the relevant commands that are required in Mplus to carry out a wide-to-long transformation. In the main text, I illustrate this for the data set that I used in Chapter 2 to demonstrate the application of the random intercept model in Mplus. 

DATA:FILE $\equiv$ data.dat;   
DATA WIDETOLONG:   
WIDE $=$ X1-X4 Y1-Y4; LONG $\equiv$ X |Y; IDVARIABLE $=$ person; REPETITION $=$ time; 

In the example above, the WIDE $=$ X1-X4 | Y1-Y4; subcommand in the DATA WIDETOLONG command is used to specify that the variables X1, X2, X3, and X4 as well as the variables Y1, Y2, Y3, and Y4 are in wide format in the original data file “data.dat” specified under DATA: FILE $=$ data.dat;. The LONG = X | Y; subcommand specifies that both the X1-X4 and the Y1-Y4 variables are to be transformed to long format. The IDVARIABLE $=$ person; option allows us to add a person ID variable to the new long- format data set in line with the example shown in Table 6.2. The REPETITION $=$ time; option produces a time variable (compare Table 6.2). 

The newly created long- format variables as well as the person and time variables need to be listed under USEVARIABLES in the VARIABLE command when a multilevel model is specified (see the example described in the text). 

```matlab
DATA WIDETOLONG:  
    WIDE = Y1-Y4;  
    LONG = Y;  
    IDVARIABLE = person;  
    REPETITION = time;  
VARIABLE: NAMES = Y1-Y4;  
    USEVARIABLES = Y person time;  
    CLUSTER = person;  
    WITHIN = time;  
ANALYSIS: TYPE = TWOLEVEL;  
MODEL: %WITHIN%  
    Y ON time@0;  
    Y;  
    %BETWEEN%  
    KSI BY Y@1;  
    [KSI*];  
    KSI;  
    [Y@0];  
    Y@0;  
OUTPUT: SAMPSTAT; 
```

We can see that the same data set as in Chapter 2 (named CH2.2_ Random_Intercept.dat) was used here. The DATA WIDETOLONG command in conjunction with the WIDE $=$ Y1-Y4; and LONG $=$ Y; subcommands specifies that the four measured variables Y1-Y4 are in wide format in the original data file CH2.2_Random_Intercept.dat and are to be transformed to long format for the analysis of the random intercept model. Furthermore, I requested that a person ID variable (IDVARIABLE $=$ person;) as well as a time variable (REPETITION $=$ time;) be created by Mplus for use in the multilevel modeling version of the random intercept analysis. 

In the VARIABLE command, the newly created Y, person, and time variables are listed under USEVARIABLES so that they can subsequently be used in the MODEL statement. In addition, the CLUSTER $=$ person; option is included to identify the multilevel data structure (here, time points nested within persons). This enables Mplus to identify the two levels of the analysis. At Level 1 (referred to as the WITHIN level by Mplus), time-varying variables are modeled that may show within-person (intraindividual) changes. At Level 2 (referred to as the BETWEEN level by Mplus), time-invariant variables are modeled that may show differences between people (interindividual differences) but not within-person differences across time. The option WITHIN $=$ time; specifies that the time variable is a variable that will only be used at Level 1. 

The ANALYSIS option is used to request a multilevel analysis with two levels (TYPE $=$ TWOLEVEL). In the MODEL statement, a separate model is specified for each of the two levels. The Level-1 part of the random intercept model 

is specified under %WITHIN%. In the random intercept model, the Level-1 part consists of two portions. First is the linear relationship between the time variable and Y, which is constrained to zero (Y on time@0;). As I explained above, this is done because the random intercept model assumes no changes across time other than spurious fluctuations due to random measurement error. Mplus still includes the random intercept coefficient of the Level-1 regression of Y on time as the default. As I show below, the mean and variance of this random intercept are modeled as latent variable parameters at Level 2. In the second part of the Level-1 model specification, I requested the estimation of the (time-invariant) measurement error variance parameter Var(ε) by specifying Y;. 

The Level-2 part of the model is specified under %BETWEEN%. The random intercept (trait) factor KSI is introduced using the usual BY statement with a fixed loading of 1. The trait factor mean [KSI]; and variance KSI; are estimated. Furthermore, the Y fixed intercept as well as the Y residual variance at Level 2 are set to zero. This is because (1) the random intercept model does not estimate a fixed intercept (additive constant) parameter and (2) the measurement error variance is modeled on Level 1. The OUTPUT option is used to request descriptive statistics (SAMPSTAT) for both levels of analysis. Below are Mplus output excerpts for the random intercept model: 

```txt
SUMMARY OF ANALYSIS Number of observations 1200   
SUMMARY OF DATA Number of clusters 300 Average cluster size 4.000 Estimated Intraclass Correlations for the Y Variables Intraclass Variable Correlation Y 0.889   
SAMPLE STATISTICS NOTE: The sample statistics for within and between refer to the maximum-likelihood estimated within and between covariance matrices, respectively. ESTIMATED SAMPLE STATISTICS FOR WITHIN Means Y TIME 0.000 1.500 Covariances Y TIME Y 26.070 TIME 0.070 1.250 
```

<table><tr><td colspan="3">Correlations</td></tr><tr><td></td><td>Y</td><td>TIME</td></tr><tr><td>Y</td><td>1.000</td><td></td></tr><tr><td>TIME</td><td>0.012</td><td>1.000</td></tr><tr><td colspan="3">ESTIMATED SAMPLE STATISTICS FOR BETWEEN Means</td></tr><tr><td></td><td>Y</td><td>TIME</td></tr><tr><td></td><td>100.280</td><td>0.000</td></tr><tr><td colspan="3">Covariances</td></tr><tr><td></td><td>Y</td><td>TIME</td></tr><tr><td>Y</td><td>209.699</td><td></td></tr><tr><td>TIME</td><td>0.000</td><td>0.000</td></tr><tr><td colspan="3">Correlations</td></tr><tr><td></td><td>Y</td><td>TIME</td></tr><tr><td>Y</td><td>1.000</td><td></td></tr><tr><td>TIME</td><td>0.000</td><td>0.000</td></tr></table>

Notice that the Number of observations here refers to the total number of data points, that is, 300 persons $\times 4$ time points $= 1 { , } 2 0 0$ . In this TWOLEVEL analysis, the number of persons is given under Number of clusters. (In general, Number of clusters gives the number of Level-2 units in Mplus when the TYPE $=$ TWOLEVEL option is used.) The average cluster size gives the average number of observations nested within the Level-2 units (here: persons). In our case, each of the 300 persons contributed four measurement occasions (there was no missing data). Therefore, the average cluster size in our example is four. 

Next, Mplus prints the estimated intraclass correlation coefficient (ICC). The ICC is given by estimated Level-2 variance $V a r ( Y _ { \mathrm { L e v e l } 2 } )$ divided by total measured variable variance $[ V a r ( Y _ { \mathrm { L e v e l \ 1 } } ) + V a r ( Y _ { \mathrm { L e v e l \ 2 } } ) ]$ : 

$$
\begin{array}{l} I C C (Y) = \operatorname {V a r} \left(Y _ {\text {L e v e l 2}}\right) / \left[ \operatorname {V a r} \left(Y _ {\text {L e v e l 1}}\right) + \operatorname {V a r} \left(Y _ {\text {L e v e l 2}}\right) \right] \\ = \operatorname {V a r} \left(Y _ {\text {B E T W E E N}}\right) / \left[ \operatorname {V a r} \left(Y _ {\text {W I T H I N}}\right) + \operatorname {V a r} \left(Y _ {\text {B E T W E E N}}\right) \right] \\ \end{array}
$$

The estimated Level-1 and Level-2 variances are given under SAMPLE STATISTICS by Mplus. In our example, we obtain 

$$
I C C (Y) = 2 0 9. 6 9 9 / (2 6. 0 7 + 2 0 9. 6 9 9) = . 8 8 9
$$

Notice that the estimated ICC value is exactly equal to the reliability $[ R e l ( Y )$ or $R ^ { 2 } ]$ estimate that we obtained in the wide-format analysis of the 

random intercept model. This makes sense because the ICC for the random intercept model partitions the measured variable variance into reliable (Level 2: trait) and unreliable (Level 1: measurement error) variance components. We can see again that the reliability of the measure is adequate (only about $1 1 \%$ of the measured variable variance is due to random errors of measurement). 

Subsequently, Mplus prints estimated sample statistics (means, covariances, and correlations) separately for each level. We can see that the time variable here has a mean of 1.5. This is because all persons contributed four time points (again, there was no missing data in this example) and the time variable was coded with values 0, 1, 2, 3 by Mplus. Given the uniform distribution of the time variable, the average value was 1.5. We can see that time was minimally correlated with Y at the WITHIN level $( r = . 0 1 2 )$ . This makes sense because the data were generated by the random intercept model, which assumes no linear changes across time. 

We already saw that the variance of Y at the WITHIN level was rather small (26.07) compared to the BETWEEN level variance (209.699), resulting in a large ICC (reliability) coefficient. The WITHIN level variance is equal (within a small rounding error) to the estimated common measurement error variance Var(ε), whereas the BETWEEN level variance is approximately equal to the estimated trait factor variance $V a r ( \xi )$ . The Y mean is given at the BETWEEN level and reflects (approximately) the estimated trait mean $E ( \xi )$ . 

Subsequently, Mplus provides a chi-square test of model fit, $\chi ^ { 2 } ( 1 ) , = 0 . 1 8$ , $p = . 6 7 1 2$ $p =$ . Notice that in contrast to the wide-format analysis of the random intercept model, the chi-square test of model fit here has only 1 df, whereas the wide-format version of the same model with equal error variances resulted in 11 df (the $p$ -values are similar, and both model versions fit well). This is because in the multilevel (long-format) version of the model, certain aspects of the model are not testable (i.e., do not result in additional df ). 

Specifically, the multilevel model does not allow testing the model-implied equality of the four means (3 df), four variances (3 df), and six covariances (5 df). Instead, it only tests whether Y is linearly unrelated to time (1 df ). In other words, the multilevel version of the model does not allow testing whether all measurement error variances are truly time-invariant and whether the fixed intercepts are truly zero in the population. These assumptions are implicitly made in the model but cannot be tested. The lack of testability of certain assumptions is one downside of the multilevel approach to longitudinal modeling compared to the wide-format confirmatory factor approach that I presented in previous chapters. Below are the Mplus parameter estimates for the random intercept model: 

<table><tr><td colspan="5">MODEL RESULTS</td></tr><tr><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-Tailed P-Value</td></tr><tr><td colspan="5">Within Level</td></tr><tr><td>Y ON</td><td></td><td></td><td></td><td></td></tr><tr><td>TIME</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Residual Variances</td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td>26.069</td><td>1.229</td><td>21.215</td><td>0.000</td></tr><tr><td colspan="5">Between Level</td></tr><tr><td>KSI BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Means</td><td></td><td></td><td></td><td></td></tr><tr><td>KSI</td><td>100.283</td><td>0.849</td><td>118.089</td><td>0.000</td></tr><tr><td>Intercepts</td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Variances</td><td></td><td></td><td></td><td></td></tr><tr><td>KSI</td><td>209.835</td><td>17.679</td><td>11.869</td><td>0.000</td></tr><tr><td>Residual Variances</td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr></table>

We can see that the model provides three parameter estimates: the (timeinvariant) measurement error variance at the WITHIN level (26.069) as well as the trait factor variance (209.835) and mean (100.283) at the BETWEEN level. The parameter estimates are very close to the estimates obtained from an analysis of the wide-format random intercept model with time-invariant measurement error variances (see the supplemental materials on the companion website for details [see the box at the end of the table of contents]). 

# 6.3.3 The Linear Growth Model as a Multilevel Model

As another single-indicator example, consider the linear latent growth curve (LGC) model presented in Chapter 3 (see Figure 6.2A for the wide-format CFA and Figure 6.2B for the long-format multilevel version of this model). Recall from Chapter 3 that the single-indicator linear LGC model can be seen as an extension of the random intercept model in which a linear trait-change (“random slope”) factor is added to the model. In the multilevel (long-format) version of the linear LGC model, both the random intercept and the random slope factor are modeled on the between-person level (Level 2) as shown in Figure 6.2B. This is because both factors represent between-person (interindividual) differences in trait and/or trait-change scores. 

Notice that the Level-1 part of the model is very similar to the Level-1 portion of the random intercept model. The only difference is that the regression slope coefficient in the linear regression of Y on time is not set to zero in the linear LGC model. Instead, the regression slope coefficient is now specified as 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/aaf8567c62142de1d14cac54fe0ad464cf3103f23950eed530f27fae510693a7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/f18970486f85096c33cbdabf30a7929a95e010c1d101f56ed122df3ad8d308d2.jpg)



FIGURE 6.2. Path diagram of a linear latent growth curve (LGC) model for a single observed variable $Y _ { t }$ that is measured on four time points. $\xi _ { 1 } = \mathrm { T i m e } { \cdot } 1$ (random intercept) trait factor; $( \xi _ { 2 } - \xi _ { 1 } ) =$ latent trait-change (random slope) factor; $\varepsilon _ { t } =$ measurement error variable. A: Wide-format single-level confirmatory factor analysis version; B: Long-format multilevel regression analysis version.


a random slope coefficient. In Figure 6.2B, this is indicated by a black dot in the middle of the regression arrow pointing from time to Y. In other words, the linear LGC model is a random coefficient regression model in which Y is linearly regressed on time and both the intercept and slope coefficients of this linear regression can vary across Level-2 units (persons). 

In the same way as in the random intercept model, the random slope is modeled as a latent variable with a mean and variance at Level 2. In our linear LGC model, the random intercept is identical to the initial trait factor $\xi _ { 1 }$ , and the random slope is identical to the linear trait-change factor $( \xi _ { 2 } - \xi _ { 1 } )$ . The intercept and slope factors at Level 2 each have a mean and variance estimated as well as a covariance between them. 

For the Mplus illustration, I applied the linear LGC model to the same data $\langle N = 3 0 0$ , IQ scores on four measurement occasions, no missing data) that I used to illustrate the wide-format version of the model in Chapter 3 (data file: CH3.5.2_Linear_Growth.dat). I applied the exact same wide-to-longformat transformation to the data that I used when fitting the multilevel random intercept model in Section 6.2.2 (see Box 6.1). Below are the Mplus ANALY-SIS and MODEL commands for the linear LGC model specified as a multilevel model: 

```txt
ANALYSIS: TYPE = TWOLEVEL RANDOM; ESTIMATOR = ML;  
MODEL: %WITHIN%  
KSI21 | Y on time;  
Y;  
%BETWEEN%  
KSI1 by Y@1;  
[KSI1*];  
[KSI21*];  
KSI1 with KSI21;  
[Y@0];  
Y@0; 
```

The ANALYSIS type is now TWOLEVEL RANDOM. This is because the linear LGC model includes not only a random intercept but also a random slope as part of the Level-1 regression of Y on time (i.e., the linear effect of time on Y is allowed to vary between individuals, i.e., at Level 2). In the MODEL statement, this is expressed by specifying KSI21 | Y on time; under %WITHIN%. KSI21 here represents the label that I chose for the linear slope factor [notice that the label is the same as the one that I chose in the wide-format analysis to indicate the linear trait-change factor $\displaystyle ( \xi _ { 2 } - \xi _ { 1 } ) ]$ . The | symbol indicates that the 

slope in the linear regression of Y on time is a random coefficient that can have a mean and variance parameter at Level 2 (variation between individuals). 

At the BETWEEN level, the random intercept factor is specified in the same way as in the random intercept model (but was given the label KSI1 here to indicate that this factor now represents trait differences between individuals at the first measurement occasion). Both the random intercept and the random slope factor have mean and variance parameters that are estimated at the BETWEEN level. Furthermore, their covariance (KSI1 with KSI21;) is estimated as well. The Level-2 fixed intercept and residual variance for Y are set to zero as in the random intercept model. 

Notice that Mplus as of Version 8 does not provide a chi-square test of model fit for linear growth curve models that are specified as random coefficient (multilevel) regression models using the TWOLEVEL RANDOM option. However, information criteria such as the Bayesian information criterion (BIC) are still provided that can be used to compare different models for a given data set. Again, the limited information on model fit is one downside of the multilevel specification of longitudinal models. Below are the Mplus parameter estimates for the linear LGC model specified as a multilevel model: 

<table><tr><td colspan="5">MODEL RESULTS</td></tr><tr><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-Tailed P-Value</td></tr><tr><td>Within Level</td><td></td><td></td><td></td><td></td></tr><tr><td>Residual Variances</td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td>33.049</td><td>1.911</td><td>17.298</td><td>0.000</td></tr><tr><td>Between Level</td><td></td><td></td><td></td><td></td></tr><tr><td>KSI1 BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>KSI1 WITH KSI21</td><td>-20.709</td><td>5.145</td><td>-4.025</td><td>0.000</td></tr><tr><td>Means</td><td></td><td></td><td></td><td></td></tr><tr><td>KSI21</td><td>2.134</td><td>0.307</td><td>6.949</td><td>0.000</td></tr><tr><td>KSI1</td><td>100.186</td><td>0.903</td><td>110.962</td><td>0.000</td></tr><tr><td>Intercepts</td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Variances</td><td></td><td></td><td></td><td></td></tr><tr><td>KSI21</td><td>21.670</td><td>2.338</td><td>9.268</td><td>0.000</td></tr><tr><td>KSI1</td><td>221.428</td><td>20.007</td><td>11.068</td><td>0.000</td></tr><tr><td>Residual Variances</td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr></table>

As in the random intercept model, at the WITHIN level, only the timeinvariant measurement error variance (33.049) is estimated. At the BETWEEN 

level, we obtain estimates of the growth factor means (intercept: 100.186; slope: 2.134), variances (intercept: 221.428; slope: 21.67), and their covariance (–20.709). We can see from the slope factor mean that on average, there was an increase in about two IQ points per unit of time. The parameter estimates are again very similar to the corresponding estimates in a wide-format analysis of the linear LGC model with time-invariant measurement error variances (see supplemental materials on the companion website for details). In the next section, I show how multiple-indicator longitudinal models can be specified for long-format data within the multilevel modeling framework. 

# 6.3.4 The Multitrait–Multistate Model as a Multilevel Model

The multilevel approach to modeling long-format longitudinal data can also be applied to multiple-indicator designs (Geiser, Bishop, Lockhart, Shiffman, & Grenard, 2013). In the case of multiple-indicator data, multilevel SEM techniques that specify latent variables at each level (Muthén, 1994) are applied to properly model long-format data. As a first example, I consider the multitrait– multistate (MTMS) model that I described in detail in Chapter 5 (see Figure 6.3A for the single- and Figure 6.3B for the multilevel representation of this model). 

Notice that in contrast to the single-indicator random intercept and linear LGC models discussed above, the MTMS model specifies latent variables at both Level 1 and Level 2. At the between-person level (Level 2), we specify the indicator-specific trait factors $\xi _ { \mathrm { i } }$ . The trait factors are again modeled at Level 2 because these factors are time-invariant (their scores vary only between individuals but not across time). In contrast, the latent state residual factors $\zeta _ { t }$ are time-varying factors and are thus modeled at the within-person level (Level 1) along with the measurement error variables $\varepsilon _ { i t } ^ { \phantom { } }$ . The multilevel analysis version of the MTMS model assumes that the latent state residual factor loadings $\delta _ { i }$ , the measurement error variances $V a r ( \varepsilon _ { i t } )$ , and the latent state residual variances $V a r ( \zeta )$ are time-invariant. 

Figure 6.3B shows that the latent trait factors are again modeled as random intercept coefficients in the Level-1 regression of the $Y _ { i t }$ variables on time. This is indicated by the black dots at the end of the regression arrows in the Level-1 part of the model. The slope coefficients of these regressions are all fixed to zero, because this version of the MTMS model assumes no trait changes across time. 

For my illustration, I used the same data set as in Chapters 4 and 5 to illustrate the wide-format LS-IS and MTMS models (data set: CH5_LS-IS.dat, $N =$ 300, three measured variables per time point, four measurement occasions, no 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/4a1b62d1ef7f483b71297676a58703a2d02ae404fd6acf72e238f3c42f9dabd2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/80a20e78f924dabd9f9cdf397e0d53486ce0f2a75bc7c8d10788934069e68d01.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/e8aee73e5c6235395e667e315b58418108268cb5d72bcd8adbb0879f18c638ea.jpg)



FIGURE 6.3. Path diagram of a multitrait–multistate (MTMS) model for three observed variables $Y _ { i t }$ that are measured on four time points. $\xi _ { \mathrm { i } } =$ indicator-specific latent trait factor; $\zeta _ { t } =$ latent state residual variable; $\varepsilon _ { i t } =$ measurement error variable; $\delta _ { \mathrm { i } } =$ constant state residual factor loading. All trait factors can be correlated. A: Wide-format single-level confirmatory factor analysis version; B: Long-format multilevel confirmatory factor analysis version.


missing data). I applied a wide-to-long transformation as shown above. Below are the Mplus ANALYSIS and MODEL statements for the MTMS model specified as a multilevel SEM: 

```txt
ANALYSIS: TYPE = TWOLEVEL;  
ESTIMATOR = ML;  
MODEL: %WITHIN%  
Y1 Y2 Y3 on time@0;  
ZETA by Y1 Y2 Y3;  
ZETA*25;  
Y1*17.6 Y2*21.5 Y3*0.23;  
%BETWEEN%  
KSI1 by Y1@1;  
KSI2 by Y2@1;  
KSI3 by Y3@1;  
[KSI1-KSI3*];  
KSI1*182 KSI2*75 KSI3*0.79;  
KSI1-KSI3 with KSI1-KSI3;  
[Y1-Y3@0];  
Y1-Y3@0; 
```

The ANALYSIS: TYPE $=$ TWOLEVEL; option is chosen to specify a CFA model on both the WITHIN and the BETWEEN person level. Notice that the RANDOM option is not required here because the MTMS model does not include any random slope factors (i.e., trait change is assumed to be zero in the model). 

In the MODEL statement, the %WITHIN% (Level-1) part of the model includes the latent state residual factor with time-invariant loadings and variance as well as the time-invariant measurement error variance parameters. Notice that I provided starting values for the variance parameters on both levels. This is because in the example, the variances differ strongly between indicators, which can result in (benign) convergence problems. By providing userdefined starting values based on the results of the wide-format CFA analysis of the model, convergence is easily achieved. 

The %BETWEEN% (Level-2) part of the model features the indicator-specific trait factors with their means, variances, and covariances. The measured variable constant intercepts and residual variances at Level 2 are again set to zero in line with the definition of the model. Below, I discuss selected output information. 

```txt
Estimated Intraclass Correlations for the Y Variables  
Y1 0.810  
Y2 0.745  
Y3 0.754 
```

The ICCs in the MTMS analysis give the (time-invariant) measured variable consistency coefficients $C o n ( Y _ { i } )$ . Recall from Chapter 5 that $C o n ( Y _ { i } )$ gives the proportion of variability in an observed variable that is due to interindividual differences in trait scores. The $C o n ( Y _ { i } )$ coefficient is thus a measure of how trait-like a given measure is. The ICCs here are equal to the $C o n ( Y _ { i } )$ coefficients because the ICCs reflect Level-2 variance relative to total (Level- $\cdot 1 +$ Level-2) variance. In the MTMS model, Level-2 variance is trait variance only, whereas Level 1 reflects the remaining (state residual and measurement error) variance components. In this example, between about 75 and $8 1 \%$ of the variability in each measure is explained by trait differences between individuals, indicating that the measures reflect mostly trait-like constructs. 

Notice that in contrast to the single-indicator random intercept model discussed above, the ICCs in the MTMS model give consistency rather than reliability. This is because in the MTMS model, there are sources of reliable variation at both levels (Level 1: state residuals $\zeta _ { i } ,$ Level 2: traits $\xi _ { { \scriptscriptstyle i } } )$ , whereas in the random intercept model, reliable variance is only present at Level 2 (trait $\xi$ ). 

As shown in detail in Chapter 5, we can use the MODEL CONSTRAINT option to compute the remaining coefficients of interest (i.e., occasion specificity and reliability). The computation of these coefficients is shown in the full Mplus input file that is available from the companion website (see the box at the end of the table of contents). The estimated values are identical to the values presented for the wide-format analysis of the MTMS model in Chapter 5. 

The chi-square test of model fit in this example $[ \chi ^ { 2 } ( 3 ) = 0 . 3 5 3$ , $p = . 9 4 9 8 ]$ had 3 df and points to an excellent fit of the model. Notice once again that the multilevel version of the model provides (a lot!) fewer $d f$ (a less stringent test) compared to the wide-format CFA version (which, in this example, has 75 df). Again, there are many covariance and mean structure restrictions that are implied by the MTMS model that the multilevel framework does not allow us to test. The only assumption that is tested here is that there is no linear influence of time on any of the measured variables. This assumption would be violated if trait changes occurred across time. Below are selected unstandardized and standardized Mplus parameter estimates for the MTMS model: 

<table><tr><td colspan="5">MODEL RESULTS</td></tr><tr><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-Tailed P-Value</td></tr><tr><td>Within Level ZETA BY</td><td></td><td></td><td></td><td></td></tr><tr><td>Y1</td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y2</td><td>0.404</td><td>0.095</td><td>4.248</td><td>0.000</td></tr><tr><td>Y3</td><td>0.035</td><td>0.008</td><td>4.224</td><td>0.000</td></tr></table>

<table><tr><td colspan="6">Variances</td></tr><tr><td colspan="2">ZETA</td><td>25.074</td><td>6.050</td><td>4.144</td><td>0.000</td></tr><tr><td colspan="6">Residual Variances</td></tr><tr><td colspan="2">Y1</td><td>17.613</td><td>5.825</td><td>3.024</td><td>0.002</td></tr><tr><td colspan="2">Y2</td><td>21.450</td><td>1.379</td><td>15.553</td><td>0.000</td></tr><tr><td colspan="2">Y3</td><td>0.228</td><td>0.013</td><td>17.682</td><td>0.000</td></tr><tr><td colspan="6">Between Level</td></tr><tr><td colspan="6">KSI1 WITH</td></tr><tr><td colspan="2">KSI2</td><td>107.039</td><td>9.599</td><td>11.151</td><td>0.000</td></tr><tr><td colspan="2">KSI3</td><td>9.460</td><td>0.929</td><td>10.183</td><td>0.000</td></tr><tr><td colspan="6">KSI2 WITH</td></tr><tr><td colspan="2">KSI3</td><td>6.202</td><td>0.604</td><td>10.273</td><td>0.000</td></tr><tr><td colspan="6">Means</td></tr><tr><td colspan="2">KSI1</td><td>99.871</td><td>0.801</td><td>124.752</td><td>0.000</td></tr><tr><td colspan="2">KSI2</td><td>45.947</td><td>0.520</td><td>88.326</td><td>0.000</td></tr><tr><td colspan="2">KSI3</td><td>0.008</td><td>0.053</td><td>0.142</td><td>0.887</td></tr><tr><td colspan="6">Variances</td></tr><tr><td colspan="2">KSI1</td><td>181.593</td><td>15.707</td><td>11.561</td><td>0.000</td></tr><tr><td colspan="2">KSI2</td><td>74.798</td><td>6.637</td><td>11.269</td><td>0.000</td></tr><tr><td colspan="2">KSI3</td><td>0.793</td><td>0.070</td><td>11.310</td><td>0.000</td></tr><tr><td colspan="6">STANDARDIZED MODEL RESULTS (STDYX Standardization)</td></tr><tr><td colspan="2"></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-TailedP-Value</td></tr><tr><td colspan="6">Between Level</td></tr><tr><td colspan="6">KSI1 WITH</td></tr><tr><td colspan="2">KSI2</td><td>0.918</td><td>0.013</td><td>73.240</td><td>0.000</td></tr><tr><td colspan="2">KSI3</td><td>0.788</td><td>0.025</td><td>31.217</td><td>0.000</td></tr><tr><td colspan="6">KSI2 WITH</td></tr><tr><td colspan="2">KSI3</td><td>0.805</td><td>0.025</td><td>32.226</td><td>0.000</td></tr></table>

At the WITHIN level, we obtain estimates of the state residual factor loadings (the first loading is fixed as usual for identification, and the remaining two loadings are estimated to be 0.404 and 0.035), the state residual factor variance (25.074), and the time-invariant measurement error variances (17.613, 21.45, and 0.228). At the BETWEEN level, we again obtain the trait factor means, variances, and covariances. The standardized solution STDYX provides us with the correlations between the indicator-specific trait factors. These correlations are often of interest as they inform us about the degree of homogeneity of the trait components. 

# 6.3.5 The Indicator‑Specific Growth Model as a Multilevel Model

Another type of multiple-indicator longitudinal model that investigators are frequently interested in estimating for intensive longitudinal data are multipleindicator growth curve models. Here, I show the application of the linear indicator-specific growth (ISG) model presented in Chapter 5 to long-format data (see Figure 6.4A for the single- and Figure 6.4B for the multilevel representation of this model). 

Like the single-indicator LGC model that I presented in Section 6.3.2, the multilevel version of the multiple-indicator linear ISG specifies the (timeinvariant) intercept and slope factors at the between-person level (Level 2). As in the MTMS model, the latent state residual factors $\zeta _ { t }$ as time-varying factors are modeled at the within-person level (Level 1) along with the measurement error variables $\varepsilon _ { i t }$ . The multilevel analysis version of the linear ISG model assumes that the latent state residual factor loadings $\delta _ { \mathrm { i } }$ , the measurement error variances $V a r ( \varepsilon _ { i t } )$ , and the latent state residual variances $V a r ( \zeta )$ are time-invariant (again, these assumptions are not testable in this analysis). 

At Level 1, each $Y _ { i t }$ variable is regressed on time in a random coefficient regression model (i.e., a linear regression with both a random intercept and a random slope). This specification parallels the specification in the singleindicator linear LGC model above, except that we now have three rather than just one indicator. As a result, we also have multiple growth factors at Level 2 for which we can estimate the means, variances, and covariances with all other growth factors. The ISG can thus be seen as a multivariate random coefficient regression model with multiple outcomes (dependent variables) at Level 1. 

For my illustration of the linear ISG, I used the same simulated data set (transformed to long format) as presented in Chapter 5 (data set: CH5_ISG.dat, $N = 3 0 0$ , three measured variables per time point, four measurement occasions, no missing data). The data set was suitable for the long-format analysis because the data had been simulated with time-invariant Level-1 parameters (i.e., invariant state residual factor loadings, state residual factor variances, and measurement error variances). These measurement equivalence restrictions are implied by the multilevel version of the ISG model. Below are the Mplus ANALYSIS and MODEL statements for the linear ISG model specified as a multilevel SEM: 

```txt
ANALYSIS: TYPE = TWOLEVEL RANDOM;  
ESTIMATOR = ML;  
MODEL: %WITHIN%  
KSILIN1 | Y1 on time;  
KSILIN2 | Y2 on time; 
```


A


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/b41abf123b662a902f7e88c95e8f38649f38e596bdaddc3b7f37748d34c768c4.jpg)



B


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/b258ab3e2e77c4addb292ca9a090bf21911030e94162271e44576fcfada503be.jpg)



Level 1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/98cf29db5690bbe1cb0ea5d68dbfcc033bee1c38c16c577dfc916306247b8d0e.jpg)



FIGURE 6.4. Path diagram of an indicator-specific linear growth curve (ISG) model for three observed variables $Y _ { i t }$ that are measured on four time points. $\xi _ { \mathrm { i 1 } } =$ indicatorspecific latent trait factor at Time 1 (random intercept factor); $( \xi _ { \mathrm { i } 2 } - \xi _ { \mathrm { i } 1 } ) =$ indicatorspecific latent trait-change score variable (random slope factor); $\zeta _ { t } =$ latent state residual variable; $\varepsilon _ { \mathrm { i } t } =$ measurement error variable; $\delta _ { \mathrm { i } } =$ constant state residual factor loading. All factor loadings on the random intercept factors $\xi _ { \mathrm { i 1 } }$ are fixed to 1. All intercept and slope factors can be correlated. A: Wide-format single-level confirmatory factor analysis version; B: Long-format multilevel confirmatory factor analysis version.


```matlab
KSILIN3 | Y3 on time;  
ZETA by Y1@1 Y2 Y3;  
ZETA*20;  
Y1*11 Y2*22 Y3*0.24;  
%BETWEEN%  
KSI11 by Y1@1;  
KSI21 by Y2@1;  
KSI31 by Y3@1;  
[KSI11*100 KSI21*50 KSI31*0];  
[KSI11*0.7 KSI11*1 KSI11*0];  
KSI11*186 KSI21*72 KSI31*0.83;  
KSI11*43 KSI11*2*10 KSI11*0;  
KSI11 KSI21 KSI31 with KSI11 KSI21 KSI31;  
KSI11 KSI21 KSI31 KSI11-KSILIN3 with KSI11@0  
KSI11*0 KSI11*0;  
[Y1-Y3@0];  
Y1-Y3@0; 
```

Notice that the ANALYSIS TYPE for the ISG model is TWOLEVEL RAN-DOM because the model involves random slope (i.e., linear growth) factors. In the Level-1 (%WITHIN%) part of the model, the random slope factors KSILINi are defined in the same way as in the single-indicator linear growth model that I described above. For example, the statement KSILIN1 | Y1 on time; means that the slope in the linear regression of the indicator Y1 on time is a random coefficient with a mean and variance parameter estimated at the BETWEEN level (Level 2). Recall that in the ISG approach, there is a separate slope factor for each indicator. 

In addition, the latent state residual factor ZETA is also specified at the WITHIN level. All three measures have a (time-invariant) loading on ZETA (the first loading is fixed to 1.0 for identification). The time-invariant ZETA and measurement error variances are also estimated at Level 1. Notice that I provided user-defined starting values for the variances based on the true population parameters to facilitate convergence, given that the indicators in this example had rather different metrics. 

In the Level-2 (%BETWEEN%) part of the model, the indicator-specific random intercept (Time-1 trait) factors KSIi1 are specified in the same way as in the MTMS model. The means and variances of the random intercept and slope factors are estimated, except for the variance of the third slope factor (KSI-LIN3), which had a variance of zero in the population. When growth factors have variances close or equal to zero, this may cause convergence problems in the multilevel SEM analysis. Fixing the variances and covariances of such factors to zero can resolve this issue. 

I again provided starting values to facilitate convergence. In general, all intercept and slope factors in the ISG model can covary, and those covariances are estimated at the BETWEEN level. However, in this example, several covariances were assumed to be zero in the population model for simplicity, and so I also fixed them to zero in the Mplus MODEL command to avoid convergence problems in the example analysis. In the output file for the ISG model, Mplus again provides us with the estimated ICCs: 

<table><tr><td colspan="6">Estimated Intraclass Correlations for the Y Variables</td></tr><tr><td></td><td colspan="2">Intraclass</td><td colspan="2">Intraclass</td><td>Intraclass</td></tr><tr><td>Variable</td><td>Correlation</td><td>Variable</td><td>Correlation</td><td>Variable</td><td>Correlation</td></tr><tr><td>Y1</td><td>0.698</td><td>Y2</td><td>0.691</td><td>Y3</td><td>0.767</td></tr></table>

Recall that the ICCs indicate the ratio of Level-2 variance to total measured variance. Hence, in the ISG model, the ICCs indicate the (average) consistency coefficients $C o n ( Y _ { i } )$ for each indicator. In the ISG model, the $C o n ( Y _ { i } )$ coefficients tell us how much of the variability in a measure is accounted for by the initial trait (intercept) and trait-change (linear slope) factors combined. We can see that initial trait and trait-change factors on average accounted for between 69.1 and $7 6 . 7 \%$ of the observed variability in this example. The remaining variance is due to either state residual or measurement error influences (which are reflected at Level 1). Consistency, occasion specificity, and reliability coefficients for specific time points can again be computed manually for specific time points using the previously described MODEL CONSTRAINT option. 

Notice that given the ANALYSIS TYPE for the ISG model is TWOLEVEL RANDOM, we do not obtain a chi-square test of model fit in Mplus. This again illustrates one downside of the multilevel approach to specifying longitudinal SEM models: No tests of absolute model fit are currently available for models with random slopes. Researchers using the multilevel approach are only provided with information criteria (e.g., AIC and BIC) that can be used to assess relative model fit through model comparisons. For example, the ISG model could be compared to the MTMS model (which does not include linear traitchange factors) to examine which model results in a better fit (i.e., lower AIC or BIC value). 

In our example, a wide-format analysis of the same data and ISG model with time-invariant loadings, as well as time-invariant latent state and measurement error variances, can be conducted and yields a chi-square value of 63.81 $( d f = 7 0$ , $p = . 6 8 5 3 )$ indicating an excellent fit of the model. The loglikelihood value (–9762) is the same within slight rounding errors across the two analysis versions (wide- vs. long-format), confirming that the models are the same. 

Below are selected parameter estimates obtained in the multilevel analysis version of the ISG model: 

<table><tr><td colspan="5">MODEL RESULTS</td></tr><tr><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-TailedP-Value</td></tr><tr><td colspan="5">Within Level</td></tr><tr><td colspan="5">ZETA BY</td></tr><tr><td>Y1</td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Y2</td><td>0.417</td><td>0.104</td><td>3.994</td><td>0.000</td></tr><tr><td>Y3</td><td>0.036</td><td>0.009</td><td>3.887</td><td>0.000</td></tr><tr><td colspan="5">Variances</td></tr><tr><td>ZETA</td><td>23.805</td><td>6.287</td><td>3.787</td><td>0.000</td></tr><tr><td colspan="5">Residual Variances</td></tr><tr><td>Y1</td><td>17.141</td><td>6.027</td><td>2.844</td><td>0.004</td></tr><tr><td>Y2</td><td>20.973</td><td>1.515</td><td>13.842</td><td>0.000</td></tr><tr><td>Y3</td><td>0.230</td><td>0.014</td><td>16.783</td><td>0.000</td></tr><tr><td colspan="5">Between Level</td></tr><tr><td colspan="5">KSI11 WITH</td></tr><tr><td>KSI21</td><td>110.645</td><td>10.301</td><td>10.741</td><td>0.000</td></tr><tr><td>KSI31</td><td>10.230</td><td>1.007</td><td>10.160</td><td>0.000</td></tr><tr><td colspan="5">KSI21 WITH</td></tr><tr><td>KSI31</td><td>6.568</td><td>0.646</td><td>10.161</td><td>0.000</td></tr><tr><td colspan="5">Means</td></tr><tr><td>KSILIN1</td><td>0.703</td><td>0.406</td><td>1.731</td><td>0.083</td></tr><tr><td>KSILIN2</td><td>1.093</td><td>0.227</td><td>4.820</td><td>0.000</td></tr><tr><td>KSILIN3</td><td>0.001</td><td>0.013</td><td>0.096</td><td>0.924</td></tr><tr><td>KSI11</td><td>99.697</td><td>0.846</td><td>117.820</td><td>0.000</td></tr><tr><td>KSI21</td><td>49.881</td><td>0.552</td><td>90.438</td><td>0.000</td></tr><tr><td>KSI31</td><td>-0.001</td><td>0.059</td><td>-0.019</td><td>0.985</td></tr><tr><td colspan="5">Variances</td></tr><tr><td>KSILIN1</td><td>41.301</td><td>3.850</td><td>10.727</td><td>0.000</td></tr><tr><td>KSILIN2</td><td>10.415</td><td>1.126</td><td>9.250</td><td>0.000</td></tr><tr><td>KSILIN3</td><td>0.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>KSI11</td><td>186.146</td><td>17.233</td><td>10.801</td><td>0.000</td></tr><tr><td>KSI21</td><td>73.683</td><td>7.170</td><td>10.277</td><td>0.000</td></tr><tr><td>KSI31</td><td>0.859</td><td>0.076</td><td>11.368</td><td>0.000</td></tr></table>

We can see that at Level 1 (WITHIN), we obtain the estimated state residual factor loadings, state residual (ZETA) factor variance, and measurement error (residual) variances. At Level 2 (BETWEEN), the intercept (KSI) and linear slope (KSILIN) factor means, variances, and covariances are estimated. Only the second slope factor (KSILIN2) had a statistically significant mean (1.093, $S E =$ 

0.227, $z = 4 . 8 2$ , $p < . 0 0 1 $ ), indicating an average increase in cognitive ability with regard to the second indicator over time. The remaining two slope factor means were not significantly different from zero, showing that no average linear changes occurred with regard to Measures 1 and 3. 

The variances of the first two slope factors indicated that there was substantial variability in the steepness of individuals’ linear trajectories over time with regard to the first two measures. The third measure did not show mean changes or significant variability in linear change across time. 

# 6.3.6 Modeling Autoregressive Effects Using DSEM

# 6.3.6.1 Introduction

As I mentioned previously, autoregressive effects are very common with intensive longitudinal data because measurements are often closely spaced in time, leading to carryover effects between adjacent measurement occasions. As we saw in previous chapters, a number of longitudinal SEMs feature autoregressive and/or cross-lagged effect parameters to take direct links between adjacent measurement occasions into account. For example, the simplex model presented in Chapter 3 included autoregressive path coefficients between adjacent latent state factors, thus implying a first-order autoregressive process. 

One downside of the conventional multilevel and multilevel SEM frameworks presented so far in this chapter is that they make it difficult or even impossible to estimate autoregressive and cross-lagged effects among latent variables when employing long-format versions of the models presented in previous chapters. As a result, biased parameter estimates may be obtained in situations in which autoregressive effects are strong but are not represented in the multilevel models. For example, in the multilevel SEM version of the MTMS model presented in Section 6.3.4, consistency coefficients (trait effects) may be overestimated when autoregressive effects are present, but not included in the model. In this section, I show how autoregressive effects can be modeled in intensive longitudinal studies by employing Asparouhov et al.’s (2018) dynamic structural equation modeling (DSEM) framework. 

The DSEM framework can be understood as a multivariable, multisubject extension of time-series analysis. It allows accounting for measurement error by including latent variables. In principle, all of the models described in previous chapters can be analyzed within the DSEM framework when a researcher has data from many measurement occasions. The model specifications follow the long-format (multilevel regression and multilevel SEM) specifications that I introduced earlier in this chapter. As an additional feature, autoregressive 

effects among adjacent measured and latent time-specific variables can be included in the models, which is currently not possible within the regular multilevel and multilevel SEM modeling frameworks that use maximum likelihood (ML) estimation. Autoregressive effects within DSEM modeling can be specified as random effects, that is, as random regression coefficients that have a mean and variance parameter estimated at Level 2 (the between-person level). More detailed information regarding the DSEM framework can be found in Asparouhov et al. (2018) and Hamaker, Asparouhov, Brose, Schmiedek, and Muthén (2018). 

# 6.3.6.2 Introduction to Bayesian Analysis

The conventional multilevel regression and multilevel SEM techniques presented above typically rely on ML estimation. In contrast, the DSEM framework uses Bayesian methods, which are more flexible with regard to handling small samples and intensive longitudinal data featuring autoregressive effects. Highly accessible introductions to Bayesian methodology and its use in the context of SEM can be found in Enders (2010), Muthén and Asparouhov (2012), as well as van de Schoot et al. (2014). In this book, I only provide a brief conceptual introduction to the Bayesian approach that allows readers to understand the basic principles of the Bayesian methodology and how it is applied within the DSEM framework in Mplus. 

Bayesian analysis is often contrasted with traditional frequentist statistical analysis. Frequentist analysis views parameters as fixed entities in the population (i.e., a “true” parameter value is supposed to exist in the population) and typically relies on null hypothesis significance testing (using $p$ -values) and confidence interval estimation for sample estimates of population parameters. In contrast, Bayesian analysis does not view parameters as fixed entities that exist in the population. Rather, in Bayesian analysis, each parameter is seen as a variable with a probability distribution. One goal of Bayesian analysis is to describe each parameter’s distribution (e.g., by estimating its central tendency and variance). To accomplish this goal, Bayesian analysis employs the following three steps: 

1. Specification of a prior distribution for each parameter that is to be estimated. 

2. Use of a likelihood function to extract information from the data. 

3. Combination of prior information and likelihood into a posterior distribution for each parameter. 

In the first step of a Bayesian analysis, prior parameter distributions are specified for each parameter. The prior distributions can be very specific, somewhat specific, or completely unspecific. A specific (so-called informative) prior distribution can be defined by the user based on prior knowledge (e.g., from parameter estimates obtained from previous analyses of independent data). In this case, one speaks of informative prior distributions because the priors contain actual information about the parameter estimate and a user’s certainty about the estimate. For example, in cases in which a lot of prior information exists (e.g., based on extensive meta-analytic studies summarizing effect sizes from a large number of independent studies), a researcher may be very certain of the accuracy of the specified prior, thus giving the prior a higher weight relative to the newly collected data to be analyzed. An informative prior distribution with a high certainty about the parameter has the advantage that it can lead to narrower confidence intervals (referred to as credible or credibility intervals within the Bayesian framework) in the study at hand, thus increasing statistical power and the accuracy of parameter estimation (van de Schoot et al., 2014). 

In cases in which prior knowledge does not exist or is of questionable applicability to the study at hand, researchers can use noninformative or diffuse priors. Noninformative priors result in the empirical data (rather than prior information) driving the estimation of the parameters. In Mplus, the default is that noninformative priors are used unless a user explicitly specifies an informative prior distribution for one or more parameters in the analysis. This makes the specification of a Bayesian analysis rather easy for the user, particularly when specific prior information is not available. However, noninformative priors also lead to a higher uncertainty (wider credibility intervals) in the study at hand. 

After the prior distributions have been specified, a likelihood function is used to extract the information contained in the empirical data similar to what is done in frequentist ML estimation. In the last step, the information extracted from the empirical data is combined with the (informative or noninformative) prior distribution to obtain a so-called posterior parameter distribution for each parameter. The posterior distributions can be seen as a compromise between the prior information (reflecting previous experience from independent sources) and the data at hand. Depending on how much weight is given to the prior distribution (based on how certain a researcher is about the priors), the posterior distribution is driven more by the prior or by the current data. Taken together, the posterior distribution represents a blend between prior knowledge (if any) and current data, thus leading to an accumulation of scientific knowledge. 

The central tendency of the posterior distribution (e.g., mean or median) is often used as the Bayesian point estimate. Based on the posterior distribution, we can also determine Bayesian credibility intervals for each parameter. 

In contrast to frequentist confidence intervals, Bayesian credibility intervals indicate the probability that a parameter falls within the boundaries of the credibility interval. Bayesian parameter distributions can be examined in posterior distribution plots (e.g., in Mplus as I show later in this chapter). 

One advantage of Bayesian analysis is that it can treat problems that are very hard or impossible to address with ML estimation. For example, in the context of longitudinal SEM, Bayesian estimation can be used to estimate a variety of random effect time-series (DSEM) models that cannot currently be estimated with ML estimation. Furthermore, sample size requirements for Bayesian analysis are lower than for ML estimation. Bayesian analysis does not rely on normal distribution theory (as does ML estimation). That is, the computation of Bayesian $p$ -values and credibility intervals based on the posterior distributions does not require these distributions to be normal or symmetric. 

Bayesian modeling allows researchers to include prior information in the analysis, thus promoting the accumulation of scientific knowledge. Bayesian analysis also provides statistics whose interpretations are preferred over the interpretation of corresponding frequentist statistics by some researchers. For example, many researchers feel that Bayesian credibility intervals have a more straightforward and useful interpretation than frequentist confidence intervals. 

# 6.3.6.3 Mplus Example

As an example of a model that can be estimated within the DSEM framework, consider the single-indicator latent autoregressive (simplex) model depicted in Figure 6.5. Recall that I discussed the wide-format version of this model (see Figure 6.5A) in detail in Chapter 3. A long-format version of the simplex model (see Figure 6.5B) can be analyzed within the DSEM framework using Bayesian estimation. 

Recall that in the wide-format version presented in Chapter 3, the regression coefficients were fixed effects (i.e., they were constant across individuals). In contrast, in the DSEM simplex model version that I present here, the autoregressive intercept and slope coefficients are specified as random regression coefficients that can vary across Level-2 units (persons). In Figure 6.5B, this can be seen from the fact that small black dots are included for the regression slope (labeled $\beta _ { \cdot }$ ) and the intercept (labeled α) at Level 1. In Mplus, the random intercept $\alpha$ and slope $\beta$ are treated as latent variables whose means and variances are estimated at Level 2. Therefore, $\alpha$ and $\beta$ are italicized here to indicate that they represent variables rather than constants. In the parameterization shown in Figure 6.5B, a mean structure is not included for the latent state variables; rather, a random intercept coefficient is estimated for the measured variables. 


A


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/0cf609207094c277b85e9719e5c5fb74a1223c82b7d1456ab5a1527adc06529c.jpg)



B


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/51689e22db6a2f94b3c2eac0b517db224474f0a8af5376cbf4b3f9706a4466bc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/ba71200f789dd952cec784e741536309261f5cc95a2a271c23a0cfe24e38e30b.jpg)



FIGURE 6.5. Path diagram of a single-indicator latent autoregressive (simplex) model for one observed variable $Y _ { t }$ that is measured on four time points. $\tau =$ latent state factor; $\varepsilon =$ measurement error variable; $\beta _ { { \scriptscriptstyle 1 t } } =$ autoregressive slope coefficient. All factor loadings on the latent state factors are fixed to 1. A: Wide-format single-level confirmatory factor analysis version; B: Long-format multilevel confirmatory factor analysis version.


To illustrate the application of the DSEM simplex model, I generated artificial data for $N = 3 2$ individuals who were tested repeatedly with an intelligence measure. The number of measurement occasions per subject varied between 2 and 15 $\mathrm { \Delta } M = 5 . 6 2 5$ measurement occasions). The total number of data points (referred to as “observations” in Mplus) was 180. Below is the Mplus input file for the specification of the DSEM simplex model with random regression coefficients: 

```matlab
TITLE: Simplex model specified as a multilevel model  
within the Mplus dynamic structural equation modeling (DSEM)  
framework  
DATA: File = CH6_Simplex_new.dat;  
VARIABLE: NAMES = person Y time;  
USEVARIABLES = Y;  
CLUSTER = person;  
ANALYSIS: TYPE = TWOLEVEL RANDOM;  
ESTIMATOR = BAYES;  
PROCESSORS = 2;  
BITERATIONS = (20000);  
FBITERATIONS = 20000;  
THIN = 30;  
MODEL: %WITHIN%  
TAU by Y@1(&1);  
beta | TAU on TAU&1;  
%BETWEEN%  
Y WITH beta;  
OUTPUT: TECH1 TECH8 STANDARDIZED(CLUSTER);  
PLOT: TYPE = PLOT2; 
```

We can see that the long-format data file CH6_Simplex_NEW.dat contains three variables: person, Y, and time. In the analysis, Y is the repeatedly measured intelligence variable. The person variable serves as the cluster variable (i.e., the variable that defines the Level-2 units, here: the persons). The time variable is not needed in this analysis (but may be needed for other types of models fit to the same data and was thus included here for the sake of completeness). 

The ANALYSIS command specifies that a multilevel analysis with two levels (Level 1: time points, Level 2: persons) and random slopes (TYPE $=$ TWOLEVEL RANDOM;) is to be conducted. The present analysis with random autoregressive coefficients among latent state variables requires Bayesian techniques (ESTIMATOR $=$ BAYES;). 

When choosing ESTIMATOR $=$ BAYES, Mplus uses an iterative Markov chain Monte Carlo (MCMC) algorithm (Muthén, 2010). The Mplus default is that two Markov chains will be used in the estimation. To speed up computations, 

the two chains can be distributed across two processors of the computer (PRO-CESSORS = 2;). The default convergence criterion in Mplus uses the potential scale reduction (PSR) factor (Gelman & Rubin, 1992). The PSR value is based on a comparison of the parameter variation within each chain (across multiple iterations) to the parameter variation across chains. A PSR value close to 1 for a parameter indicates that a parameter does not show highly discrepant values across chains. 

Even though the Mplus default convergence criterion based on the PSR value may lead to proper convergence of a model, it is a good idea to check model convergence more thoroughly by requesting a larger number of MCMC iterations (longer chains), thus overriding the Mplus default convergence criterion. In our example, the Mplus default settings did not result in proper convergence as can be seen from the fact that a version of the analysis with a larger number of (user-specified) MCMC iterations leads to substantially different parameter estimates. To study convergence in detail, I ran and compared different versions of the analysis with a larger number of iterations (e.g., 1,000; 10,000; and 20,000). I then examined convergence by checking whether PSR values remained close to 1 across MCMC iterations, comparing parameter estimates across different solutions, and looking at the patterns of the MCMC chains in so-called parameter trace plots. 

For example, in the version of the analysis shown here, I specified that a minimum number of 20,000 iterations be used in each chain [BITERA-$\mathrm { T I O N S } ~ = ~ \left( 2 0 0 0 0 \right) ; ]$ $=$ and that the total number of MCMC iterations be 20,000 (FBITERATIONS = 20000;) for each chain as shown in the example input file above. This was one of the versions that appeared to result in proper parameter convergence. 

To reduce the effect of parameter autocorrelation between subsequent chain iterations (see the discussion later in this chapter), I requested thinning such that only every 30th iteration would be used in the computation of the final posterior parameter distributions (THIN = 30;). Taken together, these specifications can help facilitate and examine proper convergence and may lead to more accurate posterior parameter distributions when using Bayesian estimation. To check the trustworthiness of the results, researchers should carefully examine all of the diagnostic tools that Mplus offers (as discussed below). In addition, detailed sensitivity analyses using different settings (e.g., increasing the number of iterations, greater thinning, etc.) can help examine convergence as well as the robustness of the parameter estimates and distributions across different settings. 

In the MODEL command, the Level-1 part of the model is specified under %WITHIN%. We can see that at Level 1, the latent state factor TAU is measured 

by Y with a loading fixed at one. The (&1) specification behind the fixed loading indicates that TAU and Y are lagged variables that occur at every measurement occasion. In the next line of code (beta | TAU on TAU&1;), the random coefficient autoregressions of the latent state variables $\tau _ { t }$ on the immediately preceding latent states $( \tau _ { t - 1 } )$ are specified. The random slope of the autoregressions is labeled as beta before the | symbol. The mean, variance, and potential covariances of the random slope can then be estimated at Level 2 (the BETWEEN level). 

On the %BETWEEN% level, the means and variances of the random intercept and random slope are estimated by default. The covariance between intercept and slope has to be explicitly requested (Y WITH beta;). Using the OUTPUT command, we can request different diagnostic information as well as the standardized solution. In the TECH1 output, the parameters of the model are enumerated which is helpful later on in order to understand the information provided in the TECH8 output. The TECH8 output provides the PSR values across iterations. The PSR value can be used as a diagnostic criterion to examine model convergence. The PSR value should be close to 1 after a number of iterations and should subsequently remain stable across iterations. By increasing the number of iterations (by using the FBITERATIONS option in the ANALYSIS command), one can check whether the PSR value remains stable and close to 1 when longer MCMC chains are used. 

With TWOLEVEL models and ESTIMATOR $=$ BAYES, Mplus standardizes the parameters within each cluster [STANDARDIZED(CLUSTER)] and also provides averages of the standardized estimates across clusters. The PLOT: TYPE $=$ PLOT2; option also provides useful diagnostic information to examine the accuracy of the estimation, convergence, and parameter distributions. 

Below I first discuss some important diagnostic information provided by Mplus that can be used to evaluate model convergence as well as the stability of the parameter estimates. Subsequently, I present selected Mplus parameter estimates for the DSEM simplex model. The TECH1 output shows us how the parameters of the model were enumerated by Mplus (only selected TECH1 output is printed below): 

```csv
TECHNICAL 1 OUTPUT
PARAMETER SPECIFICATION FOR WITHIN
PSI
TAU TAU&1 Y
TAU 1
TAU&1 0 0
Y 0 0 2 
```

<table><tr><td colspan="3">PARAMETER SPECIFICATION FOR BETWEEN</td></tr><tr><td colspan="3">ALPHA</td></tr><tr><td>BETA</td><td>Y</td><td></td></tr><tr><td>3</td><td>4</td><td></td></tr><tr><td colspan="3">BETA</td></tr><tr><td>BETA</td><td>Y</td><td></td></tr><tr><td>0</td><td>0</td><td></td></tr><tr><td>Y</td><td>0</td><td>0</td></tr><tr><td colspan="3">PSI</td></tr><tr><td>BETA</td><td>Y</td><td></td></tr><tr><td>5</td><td>7</td><td rowspan="2"></td></tr><tr><td>Y</td><td>6</td></tr></table>

We can see that the following parameters were estimated by Mplus: 

# At Level 1:

•	 the TAU residual variance $V a r ( \zeta )$ $( \zeta )$ (Parameter #1) and 

•	 the Y residual variance Var(ε) (Parameter #2). 

# At Level 2:

•	 the mean of the random slope $E ( \beta )$ (Parameter #3), 

•	 the mean of the random intercept $E ( \alpha )$ (Parameter #4), 

•	 the variance of the random slope $V a r ( \beta )$ (Parameter #5), 

•	 the covariance between the random slope and the random intercept $C o v ( \beta , \alpha )$ (Parameter #6), and 

•	 the variance of the random intercept Var(α) (Parameter #7). 

The TECH8 output at the end of the Mplus output file includes a list of the PSR values for every 100th MCMC iteration. Mplus also identifies the parameter with the highest PSR value, so that potential problems with individual parameters can be more easily diagnosed. 

<table><tr><td colspan="3">TECHNICAL 8 OUTPUT FOR BAYES ESTIMATION</td></tr><tr><td rowspan="2">ITERATION</td><td>POTENTIAL</td><td>PARAMETER WITH</td></tr><tr><td>SCALE REDUCTION</td><td>HIGHEST PSR</td></tr><tr><td>100</td><td>1.150</td><td>1</td></tr><tr><td>200</td><td>1.025</td><td>1</td></tr><tr><td>300</td><td>1.014</td><td>2</td></tr><tr><td>400</td><td>1.014</td><td>5</td></tr><tr><td>500</td><td>1.001</td><td>4</td></tr><tr><td>600</td><td>1.017</td><td>1</td></tr><tr><td>700</td><td>1.002</td><td>6</td></tr><tr><td>800</td><td>1.006</td><td>5</td></tr><tr><td>900</td><td>1.004</td><td>6</td></tr><tr><td>1000</td><td>1.004</td><td>2</td></tr><tr><td>...</td><td></td><td></td></tr><tr><td>19000</td><td>1.012</td><td>5</td></tr><tr><td>19100</td><td>1.012</td><td>5</td></tr><tr><td>19200</td><td>1.012</td><td>5</td></tr><tr><td>19300</td><td>1.012</td><td>5</td></tr><tr><td>19400</td><td>1.011</td><td>5</td></tr><tr><td>19500</td><td>1.012</td><td>5</td></tr><tr><td>19600</td><td>1.012</td><td>5</td></tr><tr><td>19700</td><td>1.012</td><td>5</td></tr><tr><td>19800</td><td>1.012</td><td>5</td></tr><tr><td>19900</td><td>1.012</td><td>5</td></tr><tr><td>20000</td><td>1.012</td><td>5</td></tr></table>

We can see that the PSR measure in our example dropped to values close to 1.0 rapidly and remained consistently close to 1.0 across 20,000 iterations. This is an indication that convergence was achieved. However, other diagnostic tools that concern individual parameters should also be examined, such as parameter trace and autocorrelation plots. By clicking on Plot View plots in the Mplus output window, we can examine such plots. 

Figure 6.6 (on pages 268–269) shows two examples of parameter trace plots obtained in a version of this analysis with only 1,000 total MCMC iterations to keep the plot easier to read for didactic purposes. Mplus provides a trace plot for every single parameter of a model, and the user should inspect all of them to ensure proper convergence of all parameters. The trace plots show the parameter estimates for both chains of the MCMC algorithm (on the y-axis) across 1,000 iterations $\boldsymbol { \mathscr { x } }$ -axis). Notice that, as indicated by the vertical line in the middle of each plot, the first half of the iterations (here, the first 500 iterations) serve as the “burn-in” phase in Mplus, which is not used in the computation of the final posterior parameter distributions. The posterior parameter distribution is obtained solely from the second half of the MCMC iterations to provide for a higher stability and accuracy of the posterior distribution. 

The trace plot in Figure 6.6A shows the Bayesian parameter estimates for the mean of the random slope parameter $E ( \beta )$ and is an example of a plot that indicates proper convergence of a parameter. This can be seen from the fact that the two lines form a relatively tight horizontal band with no large discrepancies between chains at least in the post burn-in phase. 

In contrast, Figure 6.6B is an example of a trace plot that indicates convergence of the Level-1 measurement error variance Var(ε) has not been achieved after 1,000 MCMC iterations. This can be seen from the fact that there are large discrepancies between the chains even in the post burn-in phase, resulting in a posterior distribution of Var(ε) that cannot be trusted. This means that a larger number of MCMC iterations is needed in this example to achieve convergence of all parameters. Recall that for the actual analysis, I used 20,000 MCMC iterations, which appeared to result in proper convergence of all parameters including Var(ε). 

In addition to the trace plots, researchers should also examine autocorrelation plots for each parameter. Autocorrelation plots indicate the degree of dependency of the parameter estimates across MCMC iterations. Ideally, each MCMC iteration should result in independent information for the posterior distribution of a parameter (autocorrelation of zero). Figure 6.7 (on page 270) shows an example of a parameter autocorrelation plot obtained for the mean of the random $\beta$ coefficient. In the plot, the value of the autocorrelation is shown on the y-axis, and the time lag between MCMC iterations is shown on the $x$ -axis. We can see that the autocorrelation between adjacent MCMC iterations is quite high (around .3) in this example. With increasing time lag between iterations, the autocorrelation becomes smaller and is negligible for longer lags. 

When there is substantial parameter autocorrelation (e.g., autocorrelation values $>$ .10) as in this example, thinning should be applied before computing the final posterior distributions for the parameters. Recall that thinning means that not every iteration will be used in the computation of the posterior distribution but rather only every 10th iteration or so. In this way, one avoids using highly dependent information from subsequent iterations that have a small lag and may be highly correlated. Remember that, in this example, I requested that only every 30th iteration of the post-burn-in phase be used by Mplus to compute the posterior distribution (by specifying THIN $= \ 3 0$ ; in the Mplus input file). 

In addition to the trace and autocorrelation plots, Mplus provides the posterior distributions for each parameter (see Figure 6.8 on page 271 for an example). Those parameter distributions are key to the interpretation of a model in Bayesian analysis, and they need not be normal or symmetric. The central tendency of the posterior distribution (e.g., the mean or median) may be used as the Bayesian point estimate for a given parameter. 

The standard deviation (SD) of the posterior distribution can be interpreted in a similar way as a frequentist standard error. That is, the posterior SD can be used to quantify the uncertainty about a given parameter estimate. A Bayesian $p$ -value can be obtained from the distribution by computing the proportion of 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/d055caea652eeef085bccc74ed1f7cad2ab2d0ee26adf41fcba259ba7d33ab01.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/34b978ab5d97d8c231553eaf67f04c23460762d7245ccf9eef59be4894c9f205.jpg)



6.6 is available on the companion website (see the box at the end of the race plot indicating convergence problems with the Level-1 error variance para el. A: Example of a trace plot indicating proper convergence of the autoregressi mples of Mplus parameter trace plots obtained in the Bayesian analysis of the l


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/0804dbcc554f1dd0a629f0fad83abb4fbff692de8c2c836e02f52bec7f5594ad.jpg)



ble on the companion website (see the box at the end of the ta efore computing the parameter posterior distribution (see text for details. A c ) horter lags between MCMC iterations but close to zero for long lags. This indi ) p .       p lag between MCMC iterations. The plot shows that the autocorrelation of the hesimlexmodelThey-axisindicatestheamountofarameterautocorrelat mple of an Mplus parameter autocorrelation plot obtained in the Bayesian a


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/1f27c02c04dbbee9396f95cde394cc53dfe1d5f69c7e6566889f246dd4180bf2.jpg)



contents lor version of Figure 6.8 is available on the companion website (see the box at MCMC iterations along with measures of central tendency as well as the lim of the simplex model. The graph shows the posterior distribution of the β1 p ample of an Mplus posterior parameter distribution plot obtained in the Baye


estimates that is below (for a positive estimate) or above zero (for a negative estimate). In addition, credibility intervals can be computed based on the posterior distributions, which tell a researcher in which range he or she can expect the true parameter to fall with $9 5 \%$ certainty. Note that this interpretation of the credibility interval is more straightforward and useful than the interpretation of frequentist confidence intervals. 

Mplus computes the posterior distributions for each parameter based on the post-burn-in phase, that is, by using only the parameter estimates obtained from both chains of the MCMC algorithm in the second half of the MCMC iterations (minus iterations discarded through potential thinning). In our example, only the second 10,000 iterations (minus iterations deleted through thinning) were used to create the posterior distributions. 

Figure 6.8 shows the posterior distribution for the mean slope parameter $E ( \beta )$ . We can see that the distribution in this case resembles a normal distribution (this is not always the case, and it is not a requirement in Bayesian analysis), so that mean, median, and mode are almost identical (about 0.33). The posterior $S D$ is relatively large (0.18), indicating considerable uncertainty about the true parameter value. This is reflected in the wide credibility interval, which ranges from $- 0 . 0 1$ to 0.70. That is, we can expect the true autoregressive slope parameter to fall somewhere in between $- 0 . 0 1$ and 0.70, which is a large range. This is likely due to the relatively small number of data points used in this example $N = 3 2$ ; 180 total data points), resulting in large uncertainty and low statistical power. 

After careful study of convergence criteria (PSR value), trace plots, autocorrelation plots, and posterior distribution plots, it is recommended (and frequently necessary) to rerun the analysis with a larger number of MCMC iterations and/or other changes to certain settings (e.g., greater thinning) to examine the stability of the parameter distributions and estimates across different settings. When similar parameter estimates are obtained after specifying a larger number of iterations (e.g., 20,000 versus 10,000) and the PSR value stays close to 1.0, one can be relatively confident that the results are trustworthy. Below I discuss selected parameter estimates printed in the Mplus output file for the Bayesian simplex analysis: 

<table><tr><td colspan="6">MODEL RESULTS</td></tr><tr><td></td><td>Estimate</td><td>Posterior S.D.</td><td>One-Tailed P-Value</td><td>95% Lower 2.5%</td><td>C.I. Upper 2.5%</td></tr><tr><td colspan="6">Within Level</td></tr><tr><td>TAU BY</td><td>1.000</td><td>0.000</td><td>0.000</td><td>1.000</td><td>1.000</td></tr><tr><td>Y</td><td>0.999</td><td>0.991</td><td>0.000</td><td>0.033</td><td>3.426</td></tr><tr><td colspan="6">Residual Variances</td></tr><tr><td>TAU</td><td>2.692</td><td>1.142</td><td>0.000</td><td>0.196</td><td>4.390</td></tr><tr><td colspan="6">Between Level</td></tr><tr><td colspan="6">Y WITH</td></tr><tr><td>BETA</td><td>-3.184</td><td>2.832</td><td>0.086</td><td>-9.733</td><td>1.565</td></tr><tr><td colspan="6">Means</td></tr><tr><td>Y</td><td>102.840</td><td>2.282</td><td>0.000</td><td>98.289</td><td>107.347</td></tr><tr><td>BETA</td><td>0.326</td><td>0.182</td><td>0.033</td><td>-0.018</td><td>0.704</td></tr><tr><td colspan="6">Variances</td></tr><tr><td>Y</td><td>152.132</td><td>48.665</td><td>0.000</td><td>92.043</td><td>280.853</td></tr><tr><td>BETA</td><td>0.224</td><td>0.184</td><td>0.000</td><td>0.041</td><td>0.724</td></tr></table>

The default in Mplus is that the median of the posterior distribution will be printed as the Bayesian point estimate (referred to as Estimate in the Mplus output file). This default can be changed by specifying, for example, ANALY-SIS: POINT $=$ MEAN; to obtain the mean instead of the median as the point estimate in the output file. In the next column, Mplus reports the posterior SD for each parameter. Subsequently, a one-tailed $p$ -value is provided based on the posterior distribution for significance testing. Lastly, Mplus provides the $9 5 \%$ credibility interval for each parameter. 

In our example, the point estimate of the Level-2 mean slope parameter $[ E ( \beta )$ point estimate $= 0 . 3 2 6 ]$ had a one-tailed $p$ -value of .033. This means that there is only a $3 . 3 \%$ chance that the parameter value is zero or negative. However, the $9 5 \%$ credibility interval [–0.01; 0.70] included zero and was rather wide as we already saw based on the posterior distribution shown in Figure 6.8. 

The Level-2 variance of $\beta$ was considerable $\{ V a r ( \beta )$ point estimate $= 0 . 2 2 4$ , posterior $S D = 0 . 1 8 4$ , $p < . 0 0 1$ , $9 5 \%$ credibility interval $= [ 0 . 0 4 ]$ ; 0.724]}, indicating substantial variation in the autoregressive effect across participants. The Bayesian point estimate for the mean intercept $E ( \alpha )$ was 102.84 (posterior $S D =$ 2.282, $p < . 0 0 1$ , $9 5 \%$ credibility interva $= [ 9 8 . 2 8 9$ $=$ ; 107.347]). In this case, the mean intercept gives an estimate of the average IQ level in the sample. There was also substantial variation in the intercept (IQ level) as indicated by the intercept variance $\{ V a r ( \alpha )$ point estimate $= 1 5 2 . 1 3 2$ , posterior $S D = 4 8 . 6 6 5$ , $p < . 0 0 0 1$ , $9 5 \%$ credibility interval $=$ [92.043; 280.853]}. There was no significant covariance between the random intercept and slope coefficients $\{ C o \nu ( \alpha , \beta )$ point estimate $= - 3 . 1 8 4$ , posterior $S D = 2 . 8 3 2$ , $p = . 0 8 6$ , $9 5 \%$ credibility interval $=$ [–9.733; 1.565]}. Excerpts from the standardized solution are printed below: 

<table><tr><td colspan="6">STANDARDIZED MODEL RESULTS (STDYX Standardization)</td></tr><tr><td></td><td>Estimate</td><td>Posterior S.D.</td><td>One-Tailed P-Value</td><td>95% Lower 2.5%</td><td>C.I. Upper 2.5%</td></tr><tr><td colspan="6">Within-Level Standardized Estimates Averaged Over Clusters</td></tr><tr><td>TAU BY Y</td><td>0.887</td><td>0.165</td><td>0.000</td><td>0.378</td><td>0.994</td></tr><tr><td>BETA | TAU ON TAU&amp;1</td><td>0.291</td><td>0.134</td><td>0.008</td><td>0.045</td><td>0.586</td></tr><tr><td colspan="6">Between Level</td></tr><tr><td colspan="6">Y WITH</td></tr><tr><td>BETA</td><td>-0.612</td><td>0.347</td><td>0.086</td><td>-0.981</td><td>0.286</td></tr><tr><td colspan="6">Means</td></tr><tr><td colspan="6">...</td></tr><tr><td>BETA</td><td>0.693</td><td>0.650</td><td>0.033</td><td>-0.033</td><td>2.385</td></tr><tr><td colspan="6">R-SQUARE</td></tr><tr><td>Within-Level</td><td>R-Square</td><td>Averaged</td><td colspan="3">Across Clusters</td></tr><tr><td></td><td></td><td></td><td>Posterior</td><td>One-Tailed</td><td>95% C.I.</td></tr><tr><td>Variable</td><td>Estimate</td><td colspan="2">S.D.</td><td>P-Value</td><td>Lower 2.5%</td></tr><tr><td>Y</td><td>0.788</td><td colspan="2">0.231</td><td>0.000</td><td>0.173</td></tr><tr><td></td><td></td><td>Posterior</td><td>One-Tailed</td><td colspan="2">95% C.I.</td></tr><tr><td>Variable</td><td>Estimate</td><td colspan="2">S.D.</td><td>P-Value</td><td>Lower 2.5%</td></tr><tr><td>TAU</td><td>0.260</td><td colspan="2">0.084</td><td>0.000</td><td>0.107</td></tr></table>

In addition to providing standardized estimates separately for each person (“cluster”; not shown here but included in the online supplemental materials), Mplus provides Level-1 (within-person) standardized estimates that represent averages across persons as well as $R ^ { 2 }$ values that are averaged across persons. At Level 2, the between-person standardized estimates are given. 

At the within-person level, the average standardized autoregressive slope coefficient was 0.291. At the between-person level, the same standardized coefficient was 0.693. Based on the $R ^ { 2 }$ values, we can see that the average reliability of the Y variable was .788 in this example. On average, $2 6 \%$ of the variability in the latent states was explained by the autoregression ( $\cdot R ^ { 2 }$ value for $\mathrm { T A U } = . 2 6$ ). 

# 6.3.6.4 Summary

The novel DSEM approach in Mplus offers more flexibility in handling intensive longitudinal data than traditional multilevel and multilevel SEM techniques. Through the use of Bayesian analysis techniques, longitudinal models with autoregressive and/or cross-lagged effects that are computationally very intense or infeasible with ML estimation become relatively straightforward to estimate. 

The Bayesian approach can also be applied to conventional models. This may be advantageous because this approach offers a number of features that conventional frequentist ML estimation falls short of. Bayesian estimation derives parameter posterior distributions based on both previous information (i.e., by including informative priors if available) and current empirical data (e.g., through MCMC estimation methods) and does not require large-sample, normal-distribution theory as is required with ML estimation. Bayesian posterior parameter distributions need not be normal or symmetric as the computation of posterior $p$ -values or credibility intervals does not depend on a symmetric distribution (as does the computation of ML confidence intervals). Bayesian 

$p$ -values and credibility intervals also have a more straightforward and intuitive interpretation compared to their frequentist counterparts. 

In addition, Bayesian techniques appear to work with smaller samples than ML. However, the exact conditions under which it performs accurately still need to be studied in detail for many models (e.g., by using Monte Carlo simulations). In addition, despite its advantages, Bayesian analysis also comes with some complications that researchers need to be aware of. 

First, researchers may be uncertain about how to properly specify informative prior distributions for some or all parameters to be estimated. Even though relatively straightforward in Mplus, researchers may not know which values to choose. Informative priors can also have a large influence of the results. Researchers using informative priors should provide careful documentation and justification for their choice of priors and conduct sensitivity analyses to study the impact of different priors. In cases in which a researcher does not have access to informative priors or simply wants to estimate a model that is not feasible with ML estimation, he or she can rely on noninformative priors (as shown in this chapter), which are the default in Mplus. 

Another complication of Bayesian analysis is that the accuracy of the results (posterior parameter distributions) depends to a larger degree on subjective choices to be made by the investigator than is the case with ML estimation. That is, with ML estimation, it is usually fairly obvious whether proper convergence of a model has been achieved and default settings and criteria (e.g., in Mplus) are often sufficient to obtain trustworthy results. In contrast, with Bayesian estimation, it is more difficult for the researcher to know whether or not a model has properly converged, and the Mplus default settings may not be sufficient to obtain proper convergence (as was the case in the example presented above). 

A researcher needs to carefully check whether proper convergence has been achieved for each parameter by examining convergence criteria, parameter autocorrelations, trace plots, and posterior distributions. On the positive side, Mplus makes it relatively convenient for the user to study convergence based on readily available graphics, listings of PSR values, etc. On the negative side, it remains up to the user to understand and make proper use of the diagnostics—and it takes more work than with conventional SEM modeling. Assessing parameter convergence in Bayesian analysis is also a highly subjective endeavor (i.e., studying the pattern of MCMC chains in trace plots and deciding whether or not the chains are sufficiently congruent with one another). Thinning based on autocorrelation plots also involves subjective decisions to be made by the researcher. 

Lastly, the DSEM approach and its implementation in Mplus are relatively new, and not all aspects of the modeling have yet been studied in great detail using simulation work and the like. Careful study of the performance of the 

Bayesian DSEM approach under various conditions is an important task for future research. 

# 6.4 CHAPTER SUMMARY

In this chapter, I described approaches for analyzing longitudinal structural equation models for intensive longitudinal data. I showed that such data are often most conveniently analyzed in long format by means of multilevel modeling techniques. Long-format, multilevel modeling has the advantage that it deals with imbalanced time points and missing observations in a much more convenient and efficient way than wide-format, single-level SEM analysis. As I showed in this chapter, the multilevel approach can be applied to both singleand multiple-indicator data. Even though well suited for intensive longitudinal data in principle, the multilevel approach also has some disadvantages that researchers should consider. 

Maybe the most important limitation of the multilevel approach is that stringent tests of absolute model fit (such as the chi-square test available for single-level SEM models) are nonexistent for some model versions (i.e., models with random slope coefficients as presented in this chapter). For other models such as the random intercept and MTMS models, tests of model fit are available but are limited in scope given that the multilevel versions of the models have fewer df compared to their counterparts for wide-format data. Taken together, this means that some or all aspects of longitudinal models remain untested within the multilevel framework. More specifically, many multilevel models implicitly assume the invariance of measurement error and other variances across time without allowing researchers to test this assumption based on the empirical data. If invariance assumptions are violated, this may result in biased parameter estimates in the multilevel versions of the models. In contrast, in the wide-format SEM approach to multiple-indicator data presented in Chapters 4 and 5, most invariance assumptions can be formally tested (e.g., by examining chi-square or chi-square difference tests). 

Despite these limitations, the multilevel approach is often the only feasible approach to studying intensive longitudinal data. This is because with a large number of measurement occasions, a continuous time metric, and many missing observations, a wide-format, single-level SEM analysis is not practical and sometimes even impossible to conduct. To circumvent the potential drawbacks of untestable model assumptions that may lead to bias in multilevel analyses of longitudinal data, researchers should carefully study their data, for example, by visually examining individual trajectories and analyzing parts of 

the data with wide-format SEM techniques (if possible). By using wide-format SEM techniques on partial data and examining model fit statistics, researchers can get a sense of whether the stringent invariance assumptions implied by many multilevel longitudinal models are at least approximately met in the data to be analyzed. 

Some multilevel longitudinal models currently require Bayesian estimation techniques (i.e., models that include autoregressive or cross-lagged path coefficients). In Mplus, such techniques are available as part of the DSEM framework. Bayesian techniques are well-established in general statistics but are a relatively novel approach to parameter estimation in the field of SEM. Not all social science researchers may feel comfortable applying Bayesian techniques, as they may not be familiar with them. It is indeed true that the Bayesian approach to SEM requires the researcher to pay a lot more attention to details in estimation— details that are fairly automated with ML estimation. In addition, a larger degree of subjectivity is involved in Bayesian analysis (e.g., when specifying priors or assessing convergence). 

On the other hand, the Bayesian approach offers many advantages over frequentist ML estimation, such as the potential use of smaller samples, the absence of distributional assumptions, and the possibility of examining $p$ -values and credibility intervals that have a more intuitive and straightforward interpretation. Moreover, many models to date are not feasible with ML estimation and can only be estimated using the Bayesian framework. 

# 6.5 RECOMMENDED READINGS



Asparouhov, T., Hamaker, E. L., & Muthén, B. (2018). Dynamic structural equation models. Structural Equation Modeling, 25, 359–388. 





Eid, M., Courvoisier, D. S., & Lischetzke, T. (2012). Structural equation modeling of ambulatory assessment data. In M. R. Mehl & T. S. Connor (Eds.), Handbook of research methods for studying daily life (pp. 384–406). New York: Guilford Press. 





Geiser, C., Bishop, J., Lockhart, G., Shiffman, S., & Grenard, J. (2013). Analyzing latent state–trait and multiple-­ indicator latent growth curve models as multilevel structural equation models. Frontiers in Psychology: Quantitative Psychology and Measurement, 4, 975. 





Hamaker, E. L., Asparouhov, T., Brose, A., Schmiedek, F., & Muthén, B. (2018). At the frontiers of modeling intensive longitudinal data: Dynamic structural equa‑ tion models for the affective measurements from the COGITO study. Multivariate Behavioral Research, 53, 820–841. 





Heck, R. H., & Thomas, S. L. (2015). An introduction to multilevel modeling techniques: MLM and SEM approaches using Mplus (3rd ed.). New York: Routledge. 





Muthén, B., & Asparouhov, T. (2012). Bayesian structural equation modeling: A more flexible representation of substantive theory. Psychological Methods, 17, 313– 335. 





van de Schoot, R., Kaplan, D., Denissen, J., Asendorpf, J. B., Neyer, F. J., & van Aken, M. A. G. (2014). A gentle introduction to Bayesian analysis: Applications to developmental research. Child Development, 85, 842–860. 



# Missing Data Handling

# 7.1 INTRODUCTION

Missing scores are very common in longitudinal studies, in which participants may drop out over time or new participants may join the study at later time points. On the negative side, missing data are a threat to quantitative empirical studies. When improperly handled (e.g., by using listwise or pairwise deletion), missing data can lead to a large reduction in the sample size and/or biased parameter estimates. Even when properly treated, missing scores can lead to a reduction in statistical power. As a consequence of reduced power, a researcher may not be able to detect effects that actually exist in the population under study (e.g., true changes over time in a construct or a true cross-lagged effect between two constructs). In the worst case, a researcher may not only lose statistical power, but also obtain biased parameter estimates due to missing data. Parameter bias can result from certain types of missing data (e.g. from “missing not at random” data) or when researchers use ad hoc methods for handling missing data (e.g., listwise deletion) with other, more benign missing data mechanisms such as “missing at random” data. 

On the positive side, modern missing data handling methods such as maximum likelihood estimation and multiple imputation when properly applied can help researchers retain a significant amount of statistical power and avoid bias in the presence of missing data (Enders, 2010). Contemporary software packages 

(e.g., Mplus) make the proper analysis and handling of missing data rather easy for the user—particularly the use of maximum likelihood estimation with missing data. As a consequence, researchers no longer have to use more ad hoc and statistically less appropriate methods such as listwise or pairwise deletion. 

In addition, so-called planned missing data designs in which missing scores are part of the a priori measurement design can facilitate longitudinal studies as they help save considerable time and expenses (Graham, Taylor, Olchowski, & Cumsille, 2006). As I explain in Section 7.4, in planned missing data designs, not every variable has to be collected from every participant, reducing the complexity and costs of a study, while retaining maximum statistical power. 

In the next section, I briefly review the key theoretical missing data mechanisms introduced by Rubin (1976); these mechanisms are key to understanding the proper handling of missing data. Subsequently, I show how missing data can be properly addressed by using maximum likelihood estimation or multiple imputation in Mplus. In my review, I emphasize missing data in the context of longitudinal data analysis. Later on, I provide a brief introduction to planned missing data designs, which can be very useful in longitudinal studies to reduce costs and the burden on investigators and participants. I demonstrate how the power of planned missing data designs can be examined in Mplus by means of a Monte Carlo simulation study. 

My discussion of missing data in this book is rather brief and conceptual in nature and focuses on the practical application in Mplus. A number of excellent and much more detailed resources on missing data theory and modeling exist. The books by Enders (2010) and Little and Rubin (2002), as well as work by Schafer and Graham (2002), provide detailed, specific information regarding missing data analysis, much of which applies to both cross-sectional and longitudinal data. Readers are encouraged to consult the specialized missing data literature for more general, detailed, and/or more technical information on missing data theory and analysis. 

# 7.2 MISSING DATA MECHANISMS

Rubin (1976) distinguished between different causes of missing data that are widely referred to as missing data mechanisms. According to Rubin, missing data can be missing completely at random, missing at random, or missing not at random. These three types of missing data are key for the understanding and proper treatment of missingness in practical statistical applications and are described in detail below. 

# 7.2.1 Missing Completely at Random

The most benign missing data mechanism is referred to as missing completely at random (MCAR). With MCAR, missingness is essentially irrelevant to study outcomes except that it will lead to a loss of statistical power. This is because with MCAR, missingness is completely unrelated to the variables of interest in the study. That is, missingness is not caused by or correlated with either the exogenous (independent, X) or endogenous (outcome, Y) variables to be studied in a researcher’s statistical analysis. 

As an example, consider a longitudinal study on the relationship between memory functioning $( X )$ and subjective well-being (Y). Imagine a researcher’s hypothesis is that a decline in memory function will subsequently lead to reduced subjective well-being (SWB; i.e., people becoming unhappy due to their impaired memory). To test this hypothesis, the researcher uses a longitudinal design in which both IQ and SWB are measured on two time points. He may use the simple measured-variable autoregressive/cross-lagged path model depicted in Figure 7.1 to find out whether memory test scores significantly predict subsequent SWB scores above and beyond any autoregressive effect. 

Imagine that in his or her study, the researcher loses data on some participants due to a computer crash, leading to missing memory scores for some participants at Time 1. Importantly, this technical mishap is completely unrelated to individuals’ memory and SWB scores and thus produces missing scores that are MCAR. As a consequence of this type of missing data, the researcher may lose a small or large amount of statistical power (depending on how many data 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/e02b219be52aaece7a0c6fa79ea22041cda699e2aa12f03c170456ca19ea8a0a.jpg)



FIGURE 7.1. Path diagram of an observed variable autoregressive/cross-lagged (ACL) model for two constructs $( c = 1$ , memory performance; $c = 2$ , subjective well-being [SWB]) measured on two time points $t = 1$ , 2. $\beta _ { 1 c t } =$ constant autoregressive slope coefficient; $\beta _ { 2 c t } =$ constant cross-lagged regression slope coefficient; $e _ { c t } =$ residual variable. For simplicity, the mean structure is not shown in the figure.


points were lost). In the worst-case scenario, this loss of power may lead to a Type-II error (nonsignificant cross-lagged effect from memory ability at Time 1 to SWB at Time 2, even though the effect is nonzero in the population). 

However, the estimated effect (point estimate of the path coefficient) as such will be unbiased (as long as there is sufficient data to properly estimate the statistical model of interest) because the data are MCAR. The remaining (nonmissing) data points under MCAR can be seen as a representative sample of what the full data would have looked like had there not been any missing scores. In other words, statistically, the cases with complete data are no different from the cases with missing data, and therefore, the estimation of the path coefficients remains unbiased. The MCAR condition can be formally tested, and several statistical tests are available for this purpose (for a detailed discussion, see Enders, 2010). 

# 7.2.2 Missing at Random

The missing at random (MAR) mechanism frequently causes confusion among researchers, as it seems to imply that missing scores are missing in a completely unsystematic fashion—as is the case with the MCAR mechanism described in the previous section. However, in contrast to MCAR, MAR means that missingness in an outcome Y is related to one or more variables that are part of a researcher’s data set (but not to Y itself). As an example, consider the memory $( X )$ and SWB (Y) example once again. Assume that individuals who have low memory $( X )$ scores at the first measurement occasion do not return at Time 2 because they do not remember their appointment. Therefore, memory and SWB (Y) scores at Time 2 are missing for participants with low Time-1 memory functioning. 

Further assume that low memory performance at Time 1 is the only reason for missing SWB scores at Time 2 (i.e., participants are not missing because their SWB scores at Time 2 are low). Given that the researcher has access to memory performance data from the participants at Time 1 $( X )$ , he is able to take this information regarding missingness in SWB at Time 2 into account. Statistically, MAR implies that there is no residual relationship between the outcome Y (SWB at Time 2) and missingness after controlling for (or “partialing out”) X (Time-1 memory performance). 

The MAR mechanism is often viewed as a benign (“ignorable”) missing data mechanism. This is because, with proper estimation methods (e.g., maximum likelihood or multiple imputation), MAR does not lead to bias in parameter estimates as long as all relevant variables related to missingness are included in the statistical model. In the example above, this would be the case because the 

researcher has access to all participants’ Time-1 memory scores—which in the example are the sole cause of missing data at Time 2. In this example, the key exogenous $( X )$ variable in the model is also the variable that explains missing Y scores at Time 2. 

Therefore, with proper missing data estimation techniques (e.g., maximum likelihood), the model will automatically include the necessary adjustments, and there will be no bias due to missingness (again, provided that enough data points are available for the proper estimation of the given statistical model). Longitudinal designs in general have the advantage that dropout over time is frequently related to the previously measured scores on the relevant study variables. Therefore, longitudinal data often make it more likely that missingness is in line with the MAR mechanism. 

In some cases, variables explaining missingness may not be included in the set of exogenous $( X )$ variables that are part of a researcher’s statistical model, but they may still be part of a researcher’s data set. For example, demographic variables (such as age) or health-related variables may explain why individuals quit a longitudinal study. Variables that are not part of a researcher’s model, but carry information on missing data, are referred to as auxiliary variables. Including auxiliary variables in a statistical analysis is key to proper handling of missing data. This is because auxiliary variables allow a researcher to approximate the MAR condition, thus reducing bias and improving statistical power in the analysis (Enders, 2010). As I show below, auxiliary variables can easily be incorporated into a longitudinal analysis in Mplus. 

The MAR condition is an assumption that cannot be tested or proven to hold in a given empirical application. The reason is that although certain available exogenous or auxiliary variables may be correlated with missingness, there are usually other, additional (systematic or unsystematic) reasons for missingness that remain unclear. Usually, the best that a researcher can hope for is that either the MCAR mechanism holds or that the MAR mechanism can be approximated to a reasonable degree (e.g., by including as many relevant auxiliary variables as possible), so that bias in parameter estimates will be minimal. Using missing data handling techniques that require the MAR assumption (such as maximum likelihood estimation) is still preferred in practice to other ad hoc techniques such as listwise deletion because these other techniques tend to require the even stricter MCAR mechanism to be in place (Enders, 2010). 

# 7.2.3 Missing Not at Random

The missing not at random (MNAR) mechanism is the most problematic missing data mechanism. With MNAR data, missingness is related to the outcome 

variable Y itself. Consider the above example again, in which a researcher studies the longitudinal relationship between memory at Time 1 and SWB at Time 2. Imagine that participants do not show up at the second measurement occasion because they feel depressed (have low SWB scores at Time 2). In this scenario, missingness is due to the outcome variable Y (SWB) itself. Why is this problematic? 

Recall that in the MAR example presented above, the scores at Time 2 were missing because of low memory performance at Time 1 as recorded by the researcher. Given the availability of the Time-1 memory scores, the researcher was able to find out why certain participants’ SWB scores at Time 2 were missing. Furthermore, the researcher was able to include the Time-1 memory scores from all participants into the statistical analysis, thus establishing MAR and avoiding bias in the estimation of the cross-lagged effect from Time-1 memory to Time-2 SWB. 

In contrast, in the present MNAR example, the researcher has no way of knowing why certain Time-2 SWB scores are missing. Missingness in this example is not due to low memory scores or low SWB scores at Time 1, which are available to the researcher, but rather to low SWB scores at Time 2—which are the very scores that are not available. As a result, even by including the Time-1 memory and SWB scores into the statistical model, the researcher will not be able to obtain MAR data. 

The key problem in the present scenario (and with MNAR in general) is that missingness is related to the outcome (endogenous) variable itself. This is problematic because the researcher does not have the relevant information about why the participants have missing scores. As a consequence, the researcher cannot properly account for missingness and make adjustments using auxiliary variables, as was possible in the previous (MAR) example. The result may be bias in the estimation of the relevant cross-lagged effect. 

Notice that the researcher in the above example may be able to turn his or her unfortunate MNAR situation into a more desirable MAR situation by going back and trying to find out why participants dropped out. For example, the researcher may try to contact the relevant participants or their spouses and ask them why they missed the second measurement occasion. This information could then be added to the data set in terms of auxiliary variables to approximate the MAR condition. Of course, it is usually difficult to realize this strategy in practice. As with MAR, the MNAR condition cannot be empirically tested. 

Two missing data handling methods are currently viewed as state of the art in estimating structural equation models (and many other types of statistical analyses): maximum likelihood (ML) estimation and multiple imputation 

(MI; Enders, 2010). Statistically, ML and MI are equivalent procedures. Therefore, under general conditions and when applied correctly, ML and MI lead to very similar results in practice. In the following section, I provide a conceptual review of ML estimation with missing data and show how it is implemented in the Mplus software. In Section 7.4, I deal with MI in Mplus. For more insights and an in-depth technical presentation of both ML and MI, I refer the reader to the specialized missing data literature, specifically to Enders’s (2010) book. In Section 7.5, I show how researchers can conduct power analyses for planned missing data designs in Mplus using the program’s Monte Carlo simulation features. 

# 7.3 ML MISSING DATA HANDLING

# 7.3.1 Introduction

ML estimation is the standard estimation method used for most structural equation modeling approaches, including the longitudinal models that I presented in the previous chapters. Fortunately, ML is not only suitable to obtain the parameter estimates and fit statistics with complete data. ML can also handle missing data. When used with missing data, ML estimation is often referred to as full information maximum likelihood (FIML) estimation to emphasize that this estimation procedure makes use of the entire set of available data, including participants with missing scores. 

Conceptually, when missing scores are present, ML estimation improves the accuracy of parameter estimates by borrowing information from the variables for which scores are available (Enders, 2010). Therefore, ML estimation performs better than traditional missing data handling techniques such as listwise deletion, which do not take such information into account. Specifically, ML estimation provides unbiased parameter estimates under MCAR and MAR, whereas listwise deletion produces biased results under MAR. Even for MCAR data, ML estimation is advantageous because it provides more statistical power than, for example, listwise deletion. When data are MNAR, ML estimates can be biased; however, traditional methods tend to perform no better in this case (Enders, 2010). Another advantage of ML estimation is that it provides correct standard errors under MAR and MCAR that take into account the additional uncertainty about the true parameter values due to missingness. ML estimation with missing data is very convenient, as the researcher does not need to fill in (or “impute”) missing values. (I deal with multiple imputation in Section 7.4.) Instead, ML simply uses all the available data to estimate the parameters of a given model. 

# 7.3.2 ML Missing Data Analysis in Mplus

Mplus makes the handling of and analysis with missing data very convenient for the user. Both ML estimation with missing data and MI are available in the program. ML estimation is the default option in Mplus when only continuous (metrical) outcome (e.g., indicator) variables are used in the analysis. ML estimation is a straightforward option for handling missing data that is suitable for most empirical applications with continuous observed variables, including the models described in this book. 

To illustrate ML estimation with missing data in Mplus, I generated artificial data $\left( N = 3 0 0 \right)$ ) for the previously discussed memory and SWB example based on a two-wave, two-variable autoregressive/cross-lagged (ACL) path model (see Figure 7.1). The simulated data conform to an MAR mechanism such that missingness is related to an external (auxiliary) variable (labeled Z in the Mplus example). The variable Z predicts attrition and is also correlated with the outcome variables at Time 2 (Memory and $S W B _ { 2 } \mathrm { , }$ . For example, one could think of Z as representing age or some other time-invariant variable. Below is the Mplus input file for specification of the ACL model with missing data and ML estimation based on the four variables that are of substantive interest (Memory1, Memory2, $S W B _ { 1 }$ , and $S W B _ { 2 } ^ { ' }$ ): 

```txt
TITLE: 2-wave autoregressive/cross-lagged model with missing data (Figure 7.1). Missing data are MAR and depend on external variable Z.  
Full information maximum likelihood estimation with missing data and auxiliary variable Z is used.  
DATA: FILE = CH7_ACL_corr_z.dat;  
VARIABLE: NAMES = memory2 SWB2 Z memory1 SWB1;  
    MISSING = ALL(999);  
    AUXILIARY(m) = Z;  
MODEL:  
    memory1 SWB1;  
    [memory1 SWB1];  
    memory1 with SWB1;  
    memory2 on memory1 SWB1;  
    SWB2 on memory1 SWB1;  
    memory2 with SWB2;  
OUTPUT: SAMPSTAT STDYX PATTERNS; 
```

In the present data set, missing scores were coded as “999.” In order to properly apply ML estimation with missing data, this numeric missing value code needs to be mentioned in the VARIABLE command. This is done by using the MISSING subcommand. Otherwise, Mplus would not recognize the “999” scores in the data set as missing values and would treat them as if they represented 

valid scores. Here, missing values were coded with the same numeric code (999) for all variables. Therefore, I specified MISSING $=$ ALL(999);. 1 

Notice that the auxiliary variable Z that is related to missingness is only listed as an AUXILIARY variable in the VARIABLE command but does not appear in the MODEL command. The AUXILIARY $\begin{array} { r l r } { \left( \mathrm { m } \right) } & { { } = } & { \mathrm { Z } . } \end{array}$ ; subcommand means that Z is used as a “background” variable to account for missing data without altering that part of the statistical model that is of substantive interest. Specifically, when using the AUXILIARY (m) subcommand, Mplus will correlate Z with all exogenous and all residual $( e _ { c t } )$ variables in the model in line with Graham’s (2003) saturated correlates approach to including auxiliary variables in regression, path, and structural equation models (see Enders, 2010, for details). This approach allows researchers to take the information about missingness contained in auxiliary variables into account without changing the substantive interpretation of the statistical model. 

The AUXILIARY (m) option can be seen as a convenience feature in Mplus; without this option, a researcher would have to explicitly include Z in the model and specify the correlations between Z and all exogenous as well as all residual variables. This procedure would be tedious, especially for more complex models with many variables. The ACL model as such is specified in the usual way using the MODEL statement. 

In the OUTPUT command, I requested that information on the missing data patterns (PATTERNS) be printed in the Mplus output file in addition to sample statistics (SAMPSTAT) and the standardized solution (STDYX). Below, I discuss output excerpts that highlight the main features of an ML analysis with missing data in Mplus. The first part of the Mplus output contains information on the number, types, and frequency of missing data patterns that were observed in the data set: 

SUMMARY OF DATA Number of missing data patterns 4   
SUMMARY OF MISSING DATA PATTERNS MISSING DATA PATTERNS $(\mathbf{x} =$ not missing) 1234   
MEMORY2 x x   
SWB2 x x   
MEMORY1 x x x x   
SWB1 x x x x   
 MISSING DATA PATTERN FREQUENCIES   
Pattern Frequency Pattern Frequency Pattern Frequency 1 145 3 36 2 28 4 91 

We can see that four different missing data patterns occurred in the data set. Pattern 1 was the complete data pattern (data on all four variables is present in this pattern). Pattern 2 had data on all variables except SWB2. Pattern 3 had data on all variables except MEMORY2. Pattern 4 had missing data on both SWB2 and MEMORY2 but no missing scores on either one of the Time-1 variables SWB1 and MEMORY1. 

The frequency of each missing data pattern is given next. We can see that the complete data pattern (Pattern 1) was the most frequent one $n = 1 4 5$ ; $4 8 . 3 \%$ . The next most frequent pattern was the one in which both Time-2 scores (i.e., SWB2 and memory2) were missing (Pattern 4; $n = 9 1$ ; $3 0 . 3 \%$ ). The third most frequent pattern was Pattern 3 $n = 3 6$ ; $1 2 \%$ ), and the least frequent pattern was Pattern 2 ${ \mathrm { \Delta } n = 2 8 }$ ; $9 . 3 \%$ ). In summary, slightly more than half of the $N = 3 0 0$ participants had one or two missing scores. Missingness in this example concerned the Time-2, but not the Time-1, variables. Next, Mplus provides information on the so-called covariance coverage: 

<table><tr><td colspan="5">COVARIANCE COVERAGE OF DATA
Minimum covariance coverage value 0.100
PROPORTION OF DATA PRESENT
Covariance Coverage</td></tr><tr><td></td><td>MEMORY2</td><td>SWB2</td><td>MEMORY1</td><td>SWB1</td></tr><tr><td>MEMORY2</td><td>0.577</td><td></td><td></td><td></td></tr><tr><td>SWB2</td><td>0.483</td><td>0.603</td><td></td><td></td></tr><tr><td>MEMORY1</td><td>0.577</td><td>0.603</td><td>1.000</td><td></td></tr><tr><td>SWB1</td><td>0.577</td><td>0.603</td><td>1.000</td><td>1.000</td></tr></table>

The covariance coverage should not be confused with the actual covariances (which are provided as part of the SAMPLE STATISTICS / ESTIMATED SAMPLE STATISTICS portion of the output). For each variance and covariance, the covariance coverage matrix gives the proportion of data that provided information (available data) to estimate this variance or covariance. For example, for the MEMORY2 variance, the proportion was .577. This means that $5 7 . 7 \%$ of participants provided information on this variance (i.e., Pattern $1 +$ Pattern 2 $= 4 8 . 3 \% + 9 . 3 \% = 5 7 . 6 \%$ ; note that there is a small rounding error). As another example, for the covariance between MEMORY1 and SWB1, the covariance coverage was 1.0 $1 0 0 \% )$ . This is because all $N = 3 0 0$ participants provided data on these two variables (i.e., there was not a missing data pattern in which either MEMORY1 or SWB1 had a missing score). The lowest covariance coverage value $( 4 8 . 3 \% )$ was observed for the covariance between MEMORY2 and SWB2. This is because only individuals with Pattern 1 (complete data) provided information 

on both of these variables. All other missing data patterns included missing data on either MEMORY2, SWB2, or both. 

The covariance coverage information is useful in determining which variances or covariances were particularly affected by missing data (i.e., we can investigate which variance or covariance coverage was particularly high or low). The Mplus default (which can be changed) is that the analysis will be conducted unless covariance coverage falls below $1 0 \%$ for one or more (co)variances. In the present example, no covariance coverage value fell below this threshold, and so our model was estimated by Mplus. The standardized parameter estimates are given below: 

<table><tr><td>STANDARDIZED MODEL</td><td>RESULTS (STDYX</td><td colspan="3">Standardization)</td></tr><tr><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-TailedP-Value</td></tr><tr><td>MEMORY2 ON</td><td></td><td></td><td></td><td></td></tr><tr><td>MEMORY1</td><td>0.800</td><td>0.032</td><td>25.172</td><td>0.000</td></tr><tr><td>SWB1</td><td>0.007</td><td>0.047</td><td>0.152</td><td>0.880</td></tr><tr><td>SWB2 ON</td><td></td><td></td><td></td><td></td></tr><tr><td>MEMORY1</td><td>0.309</td><td>0.061</td><td>5.080</td><td>0.000</td></tr><tr><td>SWB1</td><td>0.453</td><td>0.056</td><td>8.098</td><td>0.000</td></tr><tr><td>MEMORY1 WITH SWB1</td><td>0.347</td><td>0.051</td><td>6.830</td><td>0.000</td></tr><tr><td>MEMORY2 WITH SWB2</td><td>0.184</td><td>0.085</td><td>2.159</td><td>0.031</td></tr><tr><td>Means</td><td></td><td></td><td></td><td></td></tr><tr><td>MEMORY1</td><td>0.027</td><td>0.058</td><td>0.471</td><td>0.638</td></tr><tr><td>SWB1</td><td>0.073</td><td>0.058</td><td>1.264</td><td>0.206</td></tr><tr><td>Intercepts</td><td></td><td></td><td></td><td></td></tr><tr><td>MEMORY2</td><td>0.080</td><td>0.055</td><td>1.454</td><td>0.146</td></tr><tr><td>SWB2</td><td>0.141</td><td>0.066</td><td>2.120</td><td>0.034</td></tr><tr><td>Variances</td><td></td><td></td><td></td><td></td></tr><tr><td>MEMORY1</td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>SWB1</td><td>1.000</td><td>0.000</td><td>999.000</td><td>999.000</td></tr><tr><td>Residual Variances</td><td></td><td></td><td></td><td></td></tr><tr><td>MEMORY2</td><td>0.356</td><td>0.043</td><td>8.334</td><td>0.000</td></tr><tr><td>SWB2</td><td>0.602</td><td>0.054</td><td>11.246</td><td>0.000</td></tr><tr><td>R-SQUARE</td><td></td><td></td><td></td><td></td></tr><tr><td>Observed</td><td></td><td></td><td></td><td>Two-Tailed</td></tr><tr><td>Variable</td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>P-Value</td></tr><tr><td>MEMORY2</td><td>0.644</td><td>0.043</td><td>15.058</td><td>0.000</td></tr><tr><td>SWB2</td><td>0.398</td><td>0.054</td><td>7.427</td><td>0.000</td></tr></table>

We can see that the parameter estimates are printed in the same way as they would be for a complete-data analysis without missing data. In this example, there are significant autoregressive effects for both constructs. In addition, 

the cross-lagged effect from MEMORY1 to SWB2 is positive and statistically significant and indicates that higher memory performance at Time 1 is associated with higher subjective well-being at Time 2 above and beyond the autoregressive effect of subjective well-being on itself. In contrast, the cross-lagged effect from SWB1 to Memory2 is very small and not statistically significant. Note that the auxiliary variable Z does not appear in the MODEL RESULTS, as it is not of substantive interest. 

# 7.3.3 Summary

ML missing data handling is a convenient method that allows users to make use of all available data without having to replace missing scores. Because of its convenience and appropriate performance with MAR data, ML estimation with missing data is the default setting in the Mplus software. It is usually the option of choice when researchers analyze longitudinal data with continuous variables. Below I show an alternative option that allows researchers to impute missing scores based on multiple data sets. 

# 7.4 MULTIPLE IMPUTATION

# 7.4.1 Introduction

ML estimation as shown above does not replace missing scores in the data set. Instead, it simply uses all available information in the existing data to estimate the parameters of a statistical model properly. Under certain circumstances, imputing missing scores is desired by the user or is necessary to handle missing data properly. For example, when data are missing at the item level, a researcher may wish to impute missing item scores before creating scale (sum) scores to be used in a statistical model. Likewise, when ordinal variables are used as indicators of latent variables, multiple imputation (MI; Rubin, 1987) has an advantage over ML (Enders, 2010). 

With MI, a number of complete data sets are generated in the first step of the analysis. That is, missing values are filled in (imputed) by a computer program, thereby taking into account auxiliary variable information (see Section 7.2.2) —similar to what is done in ML estimation. To increase the accuracy and efficiency of the estimates as well as statistical power, multiple imputed data sets (say 50) are produced—hence the term multiple imputation. 

In the second step of an MI analysis, the statistical model(s) of interest are fit to each imputed data set. The parameter estimates typically vary at least 

slightly across imputed data sets. Therefore, the estimates are averaged (pooled) across imputed data sets to obtain a final set of estimates. For detailed technical presentations of MI, see Enders (2010) or Rubin (1987). For details on the use of MI in Mplus, see Asparouhov and Muthén (2010). 

# 7.4.2 MI in Mplus

Mplus allows users to generate a desired number of imputed data sets in the first step of the analysis, thereby taking potential auxiliary variables into account. It is recommended that the number of imputed data sets be sufficiently large. For example, Enders (2010) recommended a minimum number of 20 imputations and preferably more. With modern computers, it is usually not a problem to generate and analyze 50 or more imputed data sets, and doing so can increase statistical power under certain conditions. 

In the second step, all imputed data sets are analyzed by Mplus using the statistical model of choice, and the parameter estimates are pooled across the data sets. The model fitting and pooling of estimates across multiple imputed data sets are automated in Mplus (i.e., only a single input file is needed to fit the model to all data sets and obtain a final set of pooled estimates), making the procedure very convenient for the user. 

Recall that for the illustration of ML estimation with missing data in Section 7.3, I generated artificial data $\left( N = 3 0 0 \right)$ ) for the previously discussed memory and SWB example based on a two-wave, two-variable autoregressive/crosslagged (ACL) path model (see Figure 7.1). The simulated data are in line with an MAR mechanism such that missingness is related to an external (auxiliary) variable (labeled Z in the Mplus example). The variable Z predicts attrition and is also correlated with the outcome variables at Time 2 $( M e m o r y _ { 2 }$ and $S W B _ { 2 } \mathrm { . }$ ). Here I use the same data example and model as in Section 7.3, so that the ML and MI results can be directly compared. Below is the Step-1 Mplus input file that is used to generate 50 imputed data sets: 

```txt
TITLE: Multiple imputation example  
Step 1: Imputation phase  
Generate 50 imputed data sets, thereby taking auxiliary variable Z into account  
DATA: FILE = CH7_ACL_corr_z.dat;  
VARIABLE: NAMES = memory2 SWB2 Z memory1 SWB1; USEVAR = memory2 SWB2 Z memory1 SWB1; MISSING = all(999); 
```

```txt
DATA IMPUTATION:  
    IMPUTE = memory2 SWB2;  
    NDATASETS = 50;  
    SAVE = CH7_ACL_IMPUTED*.dat;  
ANALYSIS: TYPE = BASIC;  
OUTPUT: TECH8; 
```

We can see that the same data file with missing scores (CH7_ACL_ corr_z.dat) as in Section 7.3 is used here. The DATA IMPUTATION subcommand serves to define which variables have missing scores that are to be imputed by Mplus, how many imputed data sets should be created, and under which names the imputed data sets should be saved. In our case, only the variables memory2 and SWB2 have missing values. The IMPUTE $=$ memory2 SWB2; statement defines that missing values need to be filled in only for these two variables (there are no missing values in the Z, memory1, and SWB1 variables). 

Note that the remaining three variables that are listed under USEVAR (i.e., Z, memory1, and SWB1) are used as auxiliary variables in the imputation phase. Therefore, information about missingness contained in these three variables is used to generate proper imputed values for memory2 and SWB2. This parallels what is done in ML estimation with missing data in which all of the information contained in (1) variables that are part of the statistical model and (2) auxiliary variables (if any) is used to generate accurate parameter estimates under the assumption of MAR. 

The NDATASETS $= ~ 5 0$ ; statement is used to request 50 imputed data sets. The SAVE subcommand serves to define the names of the imputed data sets. In our example, the 50 imputed data sets will be saved to the same directory in which the input file is located and will be named CH7_ACL_IMPUTED1.dat;, CH7_ACL_IMPUTED2.dat, . . . , CH7_ACL_IMPUTED50.dat by Mplus. In addition to generating 50 imputed data sets, Mplus also produces a separate file named CH7_ACL_IMPUTEDlist.dat in which all 50 data file names are listed. This list file is required by Mplus in Step 2 of the MI analysis as I show below. The ANALYSIS: TYPE $=$ BASIC; option is specified to obtain descriptive statistics (means, covariances, and correlations) averaged across the 50 imputed data sets. 

The screenshot in Figure 7.2 shows some of the 50 imputed data files as well as the Mplus list file. Note that the imputed data files no longer contain any missing scores and that they can now be analyzed as if there were no missing values. This is done in Step 2 (the analysis phase), for which a separate Mplus input file is used: 

```txt
TITLE: Multiple imputation example  
Step 2: Analysis phase  
Analyze the 50 imputed data sets generated in Step 1 with the autoregressive/cross-lagged model (Figure 7.1)  
DATA: FILE = CH7_ACL_IMPUTEDlist.dat;  
TYPE = IMPUTATION;  
VARIABLE: NAMES = memory2_SWB2 Z memory1_SWB1;  
USEVAR = memory2_SWB2 memory1_SWB1;  
MODEL:  
memory1* SWB1*;  
[memory1* SWB1*];  
memory1 with SWB1;  
memory2 on memory1_SWB1;  
SWB2 on memory1_SWB1;  
memory2 with SWB2;  
OUTPUT: SAMPSTAT STDYX TECH1; 
```

Note that in the DATA command, the list file CH7_ACL_IMPUTEDlist. dat is specified rather than each of the 50 imputed data sets (which would be tedious). By specifying TYPE $=$ IMPUTATION;, we tell Mplus to look for more than one data set based on the list file. The rest of the input file parallels input files that we would use in cases in which we are analyzing a single complete data file without missing data. Notice that we do not have to specify the variable Z as an auxiliary variable here (as we did with ML estimation), given that information about missingness contained in Z was already used in the imputation 

```csv
CH7_ACL_IMPUTED29 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED30 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED31 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED32 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED33 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED34 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED35 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED36 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED37 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED38 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED39 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED40 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED41 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED42 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED43 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED44 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED45 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED46 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED47 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED48 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED49 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTED50 12/12/2019 3:20 PM DAT File 17 KB  
CH7_ACL_IMPUTEDlist 12/12/2019 3:20 PM DAT File 2 KB 
```

FIGURE 7.2. Screenshot of imputed data files created by Mplus. 

phase to properly generate the 50 imputed data files. Below are Mplus output file excerpts for the analysis with the imputed data: 

```txt
SUMMARY OF ANALYSIS   
Average number of observations 300   
Number of replications Requested 50 Completed 50   
Estimator ML   
Input data file(s) Multiple data files from CH7_ACL_IMPUTEDlist.dat 
```

The summary of the analysis shows that we analyzed all 50 imputed data sets (Number of replications) and that the model ran properly for each of the 50 data sets (the number of requested and completed replications is 50, respectively, showing that there were no convergence problems in any of the 50 imputed data sets). Each data set here contains 300 complete cases (given that missing values were imputed), so that the average sample size is 300. Regular ML estimation was used to fit the model to each imputed data element as listed in the file CH7_ACL_IMPUTEDlist.dat. 

Below are the Mplus sample statistics averaged across all 50 imputed data sets followed by the standardized parameter estimates, which were also averaged across the 50 data sets: 

```txt
SAMPLE STATISTICS  
NOTE: These are average results over 50 data sets. Means  
MEMORY2 SWB2 MEMORY1 SWB1  
0.101 0.193 0.027 0.077  
Covariances SWB2 MEMORY1 SWB1  
MEMORY2 0.905  
SWB2 0.483 1.240  
MEMORY1 0.766 0.518 1.018  
SWB1 0.283 0.663 0.367 1.099  
Correlations  
MEMORY2 SWB2 MEMORY1 SWB1 1.000  
SWB2 0.456 1.000  
MEMORY1 0.798 0.461 1.000  
SWB1 0.284 0.568 0.347 1.000 
```

<table><tr><td colspan="6">STANDARDIZED MODEL RESULTS (STDYX Standardization)</td></tr><tr><td></td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td><td>Two-Tailed P-Value</td><td>Rate of Missing</td></tr><tr><td>MEMORY2 ON</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MEMORY1</td><td>0.796</td><td>0.031</td><td>26.035</td><td>0.000</td><td>0.351</td></tr><tr><td>SWB1</td><td>0.008</td><td>0.047</td><td>0.173</td><td>0.862</td><td>0.395</td></tr><tr><td>SWB2 ON</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MEMORY1</td><td>0.300</td><td>0.058</td><td>5.201</td><td>0.000</td><td>0.362</td></tr><tr><td>SWB1</td><td>0.465</td><td>0.052</td><td>8.850</td><td>0.000</td><td>0.319</td></tr><tr><td>MEMORY1 WITH SWB1</td><td>0.347</td><td>0.051</td><td>6.830</td><td>0.000</td><td>0.000</td></tr><tr><td>MEMORY2 WITH SWB2</td><td>0.181</td><td>0.092</td><td>1.961</td><td>0.050</td><td>0.644</td></tr><tr><td>Residual Variances</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MEMORY2</td><td>0.361</td><td>0.041</td><td>8.807</td><td>0.000</td><td>0.343</td></tr><tr><td>SWB2</td><td>0.596</td><td>0.052</td><td>11.537</td><td>0.000</td><td>0.288</td></tr><tr><td>R-SQUARE</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Observed</td><td></td><td></td><td></td><td rowspan="2">Two-Tailed P-Value</td><td rowspan="2">Rate of Missing</td></tr><tr><td>Variable</td><td>Estimate</td><td>S.E.</td><td>Est./S.E.</td></tr><tr><td>MEMORY2</td><td>0.639</td><td>0.041</td><td>15.568</td><td>0.000</td><td>0.343</td></tr><tr><td>SWB2</td><td>0.404</td><td>0.052</td><td>7.825</td><td>0.000</td><td>0.288</td></tr></table>

When comparing the pooled estimates, we can see that they are very close to the ML estimated results that I presented in Section 7.3. This is expected given that ML and MI are (1) statistically equivalent procedures for handling missing data and (2) the relevant auxiliary variables were properly included in both procedures in the present example. 

The last column (Rate of Missing) gives the fraction of missing information (FMI), also referred to as $\boldsymbol { \gamma } _ { 0 }$ (Rubin, 1987). The coefficient $\boldsymbol { \gamma } _ { 0 }$ indicates the proportion of total parameter variance that is due to missing data. It indicates which proportion of the uncertainty in a parameter estimate is due to betweenimputation variability in the parameter estimates (as opposed to usual sampling error, i.e., pooled within-imputation variance or average standard error). When $\boldsymbol { \gamma } _ { 0 }$ $= 0$ , this indicates that there is no between-imputation variance in the estimate. In our example, this is the case for the estimated correlation MEMORY1 WITH SWB1 because there were no missing values at Time 1. Therefore, trivially, none of the uncertainty about this parameter estimate stems from imputing missing values. 

In contrast, for the estimated residual correlation MEMORY2 WITH SWB2, $\gamma _ { 0 } = . 6 4 4$ , indicating that $6 4 . 4 \%$ of the variability (uncertainty) in this parameter estimate was due to missing data. In general, when $\boldsymbol { \gamma } _ { 0 }$ is close to 1, this indicates that a large portion of the uncertainty in the parameter estimate is due to parameter variability across imputed data sets. This may indicate that the quality of the imputed data sets is poor (e.g., due to the omission of relevant auxiliary variables) or that more imputed data sets should be generated to obtain more efficient parameter estimates. 

# 7.4.3 Summary

MI offers an alternative to ML when dealing with missing data. Although MI is more complex, it may be preferred in certain situations, for example, when a researcher wishes to properly fill in missing values to obtain a complete data matrix. Another advantage of MI is that it offers ways to properly address itemlevel missing data. That is, with categorical (e.g., ordinal) variables, ML may not lead to accurate results, whereas MI can work well. 

Despite these advantages, MI also has its challenges. Although Mplus makes the application convenient and rather straightforward, it is up to the user to ensure proper imputation of missing scores. Problems can occur in cases in which relevant auxiliary variables are not included in the imputation phase. That is, in order to impute data correctly, the MAR condition needs to be approximated as closely as possible. Therefore, all relevant variables that account for missingness and/or are correlated with the variables to be imputed should be included in the imputation phase. Note that this issue is no different for ML estimation, which also works properly only if the MAR mechanism is reasonably closely approximated. 

Another critical issue is that researchers need to use a sufficient number of imputed data sets (e.g., 50 or more) to ensure adequate precision of the pooled estimates. With modern computers this should not pose a problem for most applications. Finally, MI may not work when a researcher has many variables to compute. In these cases, researchers should restrict the imputation to the relevant variables used in a model as well as key auxiliary variables. More detailed information on the proper use of MI can be found in Enders (2010). 

# 7.5 PLANNED MISSING DATA DESIGNS

# 7.5.1 Introduction

In order to obtain longitudinal data, researchers have to ask at least some of their participants to provide data on the same variables at multiple time points. Longitudinal designs thus place a significantly higher burden on the participants (and the researcher) than cross-sectional designs in which each participant has to respond to a set of variables only once. As a result of the increased burden of longitudinal studies, researchers may feel that they cannot assess as many different variables given the same sample size. At the same time, it is usually desirable to measure many variables in order to obtain as much information as possible on substantive and auxiliary variables. 

One solution to this problem is to use planned missing data designs in which researchers do not require all participants to provide data on all variables 


TABLE 7.1. Example of a Planned Missing Data Design for the Memory and SWB Example


<table><tr><td>Group</td><td>Memory1</td><td>SWB1</td><td>Memory2</td><td>SWB2</td></tr><tr><td>1 (20%)</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>2 (40%)</td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>3 (40%)</td><td></td><td></td><td>X</td><td>X</td></tr></table>


Note. $\mathrm { X = }$ data are being collected. An empty cell means that no data are being collected for the relevant variables. 


and/or at all time points. In fact, as I show in an applied example below, for many statistical models, it is not necessary to collect data on all waves for very many participants to retain sufficient statistical power. Table 7.1 shows an example of a simple planned missing data design that could be applied to our memory and SWB example (for a thorough discussion of more complex designs, see Graham et al., 2006). In this planned missing design, we consider three groups of participants. Group-1 members $2 0 \%$ of the total sample) are expected to provide complete data on all four study variables (i.e., they have complete data for both time points). Individuals in Group 2 $( 4 0 \% )$ are only required to provide data on their Time-1 memory performance and SWB. No data are collected from Group-2 members at Time 2. Individuals in Group 3 $( 4 0 \% )$ only provide data on their Time 2 memory performance and SWB. No data are collected from Group-3 members at Time 1. 

The design in Table 7.1 has the obvious advantage that complete data are required from only $2 0 \%$ of participants (e.g., $n = 6 0$ in a total sample of $N = 3 0 0$ ). The remaining $8 0 \%$ (e.g., $n = 2 4 0$ in a total sample of $N = 3 0 0$ ) are only required to provide data on either Time 1 or Time 2, but not both. This leads to a considerable reduction in the number of data points that need to be collected and entered into an electronic data base. At the same time, the design retains a large amount of statistical power to detect the autoregressive/cross-lagged effects of interest, as we will see below based on an Mplus simulation example. 

# 7.5.2 Analysis of Planned Missing Data and Simulations in Mplus

The analysis of data obtained from a planned missing data design in Mplus is straightforward because planned missing data satisfy the MCAR mechanism; with planned missing data, missingness is completely unrelated to the study variables of interest. As a consequence, ML estimation as discussed in Section 

7.3 or MI can be used to handle missing scores and take all information into account. Given that MCAR holds, ML parameter estimates will be unbiased. However, planned missingness can cause a reduction in statistical power. 

One useful feature of Mplus in the context of planned missing data designs is that Mplus allows researchers to conduct a priori statistical power analyses for such designs. Such power analyses can help researchers check on whether the planned missing data design that they have in mind provides sufficient statistical power to detect the effects of interest in the study. 

In Mplus, power analyses for planned missing designs can be conducted through Monte Carlo simulation studies. In such a simulation, a researcher specifies the hypothetical population model of interest (e.g., an ACL or other longitudinal model), including the expected parameter estimates, sample size, and planned missing data patterns. Mplus then draws a large number of samples (“replications”) from the specified population (e.g., 1,000 replications), thereby taking into account the expected sample size and planned missing data patterns. The program estimates the parameters of the hypothesized statistical model in each replication and computes the proportion of replications in which the key parameters of interest were statistically significant at the common alpha level of .05. This proportion is an empirical estimate of power (Muthén & Muthén, 2002). For more detailed information on Monte Carlo simulation studies in structural equation modeling, see Bandalos (2006) as well as Paxton, Curran, Bollen, Kirby, and Chen (2001). For more details on the use of Monte Carlo simulations specifically to examine statistical power using Mplus, see Muthén and Muthén (2002). 

Below I illustrate the use of a Monte Carlo simulation study in Mplus to estimate statistical power for an ACL model based on the planned missing data design shown in Table 7.1. The relevant input file to conduct the simulation is given below: 

```matlab
TITLE: Monte Carlo planned missing data simulation of 2-wave autoregressive/cross-lagged model in Figure 7.1  
MONTECARLO:  
NAMES = memory1 memory2 SWB1 SWB2;  
NOBSERVATIONS = 300;  
PATMISS = memory1 (0) memory2 (0) SWB1 (0) SWB2 (0) | memory1 (0) memory2 (1) SWB1 (0) SWB2 (1) | memory1 (1) memory2 (0) SWB1 (1) SWB2 (0);  
PATPROBS = .2 | .4 | .4;  
MODEL POPULATION:  
memory2 on memory1*.8 SWB1*0;  
SWB2 on memory1*.3 SWB1*.5;  
memory1*1 SWB1*1; memory2*.36 SWB2*.6465; [memory1-memory2*0 SWB1-SWB2*0]; 
```

```txt
memory1 with SWB1*.3;  
memory2 with SWB2*0;  
MODEL:  
memory2 on memory1*.8 SWB1*0;  
SWB2 on memory1*.3 SWB1*.5;  
memory1*1 SWB1*1; memory2*.36 SWB2*.6465; [memory1-memory2*0 SWB1-SWB2*0];  
memory1 with SWB1*.3;  
memory2 with SWB2*0;  
OUTPUT: TECH9; 
```

In the Mplus input file, the NAMES subcommand within the MONTE-CARLO command is used to define the number and names of the variables for which data are to be simulated. Here, the names correspond to our two-wave memory and SWB example. The NOBSERVATIONS subcommand defines the sample size to be used in each replication (drawn from the hypothesized population model). Here, the sample size in each replication is $N = 3 0 0$ . The PAT-MISS option is used to specify the missing data patterns that correspond to the desired planned missing data design. The present example uses a design with three groups. 

Group 1 has complete data on all four variables (both time points). This is indicated by the specification memory1 (0) memory2 (0) SWB1 (0) SWB2 (0) | in the first line of the PATMISS subcommand. The number zero in parentheses (0) behind each variable name indicates that the proportion of missingness in Group 1 is zero for all four variables. Group 2 provides complete data for the Time-1 variables (memory1 and SWB1) but has missing data for both Time-2 variables (memory2 and SWB2). This is indicated by the pattern memory1 (0) memory2 (1) SWB1 (0) SWB2 (1) |, where the number (1) in parentheses behind a variable name indicates that $1 0 0 \%$ of the scores for this variable are missing. Group 3 is characterized by complete data for both Time-2 variables (memory2 and SWB2) and missing data for the Time-1 variables (memory1 and SWB1), as indicated by the pattern memory1 (1) memory2 (0) SWB1 (1) SWB2 (0) |. 

The PATPROBS subcommand is used to specify the proportion of each missing data pattern (group). The specification means that the complete data pattern (Group 1, proportion $= . 2 \dot { }$ ) comprises $2 0 \%$ of the population, the missing-Time-2 pattern (Group 2, proportion = .4) comprises $40 \%$ of the population, and the missing-Time-1 pattern (Group 3, proportion $=$ .4) comprises the remaining $4 0 \%$ of the population. In other words, in the example, complete data are collected from only $2 0 \%$ of individuals. The remaining $8 0 \%$ of the population are missing either both Time-1 or both Time-2 variables. 

Subsequently, the population (data-generating) ACL model is specified using the MODEL POPULATION option. For each parameter of the model, a hypothesized population value has to be specified following an asterisk $( { \star } )$ . In this example, I assumed for simplicity that all variables were in z-score metric (population variances set to 1). This facilitated the specification of meaningful path coefficients, as it makes the relevant coefficients equal to standardized regression coefficients. In this example, I assumed that in the population, memory performance showed a strong autoregressive effect (standardized path coefficient $= . 8 )$ ; SWB had no cross-lagged effect on memory performance (standardized path coefficient $= 0$ ); SWB showed a moderate autoregressive effect (standardized path coefficient = .5); and memory performance had a moderate cross-lagged effect on SWB (standardized path coefficient = .3). Together with the specified residual variances (.36 for memory2 and .6465 for SWB2) and Time-1 correlation $\left( r = . 3 \right)$ , these coefficients corresponded to population $R ^ { 2 }$ values of .64 for memory2 and .35 for SWB, respectively. The residual correlation between memory2 and SWB2 (after partialing out memory1 and SWB1) was assumed to be zero. 

The exact population model was specified under MODEL to obtain the proper estimates of statistical power, given the missing data design. In the OUTPUT command, the TECH9 output option was requested, which provides information on error messages (if any) that may have occurred in one or more replications. This is relevant mostly for more complex models in which replications may show convergence or other estimation problems. In the present example simulation, no error messages occurred and all 1,000 replications converged properly. Below are output excerpts demonstrating the key results from the simulation: 

```txt
SUMMARY OF ANALYSIS  
Number of observations 300  
Number of replications  
Requested 1000  
Completed 1000 
```

Mplus first provides information on the sample size in each replication and the number of requested and completed replications. We can see that the correct sample size $\mathrm { ~ N ~ } = 3 0 0 \mathrm { ~ }$ ) was used and that all of the requested 1,000 replications were completed. When simulating more complex models, not all replications may converge due to estimation problems, potentially limiting the utility and generalizability of the simulation results. Therefore, this is important 

information. Subsequently, we obtain information on the missing data patterns, their frequencies, and the covariance coverage in the first replication that was drawn in the simulation: 

```txt
SUMMARY OF DATA FOR THE FIRST REPLICATION Number of missing data patterns 3   
SUMMARY OF MISSING DATA PATTERNS FOR THE FIRST REPLICATION MISSING DATA PATTERNS (x = not missing) 123   
MEMORY2 x x   
SWB2 x x   
MEMORY1 x x   
SWB1 x x   
MISSED DATA PATTERN FREQUENCIES   
Pattern Frequency Pattern Frequency Pattern Frequency 172 2 121 3 107 COVARIANCE COVERAGE OF DATA FOR THE FIRST REPLICATION Minimum covariance coverage value 0.100 PROPORTION OF DATA PRESENT Covariance Coverage   
MEMORY2 SWB2 0.643 0.643   
SWB2 0.643 0.643   
MEMORY1 0.240 0.240 0.597   
SWB1 0.240 0.240 0.597 0.597 
```

We can see that, in line with our requested planned missing data design, there were three missing data patterns. Pattern 1 was the complete data pattern; in Pattern 2, data were missing for both Time-1 variables; and in Pattern 3, data were missing for both Time-2 variables. In the first replication, 72 cases $( 2 4 \% )$ had complete data, 121 cases $( 4 0 . 3 3 \% )$ had data only for Time 2, and the remaining 107 cases $( 3 5 . 6 7 \% )$ had data only for Time 1. Notice that the proportions do not exactly match the population planned missing data proportions of .2, .4, and .4 that I specified under PATPROBS in the input file. This is because of the sampling error that occurs when each replication is drawn from the population in the simulation. 

As a result of the planned missing design that required $8 0 \%$ of the sample to have data for either Time 1 or Time 2 (but not both), covariance coverage was fairly low for the covariances between the Time-1 and the Time-2 variables. Only $2 4 \%$ of cases with complete data in this replication provided data for the relevant across-time covariances. As we will see below, despite this low covariance 

coverage, we obtained unbiased parameter estimates and only slightly reduced statistical power. Below is the Mplus summary of selected parameter estimates across all 1,000 replications. 

<table><tr><td colspan="8">MODEL RESULTS</td></tr><tr><td rowspan="2"></td><td rowspan="2">Population</td><td colspan="2">ESTIMATES</td><td>S. E.</td><td>M. S. E.</td><td colspan="2">95% Sig</td></tr><tr><td>Average</td><td>Std. Dev.</td><td>Average</td><td></td><td>Cover</td><td>Coeff</td></tr><tr><td>MEMORY2 ON</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MEMORY1</td><td>0.800</td><td>0.8015</td><td>0.0654</td><td>0.0663</td><td>0.0043</td><td>0.948</td><td>1.000</td></tr><tr><td>SWB1</td><td>0.000</td><td>0.0037</td><td>0.0847</td><td>0.0790</td><td>0.0072</td><td>0.944</td><td>0.056</td></tr><tr><td>SWB2 ON</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MEMORY1</td><td>0.300</td><td>0.3047</td><td>0.0959</td><td>0.0931</td><td>0.0092</td><td>0.937</td><td>0.889</td></tr><tr><td>SWB1</td><td>0.500</td><td>0.4995</td><td>0.1067</td><td>0.0980</td><td>0.0114</td><td>0.927</td><td>0.990</td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

The column Population gives the specified population parameter that was set in the MONTECARLO command in the input file. The Average column shows the average parameter estimate for each parameter calculated across all 1,000 replications. These averages can be compared to the Population values in the previous column to determine parameter estimate bias. In this simulation, parameter estimate bias was negligible, as can be seen from the fact that all averages closely match the corresponding true population parameter values. 

In the column Std. Dev., Mplus gives the standard deviations of the parameter estimates across the 1,000 replications. This standard deviation can be seen as an empirical (Monte Carlo) standard error estimate. The column S. E. Average provides the averages of the estimated standard errors across replications. The average standard error for a given parameter can be compared to the Monte Carlo standard error estimate in the previous column to determine standard error bias. In our example, there is minimal standard error bias, as indicated by the close correspondence between the values in the Std. Dev. column and the values in the S. E. Average column. The column M. S. E. gives the mean squared error, which is another measure of bias that is frequently used in Monte Carlo studies. The column $9 5 \%$ Cover indicates the proportion of replications in which the estimated $9 5 \%$ confidence interval included the true population parameter and is a measure of the accuracy of confidence intervals. In this case, the coverage is acceptable (close to .95). In summary, these results show that with our planned missing data design, we receive parameters and standard errors with very little bias. This is expected given that the design results in missing values that are missing completely at random. 

The last column, $\%$ Sig Coeff, is of specific interest to us in this chapter, as it allows us to determine the statistical power provided by a planned missing 

data design. % Sig Coeff represents the proportion of replications for which a given parameter estimate was statistically significant at the .05 level. It therefore gives an empirical estimate of power. Typically, researchers aim for at least an $8 0 \%$ chance of correctly rejecting the null hypothesis when it is false (power $= . 8 )$ . 

It can be seen that in the present example all four autoregressive and crosslagged path coefficients exceed a power value of .8. The cross-lagged path coefficient of key interest between memory1 and SWB2 has a power estimate of .889. Therefore, we can conclude that our planned missing data design has sufficient power to detect the population cross-lagged effect of $\boldsymbol { \beta } ^ { \mathrm { s t a n d a r d i z e d } } = . 3$ and that we do not need more cases with complete data in order to obtain sufficient power. 

Interestingly, we are able to retain close to $9 0 \%$ of the power compared to a complete data design. That is, a version of the simulation with $N = 3 0 0$ complete cases (i.e., no missing values for any of the four variables) results in an estimated power value of 1.0 for the same effect. At the same time, the planned missing data design employed here uses $4 0 \%$ fewer data points than the complete data design. This shows that planned missing data designs can be a powerful tool to reduce the burden in longitudinal studies while retaining a large amount of statistical power. 

# 7.6 CHAPTER SUMMARY

Only very few longitudinal studies are free of missing data. Participants have missing scores or drop out of a study for various reasons. Although missing scores are typically undesirable (unless they are the result of a planned missing data design), not all missing data situations lead to underpowered studies or biased results. As I discussed in this chapter, the question of whether missing scores are problematic depends to a large extent on what the underlying missing data mechanism is. MCAR data are the most benign: missingness in this case is completely unrelated to the variables of interest in the study. As a consequence, MCAR data do not lead to biased parameter estimates. However, depending on the amount and patterns of missing data, MCAR may still negatively impact statistical power (i.e., the probability that a true population effect will actually be detected based on the sample data). 

Similar to MCAR data, MAR data (in which missingness can be predicted from variables that were measured in the study) can be handled well as long as the researcher has access to the key variables that predict missingness. In longitudinal studies, MAR is often plausible when a researcher has access to 

previous measurements of the variables that show missingness at later measurement occasions. This is because the previous scores are often correlated with subsequent attrition (e.g., in the memory example described above, low memory functioning led to dropout over time). Including the previously measured scores in the model (which is automatically done in most longitudinal models) often helps to approximate the MAR condition. In addition, it is recommended that researchers collect information on as many potential auxiliary variables (external variables that are correlated with missingness and/or with the study variables that contain missing scores) as possible (Enders, 2010). Such auxiliary variables can help establish or at least approximate the MAR condition, leading to reduced bias and increased statistical power. 

The most problematic missing data mechanism is MNAR, in which missingness is due to the very scores that are missing (i.e., scores on the outcome variable). MNAR is problematic because, in contrast to MAR, a researcher has no information on why the scores are missing. As a consequence, the researcher cannot include this information in the statistical analysis. Therefore, the available scores may lead to biased statistical results (e.g., because individuals with low ability are missing). Although some solutions have been proposed for MNAR data in longitudinal studies (e.g., Enders, 2011), MNAR remains a problematic situation in many studies. 

One strategy to reduce the likelihood of an MNAR situation is again to collect as many variables (including potential auxiliary variables) as possible, including demographic and other background measures. It has also been recommended that a variable be included in longitudinal studies that asks participants at each wave about the likelihood that they will drop out of the study in the future (Schafer & Graham, 2002). Such a variable can serve as a valuable auxiliary variable in subsequent statistical analyses. 

As I showed in this chapter, missingness can also be used to the benefit of an investigator. In planned missing data designs, missing scores are not a post hoc empirical result that a researcher has to face after the study is completed. Instead, missingness is due to a specific a priori measurement design that reduces the number of variables recorded from each participant. Given that missingness is due to the a priori design, the resulting missing scores are in line with the benign MCAR mechanism, and ML or MI techniques can be used to take all available data into account. 

Planned missing data designs are highly advantageous for longitudinal studies, as they allow researchers to collect more variables from fewer participants while retaining a maximum amount of statistical power. As I illustrated based on a small Monte Carlo simulation study, planned missing data designs 

can lead to a large reduction in the number of required data points while retaining almost as much power as a more cumbersome complete-data design. 

One strength of the Mplus software is that it makes it easy for researchers to study the performance of planned missing designs (and other instances of anticipated missing values) a priori through simulations. This can help researchers in the planning phase of a study. Not only can researchers examine the performance of different planned missing designs, but they can also study how different amounts of missing scores due to “natural” dropout over time may affect the parameter estimates, standard errors, and statistical power of a longitudinal study. All models described in this book can be used in Monte Carlo simulation studies in Mplus. Monte Carlo simulations also allow examining statistical power in complete data designs (e.g., Muthén & Muthén, 2002). 

In summary, longitudinal researchers typically have to expect missing scores. Therefore, investigators should already think about this issue in the planning phase of their study. Which participants might drop out of the study and why? Can potential auxiliary variables be included in the study’s measurement design that can later help establish MAR in the statistical analysis phase? 

Once the data have been collected, researchers should carefully study patterns and correlates of missing scores to identify potential causes and correlates of missingness as well as auxiliary variables to be included in the statistical analysis of interest. Modern missing data handling techniques such as ML and MI can then be applied to properly address missingness. These techniques help avoid (or at least reduce) biased parameter estimates and retain as much statistical power as possible. As I showed in this chapter, Mplus makes it easy to apply especially the ML technique and to include auxiliary variables to improve its performance. Both ML and MI can be applied to all the longitudinal models I discuss in this book. 

# 7.7 RECOMMENDED READINGS



Enders, C. K. (2010). Applied missing data analysis. New York: Guilford Press. 





Graham, J. W., Taylor, B. J., Olchowski, A. E., & Cumsille, P. E. (2006). Planned missing data designs in psychological research. Psychological Methods, 11, 323–343. 





Little, R. J. A., & Rubin, D. B. (2002). Statistical analysis with missing data (2nd ed.). New York: Wiley. 





Muthén, B. O., & Muthén, L. K. (2002). How to use a Monte Carlo study to decide on sample size and determine power. Structural Equation Modeling, 4, 599–620. 



Rubin, D. B. (1987). Multiple imputation for nonresponse in surveys. New York: Wiley. 

Schafer, J. L., & Graham, J. W. (2002). Missing data: Our view of the state of the art. Psychological Methods, 7, 147–177. 

# NOTE

1. Missing value codes are allowed to differ between variables in Mplus and there can also be multiple missing value codes for a given variable. Details on how to deal with multiple codes can be found in the Mplus user’s guide (Muthén & Muthén, 1998–2017). 

# 8

# How to Choose between Models and Report the Results

In this book, I discussed a variety of different longitudinal models. In practice, researchers may be unsure about which model to select in their specific application. In addition, researchers are often unsure about how to present the results, for example, in a journal article. In this final chapter, I provide some guidelines on model selection and on how to report results. 

# 8.1 MODEL SELECTION

My selection of models in this book covered a range of approaches that are frequently used in practice. Which model should a researcher use and under what circumstances? In this section, I provide some general recommendations, ideas for modeling strategies, and guidelines for model selection. 

As a general recommendation, I suggest that researchers prefer multipleindicator models (Chapters 4 and 5) over single-indicator models (Chapters 2 and 3) whenever possible because of the greater flexibility and robustness of multiple-indicator models. I provided a detailed discussion of the advantages and limitations of multiple-indicator models in the chapter summary in Chapter 5. To reiterate, multiple-indicator models have a number of key advantages, including stronger identification status and greater estimation stability; these models offer the possibility to conduct detailed tests of measurement equivalence (ME) across time. Multiple-indicator models can be used whenever data 

from multiple items or scales are available for each construct under study; this is often the case in practice. 

When multiple-indicator designs are used, a good starting point for a longitudinal analysis is the latent state (LS) model described in Chapter 4. This model and its extended version with indicator-specific factors (LS-IS) are useful first to examine whether the same factor structure holds across occasions, whether indicator-specific (methods) effects are present, and what level of ME can be assumed for the indicators. Second, these models are unrestrictive in their structural model components. Therefore, these models focus on evaluation of the measurement model. This is useful because logically, measurementrelated issues should be examined before we move on to structural (latent variable) analyses. For example, if the hypothesized factor structure (number of factors or loading pattern) turns out to be incorrect or if the factor structure changes across time, there would be no point in conducting tests of latent variable mean changes over time. In this case, the proper measurement model has to be established first before moving on to tests related to the latent variable structure. 

Both the LS and LS-IS models allow researchers to examine the psychometric properties (e.g., factor structure, reliability, indicator specificity, and measurement equivalence) of their measures before testing specific hypotheses about changes in latent variables across time. At the same time, the LS and LS-IS models still allow researchers to already conduct preliminary analyses of changes in latent variables by examining latent state factor means, variances, and covariances (provided that a sufficient level of ME can be established) before more complex models are tested. 

Multiple-indicator models require that researchers use measurement designs with more than one (and preferable three or more) repeatedly measured variables. This is not always feasible, and researchers will sometimes have no choice but to apply single-indicator models. In this case, depending on the model to be used, it can be useful to collect a larger sample and/or more measurement occasions, if possible, to compensate for some of the problems that can arise in single-indicator models. For example, as I discussed in detail in Chapter 3, the trait–state occasion (TSE) model tends to be empirically underidentified and unstable in smaller samples and/or with a small number of measurement occasions. The use of a larger sample and/or more measurement occasions can make this model feasible when there is only one measure. Applied Monte Carlo simulation studies can help researchers determine the necessary sample size and/or number of time points for a given model (e.g., Cole et al., 2005; Muthén & Muthén, 2002; Paxton et al., 2001; see also Chapter 7). In other cases, it may be easier to add another measure or two (rather than increase the sample size or 

number of occasions) and use multiple-indicator latent state–trait (LST) models (see Chapter 5) that do not share the instability problems of the TSE model. 

Which specific model (e.g., single-trait, autoregressive, state–trait, or growth) should researchers use in either case (single- or multiple-indicator design) after they have conducted analyses with preliminary models such as the LS and LS-IS models? To answer this question, it is useful to recall that different models can imply different longitudinal processes such as stability, variability, and/or trait changes across time. A researcher should select the model that best reflects their theory about the longitudinal course of the construct under study. 

For example, some constructs (e.g., intelligence) may predictably remain more or less perfectly stable across a certain range of time (e.g., across 5 years of adulthood). For other constructs such as mood and emotions, it may be predicted that they remain relatively stable over time except for some reversible situation-specific fluctuations in true scores across occasions. In yet another scenario, enduring changes in the trait scores may be expected over time (e.g., changes in emotion regulation from childhood to early adolescence). 

When a researcher hypothesizes that an attribute under study is essentially a trait construct with very high or even perfect stability of individual differences and/or mean stability across time (e.g., intelligence), single-factor models as described in Chapter 2 can be tried in the first step. These models imply processes of trait stability and/or processes with rather minimal trait changes.1 

In the most extreme case (the random intercept model; see Section 2.2 in Chapter 2), no changes in the true scores over time are allowed at all. Though unrealistic for most applications, the random intercept model is a useful baseline model for longitudinal studies because it allows testing the hypothesis of perfect (mean and covariance) stability. Subsequent models (random and fixed intercepts, $\xi .$ -congeneric; see Sections 2.3 and 2.4) relax the assumption of perfect stability to some degree (e.g., by allowing for mean differences over time as in the random and fixed intercepts model) and may be useful for constructs that are almost perfectly stable across time (e.g., intelligence scores). 

When trait-change processes involve enduring changes in the rank order of trait scores over time (e.g., changes in cognitive ability scores), latent change or latent growth curve models can be examined. Latent change score models have the advantage that they are somewhat more flexible in that they do not restrict trait changes to following a specific form (e.g., linear or quadratic changes). Pure trait-change models are especially useful when constructs show little situation dependence (e.g., measures of cognitive abilities). 

In contrast, when a construct is expected to have a stable or essentially stable trait component but to show reversible situational variability (e.g., mood states fluctuating around a dispositional mood level), latent state–trait (LST) 

models are most appropriate. This is because LST models allow separating trait influences from state residual and measurement error components. When both state variability and trait-change processes are at work, hybrid models such as the multiple-indicator latent trait-change and growth curve models described in Chapter 5 best reflect this process. Change score and growth models allow researchers to directly express true individual differences in change over time with latent difference score variables. Latent difference score variables can be related to external variables, for example, to predict individual differences in change. 

Autoregressive/cross-lagged (ACL) models with latent variables are useful when researchers want to examine the over-time relationships of two or more repeatedly measured constructs. ACL models allow examining, for example, whether Construct 1 predicts another Construct 2 over time above and beyond Construct 1’s autoregression (stability) and vice versa. Such models are therefore especially useful to examine and rule out certain causal effect hypotheses (e.g., does depression cause anxiety, or does anxiety cause depression?), although they typically do not allow a researcher to prove that a causal effect exists (unless the underlying experimental design is very strong). 

In summary, I recommend that researchers fit models that best reflect their theories and hypotheses about the longitudinal process that characterizes the construct(s) under study. In addition, model comparisons can sometimes be helpful when competing theories exist. For example, is impulsivity a state or a trait construct? Do impulsivity trait scores remain stable across adulthood, or do they change? These questions can be examined by fitting different longitudinal models (e.g., single-trait-only model, latent state–trait model, hybrid LST traitchange models) and comparing their fit. The best-fitting model may be the one that best represents the longitudinal process at work. 

# 8.2 REPORTING RESULTS

In this section, I provide some guidelines and examples for how to report the results of longitudinal structural equation analyses. I begin with general recommendations. Later in the chapter, I discuss a specific example application. 

# 8.2.1 General Recommendations

As a general rule, reports should be detailed enough and include all of the relevant information for the study to be $1 0 0 \%$ replicable by other researchers. 

Moreover, readers of the report should be able to reanalyze the presented data with alternative models. In structural equation modeling, this can frequently be accomplished without providing the raw data. Many types of longitudinal structural equation analyses only require summary statistics, that is, the covariance matrix and mean vector of the observed variables used in the models as well as any potential control variables (or the means, correlation matrix, and standard deviations from which the covariance matrix can be inferred). For item-level (ordinal) data, the polychoric correlation matrix can be provided to make the results replicable. With the exception of intensive longitudinal models (Chapter 6), all models presented in this book can be replicated based on such summary statistics (i.e., without access to raw data). In addition, some specific robust estimation methods require raw data for replication (e.g., methods for handling clustered [multilevel] or non-normal data). 

In cases in which journal space does not suffice to report all data, supplemental analyses, and additional information needed to make the analyses and results fully transparent and replicable in an article, researchers can create a free permanent repository on the Open Science Forum website at https://osf.io in which they can store online supplemental materials. In addition, many journals now offer the possibility to submit and permanently store online supplemental materials as part of their own websites so that there is basically no limit to how much additional information can be provided. I strongly recommend that researchers make use of these opportunities. 

A convenient approach for many types of analyses when using Mplus is simply to store the Mplus output files (including sample statistics and missing data pattern information) in an online repository. In this way, a lot of the relevant information becomes readily accessible because the Mplus output files can be generated in such a way that they include information on both model specification and parameter estimates as well as the relevant sample statistics (SAMPSTAT; e.g., the covariance matrix and mean vector) that can be used to properly reproduce the model results or fit alternative models. In addition, information regarding missing scores (e.g., the missing data patterns and covariance coverage, see below) can be included in the output file. 

# 8.2.2 Methods Section

I recommend that researchers provide a sufficiently detailed description of the sample, measures (observed variables), longitudinal design, and statistical model(s) in their Methods section so that other researchers can replicate the results with the same or other data. 

# 8.2.2.1 Sample

Not only the sample size, but also the sampling process (e.g., simple random sample? representative population sample? convenience sample? cluster sample?) should be made transparent, and demographic information should be provided. Were any cases excluded from the final analyses (e.g., outliers or invalid scores)? If yes, what were the criteria for excluding cases? 

Researchers should also report the amounts and patterns of missing data (if any), the covariance coverage, and the assumed missing data mechanism (for details, see Chapter 7). The report should make clear why a specific missing data mechanism (e.g., missing at random data) was deemed plausible for the data at hand. This can be accomplished by presenting the results of detailed missing data analyses (e.g., mean comparisons across cases with and without missing scores). Lastly, researchers dealing with missing scores should clearly state which approach they used to handle missing data (e.g., maximum likelihood or multiple imputation, see Chapter 7) and whether or not they included any auxiliary variables in the missing data handling procedure. When multiple imputation is used, details on how the data were imputed should be provided (for examples of how to present the results of a missing data analysis, see Enders, 2010). Summary data reported for reanalysis or replication purposes (see above) should be accompanied by information on whether these statistics are based on complete data, full information maximum likelihood estimation with missing data, or multiple imputation as well as the relevant sample size. 

# 8.2.2.2 Measures

Researchers should clearly state the indicators (measured variables such as items, questionnaire scales, or tests) they used in the model and how many measurement occasions they considered. They should also note whether the indicators were categorical or continuous. For categorical indicators, researchers should give the number of response categories and they should explain how the categorical nature of the items was taken into account in their analyses (e.g., by using mean- and variance-adjusted least squares estimation; see Chapter 3, Box 3.11). The psychometric properties of the measures should also be addressed. In particular, evidence for the reliability and validity of the measures should be provided. As I showed in this book, reliability estimates can often be derived from the estimated model parameters of the longitudinal model fit to the data. This approach is often preferable to using reliability estimates obtained from different samples. 

When data violate certain assumptions (e.g., when there is nonindependence of observations due to multilevel data or when data are non-normal), researchers should report this along with relevant statistics (e.g., intraclass correlation coefficients as measures of dependence; skewness and kurtosis measures to indicate the degree of non-normality) and indicate how these violations were addressed (e.g., by using robust estimation methods). 

# 8.2.2.3 Model Description

Researchers should first explain why they chose a specific statistical model (or set of competing models) for their analyses. For example, a researcher’s theory may predict that a construct shows stable trait levels in conjunction with situation-specific variability. The researcher wants to test this theory and determine the proportions of trait versus situation-specific variability. Therefore, the researcher may choose a latent state–trait model for analysis. In another case, a researcher might predict linear increases in a construct over time and select a linear growth curve model for the analysis. 

For the purpose of model description, it is often useful to include a path diagram of the specified model. Ideally, the path diagram further clarifies what the indicators were, how many measurement occasions were included in the analysis, and which parameters in the model were freely estimated versus fixed (and if fixed, to which specific values). In addition, it may be necessary to include more specific descriptions of the model parameters, any additional model constraints (e.g., ME or other parameter equality restrictions), and/or different versions of the same model in the text. As an example, consider the following description of an LST model: 

To examine whether positive affect represented more of a trait or more of a situation-dependent construct, we fit the latent state–trait (LST) model depicted in Figure 8.1 to the three affect items happy, calm, and content. This model is known as the multitrait–multistate (MTMS) model (Eid, 1996). To account for stable itemspecific variance, each of the three measured items had its own (item-specific) trait factor $T _ { i }$ in the model $\overset { \cdot } { 1 } =$ indicator). In addition, all measured variables that shared the same measurement occasion loaded on a common time-specific state residual factor $S R _ { t }$ $\langle t =$ time point). Measurement error influences $( e _ { i t } )$ were also taken into account for each variable in the model. All trait factors were allowed to correlate, enabling us to examine the degree of homogeneity of the trait components across items. We assumed all latent state residual factors to be uncorrelated with each other as well as with the trait factors. Measurement error variables were also uncorrelated with all other latent variables. 

In our model, we assumed strong measurement equivalence such that all intercepts were fixed to zero, all trait factor loadings were fixed at 1, and all state residual factor loadings $( \delta _ { i } )$ were constrained to be time-invariant (set equal across time for the same indicator). Therefore, we estimated only two state residual factor loadings $( \delta _ { 2 }$ and $\delta _ { 3 }$ ; the first state residual loading $\delta _ { 1 }$ was fixed to 1 at each time point to set the scale of each state residual factor as shown in Figure 8.1), three trait factor means, three trait factor variances, three trait factor covariances $( \phi )$ , three state residual factor variances, and nine measurement error variances. In total, there were 23 free parameters. With three repeatedly measured variables on three occasions, there were 54 pieces of known information (9 means, 9 variances, and 36 covariances). The model thus had 31 degrees of freedom. Given that the three items were measured on a scale from 0 to 100 and approximately normally distributed, we obtained model fit statistics and parameter estimates through maximum likelihood estimation in Mplus version 8. 

Notice that I included a detailed description of which parameters were estimated versus constrained in the model. This information is important because it may not always be obvious from a path diagram or the model results (fit statistics and parameter estimates) reported later on. In many practical applications, it remains unclear which parameters were (or were not) estimated and why a model had a given number of degrees of freedom. When this is not clear, an exact replication of the analyses may be impossible. Together with the path diagram in Figure 8.1, other researchers should be able to exactly reproduce the analysis and/or apply the exact same model to a replication data set. Therefore, a detailed description of the model parameters and degrees of freedom computation is useful as it increases the transparency and replicability of the analyses. Notice that I also described which estimation method (maximum likelihood) and specific software package (Mplus) was used to obtain model fit information and parameter estimates. In this case, maximum likelihood estimation was used because of the quasi-continuous nature of the items and approximately normal distributions. In cases in which items have few response categories and/ or deviate strongly from non-normality, other estimators should be chosen (e.g., WLSMV; see Chapter 3, Box 3.11). 

Notice that Bayesian statistical techniques as employed with modern dynamic structural equation modeling (Chapter 6) typically require more detailed descriptions regarding the analytic approach than do traditional approaches to fitting longitudinal models such as frequentist maximum likelihood estimation. This is because Bayesian methods involve a larger number of subjective decisions (e.g., regarding the choice of priors or the burn-in phase; asee Chapter 6 for details). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-03/7e0c717a-2a86-4ae7-b2f3-8b2c1d011cd6/656f237b0f78113db8ab2e95294eff9c65bebc4b4feca76a419dbf3f946ac6fa.jpg)



FIGURE 8.1. Multitrait–multistate (MTMS) model fit to three affect items $Y _ { i t } \left( i = \mathrm { i t e m } \right.$ $Y _ { i t }$ , $t =$ time point) on three measurement occasions. $T _ { \mathrm { i } } =$ trait factor; $S R _ { t } =$ state residual factor; $e _ { i t } =$ measurement error variable; $\delta _ { \mathrm { i } } =$ time-invariant state residual factor loading; $\phi _ { \mathrm { i i ^ { \prime } } } =$ trait factor covariance.


# 8.2.3 Results Section

# 8.2.3.1 Descriptive Statistics

In the Results section, researchers should typically first discuss descriptive statistics for the measured variables used in their analyses. For continuous indicators, it is useful to include the means, standard deviations, and the correlation matrix. Not only does this allow researchers to replicate the analyses or fit alternative models, but it also provides useful information regarding the measured variables (e.g., how strongly were they correlated?). In addition to the means, standard deviations, and correlations, researchers may include information about skewness and kurtosis. This is particularly useful when measures are non-normal. 

For categorical items with few response categories, researchers might include information on the proportions of responses in each category as well as the matrix of tetrachoric correlations (for binary indicators) or polychoric 

correlations (for ordinal indicators). Mplus provides these statistics for binary and ordinal variables when defining the indicators as CATEGORICAL (see Chapter 3, Box 3.11). 

# 8.2.3.2 Estimation Problems and Model Fit Information

In the next step, estimation problems (if any) should be reported. For example, models sometimes do not converge or show improper parameter estimates (e.g., negative variances). In these cases, researchers should be open about these issues and clearly explain how they were addressed. For example, a convergence problem may simply be due to variables being measured on very different scales. Providing user-defined starting values, rescaling variables to a more similar metric, or choosing alternative methods of scale setting may solve this issue. In other cases, models showing convergence problems or improper parameter estimates may require more serious respecification (e.g., nonconvergence and improper estimates can be due to an overparameterization or other misspecification), and researchers should explain their rationale for such respecifications in sufficient detail. 

Subsequently, fit statistics should be reported for all examined models. In line with Schermelleh-Engel, Moosbrugger, and Müller (2003), I recommend that multiple fit statistics be included in addition to the overall model chi-square value, its degrees of freedom, and $p$ -value. For example, a description of model fit may read as follows: 

The MTMS model fit the three affect items well, χ2 (31, $N = 3 0 0 ) = 4 1 . 0 2$ , $p = . 1 1$ , RMSEA $= 0 . 0 3$ , $\mathrm { C F I } = 0 . 9 9$ , SRMR = 0.05. 

In cases in which multiple competing models are compared, fit statistics may be more efficiently communicated through a table. For an example, see Table 4.1 in Chapter 4 in this volume or Table 3 in Irwin, Marks, and Geiser (2018). When multiple models are compared, the discussion of model fit should end with a clear statement regarding which model was selected and why. 

# 8.2.3.3 Parameter Estimates, Standard Errors, Effect Sizes, and Tests of Statistical Significance

Subsequently, the full set of unstandardized model parameters should be reported along with the corresponding standard errors. Unstandardized parameters have the advantage that they are more easily compared across different samples (e.g., independent groups or different studies) than standardized parameters that 

depend more heavily on the variances in a given sample or population. This is important, for example, for meta analyses that compare effects across studies. 

Standard errors are important because they inform readers about the degree of precision of the parameter estimates. Small standard errors indicate high precision, whereas large standard errors can indicate a lack of precision (e.g., due to a small sample) and/or problems with the model (e.g., empirical underidentification). Standard errors can also be used to construct confidence intervals around parameter estimates and to conduct tests of statistical significance.2 In some situations, it may be useful to report the results of test statistics (e.g., z-scores) for individual parameter estimates, along with the corresponding $p$ -values (for testing the null hypothesis that a parameter is zero in the population). 

In many cases, it will be useful to also report standardized parameter estimates. For example, standardized factor loadings can be informative as they indicate the correlations between a variable and its factor(s) in some models (e.g., many LST models; see the example in Table 8.1). Note that this is not true for all longitudinal models. For example, in many types of latent growth curve models, variables load on multiple growth factors (e.g., intercept and slope), and the growth factors are often allowed to correlate. In cases in which variables load on multiple correlated factors, the standardized loadings cannot be interpreted as correlations. 

For latent factors, standardized covariance estimates are informative as they represent correlations between factors (see the example presented in Table 8.1). Correlations are easier to interpret than covariances and can also be seen as standardized effect size measures. It has been recommended that scientists report effect size measures in addition to (or instead of) tests of statistical significance (e.g., Kline, 2020). In addition, it may be useful to include other standardized effect size measures (e.g., Cohen’s $d$ for mean differences). 

To reduce the amount of information presented in the text, it is typically helpful to report the parameter estimates in one or more tables (see Tables 8.1 and 8.2 for examples). The most relevant findings can then be highlighted in the main text. For example, a description summarizing key parameter estimates in an application of the MTMS model could read as follows: 

The parameter estimates for the MTMS model are presented in Table 8.1. Trait factors had larger variances than did state residual factors. In addition, it can be seen that for the items happy and calm, standardized trait factor loadings were larger than standardized state residual factor loadings. In contrast, for the item content, standardized trait factor loadings were smaller than standardized state residual factor loadings. Taken together, these results indicate a stronger trait influence on the item scores for happy and calm as compared to content. 


TABLE 8.1. Parameter Estimates and Standard Errors for the MTMS Model


<table><tr><td>Parameter</td><td>Estimate</td><td>SE</td><td>Standardized estimate</td></tr><tr><td colspan="4">Trait factor loadings</td></tr><tr><td>Happy</td><td>1.00a</td><td>—</td><td>.71, .71, .70c</td></tr><tr><td>Calm</td><td>1.00a</td><td>—</td><td>.74, .73, .74c</td></tr><tr><td>Content</td><td>1.00a</td><td>—</td><td>.58, .63, .59c</td></tr><tr><td colspan="4">SR factor loadings</td></tr><tr><td>Happy</td><td>1.00a</td><td>—</td><td>.52, .51, .53c</td></tr><tr><td>Calm</td><td>0.88b</td><td>0.06</td><td>.48, .47, .50c</td></tr><tr><td>Content</td><td>1.37b</td><td>0.09</td><td>.67, .72, .69c</td></tr><tr><td colspan="4">Factor means</td></tr><tr><td>Trait 1 (Happy)</td><td>50.11</td><td>0.67</td><td></td></tr><tr><td>Trait 2 (Calm)</td><td>50.16</td><td>0.64</td><td></td></tr><tr><td>Trait 3 (Content)</td><td>50.01</td><td>0.63</td><td></td></tr><tr><td colspan="4">Factor variances</td></tr><tr><td>Trait 1 (Happy)</td><td>99.39</td><td>11.01</td><td>1.00a</td></tr><tr><td>Trait 2 (Calm)</td><td>96.76</td><td>10.22</td><td>1.00a</td></tr><tr><td>Trait 3 (Content)</td><td>75.16</td><td>10.21</td><td>1.00a</td></tr><tr><td>SR Time 1</td><td>52.63</td><td>8.03</td><td>1.00a</td></tr><tr><td>SR Time 2</td><td>51.77</td><td>8.00</td><td>1.00a</td></tr><tr><td>SR Time 3</td><td>56.09</td><td>8.60</td><td>1.00a</td></tr><tr><td colspan="4">Factor covariances and correlations</td></tr><tr><td>Trait 1 (Happy) with Trait 2 (Calm)</td><td>67.03</td><td>8.91</td><td>.68</td></tr><tr><td>Trait 1 (Happy) with Trait 3 (Content)</td><td>67.11</td><td>9.24</td><td>.78</td></tr><tr><td>Trait 2 (Calm) with Trait 3 (Content)</td><td>37.37</td><td>7.98</td><td>.44</td></tr><tr><td colspan="4">Measurement error variances</td></tr><tr><td>Happy, Time 1</td><td>43.93</td><td>6.22</td><td>.22d</td></tr><tr><td>Calm, Time 1</td><td>46.03</td><td>6.17</td><td>.23d</td></tr><tr><td>Content, Time 1</td><td>45.12</td><td>6.29</td><td>.23d</td></tr><tr><td>Happy, Time 2</td><td>37.95</td><td>5.48</td><td>.22d</td></tr><tr><td>Calm, Time 2</td><td>43.47</td><td>5.73</td><td>.24d</td></tr><tr><td>Content, Time 2</td><td>36.54</td><td>5.43</td><td>.21d</td></tr><tr><td>Happy, Time 3</td><td>48.71</td><td>8.98</td><td>.22d</td></tr><tr><td>Calm, Time 3</td><td>16.98</td><td>7.09</td><td>.09d</td></tr><tr><td>Content, Time 3</td><td>39.09</td><td>8.25</td><td>.18d</td></tr></table>


Note. $S R =$ latent state residual factor. Standardized factor loadings can be interpreted as correlations between measured variables and latent factors. a Parameter fixed a priori for model identification or theoretical reasons; b parameter set equal across time; c standardized factor loadings are reported in the following order: Time 1, Time 2, Time 3; d standardized measurement error variances indicate 1 – Reliability. Dashes (—) indicate that a standard error was not computed due to a parameter being fixed rather than freely estimated. All intercepts were fixed to zero and are therefore not shown in the table. 


The trait factors for happy and calm as well as happy and content were strongly (.68 and .78) correlated, whereas the correlation between the calm and happy trait factors was modest (.44). This indicated that, although all three trait factors were substantially positively related, each item also reflected a unique aspect of the positive affect trait construct that was not shared with the other items. 

Estimates of consistency (CO), occasion specificity (OS), and reliability were computed based on the parameter estimates in Table 8.1 and can be found in Table 8.2. We report CO and OS values for both the item scores and the underlying true scores. For happy and calm, CO values were higher than OS values, indicating that these items reflected more trait than state residual variance. The content item showed slightly higher OS than CO values, indicating that this item was more strongly influenced by situational and/or person $\times$ situation interaction effects than the other two items. Estimated reliability coefficients were $\geq . 7 7$ for all item scores and indicated appropriate measurement precision given that the indicators were single-item measures. 

Due to space constraints and depending on the size and complexity of the model, it may not always be possible to include all parameter estimates directly in the report. In these cases, researchers should nonetheless ensure that they include the full set of parameters (e.g., as part of an Mplus output file) in an online appendix. That way, the full set of results is made available to other 


TABLE 8.2. Consistency, Occasion Specificity, and Reliability Coefficients


<table><tr><td>Item</td><td>CO(item)</td><td>OS(item)</td><td>Reliability</td><td>CO (true scores)</td><td>OS (true scores)</td></tr><tr><td>Happy, Time 1</td><td>.51</td><td>.27</td><td>.78</td><td>.65</td><td>.35</td></tr><tr><td>Calm, Time 1</td><td>.55</td><td>.23</td><td>.78</td><td>.70</td><td>.30</td></tr><tr><td>Content, Time 1</td><td>.34</td><td>.44</td><td>.78</td><td>.43</td><td>.57</td></tr><tr><td>Happy, Time 2</td><td>.50</td><td>.26</td><td>.77</td><td>.66</td><td>.34</td></tr><tr><td>Calm, Time 2</td><td>.54</td><td>.22</td><td>.76</td><td>.71</td><td>.29</td></tr><tr><td>Content, Time 2</td><td>.40</td><td>.51</td><td>.91</td><td>.44</td><td>.56</td></tr><tr><td>Happy, Time 3</td><td>.50</td><td>.28</td><td>.78</td><td>.64</td><td>.36</td></tr><tr><td>Calm, Time 3</td><td>.55</td><td>.25</td><td>.79</td><td>.69</td><td>.31</td></tr><tr><td>Content, Time 3</td><td>.34</td><td>.48</td><td>.82</td><td>.42</td><td>.58</td></tr></table>


Note. CO $=$ consistency (proportion of trait variance); $\mathrm { O S = }$ occasion specificity (proportion of state residual variance). CO(item) and OS(item) sum up to Reliability for a given item within rounding error. CO(true scores) and OS(true scores) sum up to 1.0 for a given item. 


researchers without using too much journal space. The article by Irwin et al. (2018) can be consulted for a more detailed example of how to report the results of a latent state–trait analysis. More guidelines on how to report the results of structural equation modeling analyses in general can be found in Kline (2016). 

# 8.3. CHAPTER SUMMARY

In this chapter, I provided some guidelines for model selection and for how to report the results of a longitudinal structural equation analysis. I recommend that researchers favor multiple-indicator approaches over single-indicator models whenever possible. In addition, a researcher’s theory about the longitudinal process at work should guide the selection of the specific longitudinal model to be used. In some cases, model fit statistics can help decide between competing models that imply different longitudinal processes (e.g., trait stability vs. trait change). 

When writing up the results, clarity, transparency, and replicability of both methods (including sample, measures, missing value handling, and model description) and statistical results (observed variable descriptive statistics, fit statistics, and model parameter estimates) are very important. Data sets should be made available so that other researchers can check the analyses or fit alternative models. Often, summary data sets (correlations, means, and standard deviations) are sufficient, and these statistics should be reported in the paper anyway. After completing a report of a longitudinal study, researchers should ask themselves: Would I be able to exactly reproduce the statistical analyses based on the information provided? If this is not the case, then the report should be revised to include more details, or additional supplemental materials should be provided. These recommendations are general in nature and apply to many other kinds of empirical reports beyond those dealing with longitudinal studies. 

# 8.4 RECOMMENDED READINGS



Enders, C. K. (2010). Applied missing data analysis. New York: Guilford Press. 





Irwin, H. J., Marks, A. D. G., & Geiser, C. (2018). Belief in the paranormal: A state, or a trait? Journal of Parapsychology, 82, 24–40. 





Kline, R. B. (2016). Principles and practice of structural equation modeling (4th ed.). New York: Guilford Press. 



# NOTES

1. Notice that, although not explicitly shown in this book, single-trait factor models can also be applied to multiple-indicator data. For example, the singletrait– multistate (STMS) model discussed in Section 5.4.2 or the multitrait–multistate (MTMS) model discussed in Section 5.4.4 could be specified without state residual factors implying a process of trait stability with no situation or person $\times$ situation interaction effects. 

2. Confidence intervals for all parameter estimates can be requested in Mplus by specifying OUTPUT: CINTERVAL; in the input file. 

# References



Asparouhov, T., Hamaker, E. L., & Muthén, B. (2018). Dynamic structural equation models. Structural Equation Modeling, 25, 359–388. 





Asparouhov, T., & Muthén, B. (2010). Multiple imputation with Mplus (Version 2). Mplus technical report. Retrieved March 27, 2019, from http://statmodel2.com/ download/Imputations7.pdf. 





Bandalos, D. L. (2006). The use of Monte Carlo studies in structural equation modeling research. In G. R. Hancock & R. O. Mueller (Eds.), Structural equation modeling: A second course (pp. 385–426). Greenwich, CT: Information Age. 





Bentler, P. M. (1990). Comparative fit indexes in structural models. Psychological Bulletin, 107, 238–246. 





Bentler, P. M. (1995). EQS structural equations program manual. Encino, CA: Multivariate Software. 





Bishop, J., Geiser, C., & Cole, D. A. (2015). Modeling growth with multiple indicators: A comparison of three approaches. Psychological Methods, 20, 43–62. 





Bollen, K. A. (1989). Structural equations with latent variables. New York: Wiley. 





Bollen, K. A., & Curran, P. J. (2006). Latent curve models: A structural equation perspective. New York: Wiley. 





Bollen, K. A., & Long, J. S. (1993). Testing structural equation models. Newbury Park, CA: Sage. 





Byrne, B. M., Shavelson, R. J., & Muthén, B. O. (1989). Testing for the equivalence of factor covariance and mean structures: The issue of partial measurement invariance. Psychological Bulletin, 105, 456–466. 





Chen, F., Bollen, K. A., Paxton, P., Curran, P., & Kirby, J. (2001). Improper solutions in structural equation models: Causes, consequences, and strategies. Sociological Methods and Research, 29, 468–508. 





Cohen, J., Cohen, P., West, S. & Aiken, L. (2003). Applied multiple regression/correlation analysis for the behavioral sciences. Mahwah, NJ: Erlbaum. 





Cole, D. A., Martin, N. M., & Steiger, J. H. (2005). Empirical and conceptual problems with longitudinal trait–state models: Introducing a trait–state–occasion model. Psychological Methods, 10, 3–20. 





Duncan, T., Duncan, S., & Strycker, L. (2006). An introduction to latent variable growth curve modeling: Concepts, issues, and applications (2nd ed.). Mahwah, NJ: Erlbaum. 





Eid, M. (1995). Modelle der Messung von Personen in Situationen [Models for measuring persons in situations]. Weinheim, Germany: Beltz. 





Eid, M. (1996). Longitudinal confirmatory factor analysis for polytomous item responses: Model definition and model selection on the basis of stochastic measurement theory. Methods of Psychological Research—Online, 1, 65–85. 





Eid, M., Courvoisier, D. S., & Lischetzke, T. (2012). Structural equation modeling of ambulatory assessment data. In M. R. Mehl & T. S. Connor (Eds.), Handbook of research methods for studying daily life (pp. 384–406). New York: Guilford Press. 





Eid, M., & Hoffmann, L. (1998). Measuring variability and change with an item response model for polytomous variables. Journal of Educational and Behavioral Statistics, 23, 193–215. 





Eid, M., Holtmann, J., Santangelo, P., & Ebner-Priemer, U. (2017). On the definition of latent state–trait models with autoregressive effects: Insights from LST-R theory. European Journal of Psychological Assessment, 33, 285–295. 





Eid, M., Schneider, C., & Schwenkmezger, P. (1999). Do you feel better or worse? The validity of perceived deviations of mood states from mood traits. European Journal of Personality, 13, 283–306. 





Enders, C. K. (2010). Applied missing data analysis. New York: Guilford Press. 





Enders, C. K. (2011). Missing not at random models for latent growth curve analysis. Psychological Methods, 16, 1–16. 





Finney, S. J., & DiStefano, C. (2006). Non-normal and categorical data in structural equation modeling. In G. R. Hancock & R. O. Mueller (Eds.), Structural equation modeling: A second course (pp. 269–314). Greenwich, CT: Information Age. 





Gelman, A., & Rubin, D. B. (1992). Inference from iterative simulation using multiple sequences. Statistical Science, 7, 457–511. 





Geiser, C., Bishop, J., Lockhart, G., Shiffman, S., & Grenard, J. (2013). Analyzing latent state–trait and multiple-indicator latent growth curve models as multilevel structural equation models. Frontiers in Psychology: Quantitative Psychology and Measurement, 4, Article 975. 





Geiser, C., Griffin, D., & Shiffman, S. (2016). Using multigroup–multiphase latent stait–trait models to study treatment-induced changes in intra-individual state variability: An application to smokers’ affect. Frontiers in Psychology. Available at www.frontiersin.org/articles/10.3389/fpsyg2016.01043/full 





Geiser, C., & Lockhart, G. (2012). A comparison of four approaches to account for method effects in latent state trait analyses. Psychological Methods, 17, 255–283. 





Geiser, C., Keller, B. T., & Lockhart, G. (2013). First- versus second-order latent growth curve models: Some insights from latent state–trait theory. Structural Equation Modeling, 20, 479–503. 





Geiser, C., Keller, B. T., Lockhart, G., Eid, M., Cole, D. A., & Koch, T. (2015). 





Distinguishing state variability from trait change in longitudinal data: The role of measurement (non)invariance in latent state–trait analyses. Behavior Research Methods, 47, 172–203. 





Graham, J. W. (2003). Adding missing-data relevant variables to FIML-based structural equation models. Structural Equation Modeling, 10, 80–100. 





Graham, J. W., Taylor, B. J., Olchowski, A. E., & Cumsille, P. E. (2006). Planned missing data designs in psychological research. Psychological Methods, 11, 323–343. 





Guttman, L. (1954). A new approach to factor analysis: The radex. In P. F. Lazarsfeld (Ed.), Mathematical thinking in the social sciences (pp. 258–349). Glencoe, IL: Free Press. 





Hamaker, E. L., Asparouhov, T., Brose, A., Schmiedek, F., & Muthén, B. (2018). At the frontiers of modeling intensive longitudinal data: Dynamic structural equation models for the affective measurements from the COGITO study. Multivariate Behavioral Research, 53, 820–841. 





Heck, R. H., & Thomas, S. L. (2015). An introduction to multilevel modeling techniques: MLM and SEM approaches using Mplus (3rd ed.). New York: Routledge. 





Hu, L., & Bentler, P. M. (1999). Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives. Structural Equation Modeling, 6, 1–55. 





Irwin, H. J., Marks, A. D. G., & Geiser, C. (2018). Belief in the paranormal: A state, or a trait? Journal of Parapsychology, 82, 24–40. 





Jagodzinski, W., Kühnel, S. M., & Schmidt, P. (1987). Is there a “Socratic effect” in nonexperimental panel studies? Consistency of an attitude toward guestworkers. Sociological Methods and Research, 15, 259–302. 





Jöreskog, K. G. (1970). Estimation and testing of simplex models. British Journal of Mathematical and Statistical Psychology, 23, 121–145. 





Jöreskog, K. G. (1971a). Statistical analysis of sets of congeneric tests. Psychometrika, 36, 109–133. 





Jöreskog, K. G. (1971b). Simultaneous factor analysis in several populations. Psychometrika, 36, 409–426. 





Jöreskog, K. G. (1979a). Statistical models and methods for analysis of longitudinal data. In K. G. Jöreskog & D. Sörbom (Eds.), Advances in factor analysis and structural equation models (pp. 129–169). Cambridge, MA: Abt. 





Jöreskog, K. G. (1979b). Statistical estimation of structural models in longitudinal– developmental investigations. In J. R. Nesselroade & P. B. Baltes (Eds.), Longitudinal research in the study of behavior and development (pp. 303–351). New York: Academic Press. 





Jöreskog, K. G., & Sörbom, D. (1981). LISREL V: Analysis of linear structural relationships by the method of maximim likelihood. Chicago: National Educational Resources. 





Kenny, D. A. (1976). An empirical application of confirmatory factor analysis to the multitrait–multimethod matrix. Journal of Experimental Social Psychology, 12, 247–252. 





Kenny, D. A., & Zautra, A. (1995). The trait–state–error model for multiwave data. Journal of Consulting and Clinical Psychology, 63, 52–59. 





Kenny, D. A., & Zautra, A. (2001). Trait–state models for longitudinal data. In L. M. Collins & A. G. Sayer (Eds.), New methods for the analysis of change (pp. 243– 263). Washington, DC: American Psychological Association. 





Kline, R. B. (2016). Principles and practice of structural equation modeling (4th ed.). New York: Guilford Press. 





Kline, R. B. (2020). Becoming a behavioral science researcher: A guide to producing research that matters (2nd ed.). New York: Guilford Press. 





LaGrange, B., & Cole, D. A. (2008). An expansion of the trait–state–occasion model: Accounting for shared method variance. Structural Equation Modeling, 15, 241–271. 





Little, R. J. A., & Rubin, D. B. (2002). Statistical analysis with missing data (2nd ed.). New York: Wiley. 





Little, T. D. (2013). Longitudinal structural equation modeling. New York: Guilford Press. 





Little. T. D., Slegers, D. W., & Card, N. A. (2006). A non-arbitrary method of identifying and scaling latent variables in SEM and MACS models. Structural Equation Modeling, 13, 59–72. 





Lüdtke, O., Robitzsch, A., & Wagner, J. (2018). More stable estimation of the STARTS model: A Bayesian approach using Markov chain Monte Carlo techniques. Psychological Methods, 23, 570–593. 





MacKinnon, D. P. (2008). Introduction to statistical mediation analysis. Mahway, NJ: Erlbaum. 





Marsh, H. W., & Grayson, D. (1994). Longitudinal confirmatory factor analysis: Common, time-specific, item-specific, and residual-error components of variance. Structural Equation Modeling, 1, 116–145. 





McArdle, J. J. (1980). Causal modeling applied to psychonomic systems simulation. Behavior Research Methods and Instrumentation, 12, 193–209. 





McArdle, J. J. (1988). Dynamic but structural equation modeling of repeated measures data. In J. Nesselroade & R. Cattell (Eds.), Handbook of multivariate experimental psychology (2nd ed., pp. 561–614). New York: Plenum Press. 





McArdle, J. J. (2009). Latent variable modeling of differences and changes with longitudinal data. Annual Review of Psychology, 60, 577–605. 





Mehta, P. D., Neale, M. C., & Flay, B. R. (2004). Squeezing interval change from ordinal panel data: Latent growth curves with ordinal outcomes. Psychological Methods, 9, 301–333. 





Meredith, W. (1993). Measurement invariance, factor analysis, and factorial invariance. Psychometrika, 58, 525–543. 





Millsap, R. E. (2011). Statistical approaches to measurement invariance. New York: Routledge. 





Muthén, B. O. (1994). Multilevel covariance structure analysis. Sociological Methods and Research, 22, 376–398. 





Muthén, B. (2010). Bayesian analysis in Mplus: A brief introduction (Version 3). Mplus technical report. Retrieved March 27, 2019 from www.statmodel.com/download/ IntroBayesVersion%203.pdf. 





Muthén, B., & Asparouhov, T. (2002). Latent variable analysis with categorical outcomes: 





Multiple-group and growth modeling in Mplus. Mplus web note. Retrieved October 28, 2019, from www.statmodel.com/download/webnotes/CatMGLong.pdf. 





Muthén, B., & Asparouhov, T. (2012). Bayesian structural equation modeling: A more flexible representation of substantive theory. Psychological Methods, 17, 313–335. 





Muthén, B. O., & Muthén, L. K. (2002). How to use a Monte Carlo study to decide on sample size and determine power. Structural Equation Modeling, 4, 599–620. 





Muthén, L. K., & Muthén, B. O. (1998–2017). Mplus user’s guide (8th ed.). Los Angeles: Muthén & Muthén. 





Paxton, P., Curran, P. J., Bollen, K. A., Kirby, J., & Chen, F. (2001). Monte Carlo experiments: Design and implementation. Structural Equation Modeling, 8, 287– 312. 





Prenoveau, J. M. (2016). Specifying and interpreting latent state–trait models with autoregression: An illustration. Structural Equation Modeling, 23, 731–749. 





Raffalovich, L. E., & Bohrnstedt, G. W. (1987). Common, specific, and error variance components of factor models: Estimation with longitudinal data. Sociological Methods and Research, 15, 385–405. 





Raykov, T. (1993). On estimating true change interrelationships with other variables. Quality and Quantity, 27, 353–370. 





Rubin, D. B. (1976). Inference and missing data. Biometrika, 63, 581–592. 





Rubin, D. B. (1987). Multiple imputation for nonresponse in surveys. New York: Wiley. 





Sayer, A. G., & Cumsille, P. E. (2001). Second-order latent growth models. In L. M. Collins & A. G. Sayer (Eds.), New methods for the analysis of change (pp. 177– 200). Washington, DC American Psychological Association. 





Schafer, J. L., & Graham, J. W. (2002). Missing data: Our view of the state of the art. Psychological Methods, 7, 147–177. 





Schermelleh-Engel, K., Moosbrugger, H., & Müller, H. (2003). Evaluating the fit of structural equation models: Test of significance and descriptive goodness-of-fit measures. Methods of Psychological Research—Online, 8, 23–74. 





Shiffman, S., Stone, A. A., & Hufford, M. (2008). Ecological momentary assessment. Annual Review of Clinical Psychology, 4, 1–32. 





Sörbom, D. (1975). Detection of correlated errors in longitudinal data. British Journal of Mathematical and Statistical Psychology, 28, 138–151. 





Steiger, J. H., & Lind, J. C. (1980, May). Statistically based tests for the number of common factors. Paper presented at the annual meeting of the Psychometric Society, Iowa City, IA. 





Steyer, R. (1989). Models of classical psychometric test theory as stochastic measurement models: Representation, uniqueness, meaningfulness, identifiability, and testability. Methodika, 111, 25–60. 





Steyer, R., Eid, M., & Schwenkmezger, P. (1997). Modeling true intraindividual change: True change as a latent variable. Methods of Psychological Research— Online, 2, 21–33. 





Steyer, R., Ferring, D., & Schmitt, M. J. (1992). States and traits in psychological assessment. European Journal of Psychological Assessment, 8, 79–98. 





Steyer, R., Majcen, A.-M., Schwenkmezger, P., & Buchner, A. (1989). A latent state– trait anxiety model and its application to determine consistency and specificity coefficients. Anxiety Research, 1, 281–299. 





Steyer, R., Mayer, A., Geiser, C., & Cole, D. A. (2015). A theory of states and traits: Revised. Annual Review of Clinical Psychology, 11, 71–98. 





Steyer, R., Partchev, I., & Shanahan, M. (2000). Modeling true intraindividual change in structural equation models: The case of poverty and children’s psychosocial adjustment. In T. D. Little, K. U. Schnabel & J. Baumert (Eds.), Modeling longitudinal and multiple-group data: Practical issues, applied approaches, and specific examples (pp. 109–126). Hillsdale, NJ: Erlbaum. 





Steyer, R., Schmitt, M., & Eid, M. (1999). Latent state–trait theory and research in personality and individual differences. European Journal of Personality, 13, 389–408. 





Steyer, R., & Schmitt, T. (1994). The theory of confounding and its application in causal modeling with latent variables. In A. Von Eye & C. C. Clogg (Eds.), Latent variables analysis: Applications for developmental research (pp. 36–67). Thousand Oaks, CA: Sage. 





Tisak, J., & Tisak, M. S. (2000). Permanency and ephemerality of psychological measures with application to organizational commitment. Psychological Methods, 5, 175–198. 





van de Schoot, R., Kaplan, D., Denissen, J., Asendorpf, J. B., Neyer, F. J., & van Aken, M. A. G. (2014). A gentle introduction to Bayesian analysis: Applications to developmental research. Child Development, 85, 842–860. 





von Oertzen, T., Hertzog, C., Lindenberger, U., & Ghisletta, P. (2010). The effect of multiple indicators on the power to detect interindividual differences in change. British Journal of Mathematical and Statistical Psychology, 63, 627–646. 





Widaman, K. F., & Reise, S. P. (1997). Exploring the measurement invariance of psychological instruments: Applications in the substance use domain. In K. J. Bryant, M. Windle, & S. G. West (Eds.), The science of prevention: Methodological advances from alcohol and substance abuse research (pp. 281–324). Washington, DC: American Psychological Association. 



# Author Index

Note. $f$ or $b$ following a page numbers indicates a figure or a box. 

Aiken, L., 167 

Asparouhov, T., 109, 232, 258, 291 

# B

Bandalos, D. L., 298 

Bentler, P. M., 24b 

Bishop, J., 211, 247 

Bohrnstedt, G. W., 136 

Bollen, K. A., 19b, 24b, 97, 218, 298 

Brose, A., 258 

Buchner, A., 3 

Byrne, B. M., 154 

# C

Card, N. A., 120b 

Chen, F., 218, 298 

Cohen, J., 167 

Cohen, P., 167 

Cole, D. A., 3, 83b, 185b, 211, 226, 227, 308 

Courvoisier, D. S., 211 

Cumsville, P. E., 211, 280 

Curran, P. J., 97, 218, 298 

# D

Duncan, S., 97 

Duncan, T., 97 

# E

Ebner-Priemer, U., 71 

Eid, M., 3, 4, 71, 72b, 112, 136, 140b, 204, 207b, 211, 227, 231, 313 

Enders, C. K., 258, 280, 282, 283, 285, 290, 291, 304, 312 

# F

Ferring, D., 3 

# G

Geiser, C., 3, 105, 144b, 175b, 189, 192, 194b, 208, 211, 247, 316 

Gelman, A., 263 

Graham, J. W., 280, 287, 304 

Grayson, D., 136 

Griffin, D., 208 

Guttman, L., 45 

Meredith, W., 113 

Millsap, R. E., 113 

Moosbrugger, H., 24b, 316 

Müller, H., 24b, 316 

Muthén, B. O., 109, 154, 232, 258, 291, 298, 305, 306, 308 

Muthén, K. L., 308 

Muthén, L. K., 298, 305, 306 

# H

Hamaker, E. L., 232, 258 

Heck, R. H., 235 

Hoffmann, J., 4, 71, 204 

Hu, L., 24b 

Hufford, M., 231 

# O

Olchowski, A. E., 280 

# I

Irwin, H. J., 316 

# P

Partchev, I., 157 

Paxton, P., 218, 298, 308 

Prenoveau, J. M., 185b 

# J

Jöreskog, K. G., 24b, 45, 62, 110, 230 

# R

Raffalovich, L. E., 136 

Reise, S. P., 113, 123b 

Robitzsch, A., 87 

Rubin, D. B., 263, 280, 290, 291 

# K

Keller, B. T., 105 

Kenny, D. A., 69, 72b, 74, 76b, 79, 87, 111, 171 

Kirby, J., 218, 298 

Kline, R. B., 44, 317 

# S

Santangelo, P., 71 

Sayer, A. G., 211 

Schafer, J. L., 280, 304 

Schermelleh-Engel, K., 24b, 316 

Schmiedek, F., 258 

Schmitt, M. J., 3, 185b, 227 

Schneider, C., 136 

Schwenkmezger, P., 3, 136 

Shanahan, M., 157 

Shavelson, R. J., 154 

Shiffman, S., 208, 231, 247 

Slegers, D. W., 120b 

Sörbom, D., 24b, 136, 144b 

Steiger, J. H., 24b 

Steyer, R., 3, 5, 157, 166, 172, 185b, 207b, 209b, 227, 230 

Stone, A. A., 231 

Strycker, L., 97 

# L

LaGrange, B., 185b 

Lind, J. C., 24b 

Lischetzke, T., 211 

Little, T. D., 118, 120b, 124, 280 

Lockhart, G., 105, 144b, 189, 192, 247 

Long, J. S., 24b 

Lüdtke, O., 87 

# M

Majcen, A.-M., 3 

Marks, A. D. G., 316 

Marsh, H. W., 136 

Mayer, A., 3 

McArdle, J. J., 62, 211, 213f 

# T

Taylor, B. J., 280 

Thomas, S. L., 235 

Tisak, J., 211 

Tisak, M. S., 211 

# V

van de Schoot, R., 258 

# W

Wagner, J., 87 

West, S., 167 

Widaman, K. F., 113, 123b 

# Z

Zautra, A., 69, 72b, 74, 76b, 79, 87, 111, 171 

# Subject Index

Note. The letters f, t, or $b$ after a page number indicates a figure, a table, or a box. 

Autoregressive effects 

DSEM modeling of, 257–276 (see also Bayesian analysis; Dynamic structural equation modeling [DSEM]) 

in intensive longitudinal designs, 235 

Autoregressive/cross-lagged (ACL) model, 281, 281f, 286–287, 291–294; see also Latent autoregressive/crosslagged states (LA(C)S) model 

indications for using, 310 

Monte Carlo command and, 298 

path diagram of, 281, 281f 

# B

Bayesian analysis, 258–260 

advantages of, 260, 274–275, 277 

complications of, 275 

description in results report, 314 

disadvantages of, 277 

versus frequentist statistical analysis, 258 

ML estimation and, 259–260, 274, 275, 277 

steps in, 258–260 

Behavior 

current, as predictor of future behavior, 161, 165 (see also Latent autoregressive/cross-lagged states model; Simplex model) 

stability/change in, in simplex model, 53–56, 54b–55b 

# C

Change across time; see also Trait change CTT and, 7b 

factors affecting, 3 

in latent growth curve models with unspecified growth pattern, 101–103 

linear LGC model and, 88, 89f, 90, 91b, 94, 96, 107 

LST-R theory and, 4–6, 14 

ME across time and, 151–152 

ME and, 2, 109–110 

omission in random intercept model, 17, 20b, 21, 21f, 27, 237 

random and fixed intercepts model and, 30, 30f, 32, 34 

simplex model and, 45, 46f, 53–56, 54b–55b, 107 

single-indicator models and, 109 

STMS model and, 174 

$\xi .$ -congeneric model and, 36f, 37, 43 

Chi-square difference test 

nested models and, 123, 124b 

random intercept model and, 23 

simplex model and, 58–60 

Classical test theory (CTT) 

key concepts and definitions in, 7b 

LST-R, 4 

random intercept model and, 18, 21 

and Rel(Yt) coefficient in random intercept model, 22 

situational vacuum in, 4 

tau-congeneric variables in, $\xi .$ -congeneric model and, 35–36 

true score variables in, 6, 7b 

Coefficients 

in CTT, 7b 

in indicator-specific linear growth curve (ISG) model, 215–217 

in latent autoregressive/cross-lagged states (LA(C)S) model, 164 

in latent change score model, 64–65 

in latent state change (LSC) models, 159 

in latent state variables, 13–14 

in latent state-indicator-specific (LS-IS) model, 142–143, 145 

latent state–trait theory revised (LST-R) and, 11, 13–14 

in LST trait-change (LST-TC) model, 208 

in multitrait–multistate (MTMS) model, 195–196 

in singletrait–multistate (STMS) model, 176–177, 177b 

in STMS-IS model, 188–190 

in trait–state–error (TSE) model, 75, 77–79, 85–86 

Cognitive abilities 

latent state model example and, 118–120 

subjective well-being and, 167–170 

Configural measurement equivalence, 123b, 127, 128b, 129, 132t 

Confirmatory factor analysis (CFA) 

latent state model and, 114, 118 

model goodness-of-fit assessment and, 24b 

$\xi$ -Congeneric [O1]model; see $\xi .$ -Congeneric model 

Consistency coefficient, in LST-R theory, 11, 13 

Convergent validity coefficient, of LS-IS model, 142–143 

Correlated uniqueness (CU) approach, to LS-IS model, 144b 

# D

Data, missing; see Missing data handling 

Data collection, MI-LGC models and, 228 

Degrees of freedom, calculation of, $1 9 b$ 

Descriptive statistics, in results report, 315–316 

DSEM modeling of simplex model, 262–274 

Mplus application 

ANALYSIS command, 262 

ANALYSIS: POINT $=$ MEAN, 273 

Bayesian analysis, 272–273 

ESTIMATOR $=$ BAYES command, 262–263 

input file, 262 

with iterative Markov chain Monte Carlo (MCMC) algorithm, 262–263 

MODEL command, 263–264 

parameter autocorrelation plots, 267, 270f 

parameter estimates, 264–265 

parameter trace plots, 266–267, 268f, 269f, 270f, 271f, 272 

Plot View plots, 266 

posterior parameter distributions, 267, 271f, 272 

PSR values and MCMC iteration, 265–266 

rerunning with more MCMC iterations, 272 

STANDARDIZED MODEL RESULTS, 273–274 

TWOLEVEL model, 263–264 

Mplus input file, 262 

summary, 274–276 

Dynamic structural equation modeling (DSEM), 232 

advantages of, 274 

applications of, 257–258 

Dynamic structural equation modeling (cont.) 

Bayesian analysis and, 258–260 

limited research on, 275–276 

Mplus example, 260–274 

# E

Effect sizes, in results report, 316–317 

Estimation problems 

MI-LGC models and, 226 

in results report, 316 

# F

Full information maximum likelihood (FIML), 285; see also Maximum likelihood (ML) estimation 

# G

Gold-standard measure, 119 

h11L4v6z7W3k99rl 

# I

Indicator homogeneity, MI-LGC models and, 226–227 

Indicators, reference versus nonreference, 119–120 

Indicator-specific linear growth curve (ISG) model 

advantages of, 222 

definition based on LST-R theory, 216b 

description of, 212–215 

Mplus application, 217–222 

MODEL CONSTRAINT option, 220–221 

MODEL RESULTS, 219 

MODEL statement, 217–218 

NEW ADDITIONAL parameters, 221 

STANDARDIZED MODEL RESULTS, 220 

trait-changes and, 218–220, 222 

WARNING message, 218 

versus MTMS approach, 212–215 

parameters estimated by, 215 

path diagram of, 214–215, 214f 

summary, 222–223 

variance decomposition and coefficients, 215–217 

Indicator-specific growth (ISG) model as multilevel model, 252–257 

Mplus application 

ANALYSIS statement, 252, 254 

and estimated intraclass correlation coefficients, 255 

MODEL CONSTRAINT option, 255 

MODEL statement, 252, 254 

parameter estimates, 256–257 

TWOLEVEL RANDOM ANALYSIS TYPE, 254 

path diagram of, 253f 

Indicator-specific variance components, 2–3 

Indicator-specificity coefficient, of LS-IS model, 143 

Individual differences, true, versus random measurement error, 3 

Intensive longitudinal data; see also Indicator-specific growth model as multilevel model; Linear latent growth model as multilevel model; Multitrait–multistate (MTMS) model as multilevel model; Random intercept model as multilevel model 

advantages of, 231 

challenges of, 231–232 

ecological momentary assessment example, 231 

longitudinal SEMs for, 235–276 

and long versus wide format, 235 

multilevel approach to, limitations of, 276 

special features of, 232–235 

autoregressive effects, 235 

imbalanced time points, 234 

wide- versus long-format data, 232–234, 233t, 276 

Intraclass correlation coefficients (ICCs), 241–242, 250, 255 

Intraindividual scores, measurement error and, 8 

IQ-score metric, latent state model example and, 118–119 

# L

Latent autoregressive models, 155 

Latent autoregressive/cross-lagged states (LA(C)S) model, 161–171 

autoregressive structure of path diagram of, 162f for predicting future behavior, 161 

cognitive abilities: subjective well-being example and, 167–170 

definition based on LST-R theory, 164b 

versus LAS model, 162–164 

limitations of, 171 

LS and LS-IS models and, 167 

Mplus application, 167–170 MODEL RESULTS, 168–169 MODEL statement, 168 

other features, 165 

path diagram of, 166f 

versus simplex model, 170 

simplex model and, 161, 165 

summary and comparison of, 224t 

TSE model and, 161 

Latent change models, advantages of, 309 

Latent change score model, 62–68 

description of, 63–64 

and interindividual differences in change across time, 68 

interindividual variability in change and, 62, 63f 

limitations of, 68 

Mplus application, 65–68 

MODEL command, 65 

MODEL RESULTS, 67 

STANDARDIZED MODEL RESULTS, 68 

parameter estimates in, 66–67 

path diagram of, 63f 

as reformulation of simplex model, 62, 64 

summary of, 68 

variance decomposition and coefficients in, 64–65 

Latent growth curve (LGC) models, 88–96; see also Linear latent growth curve model 

advantages of, 309 

change across time and, 107, 108 

limitation of, 105 

with unspecified growth pattern, 97–105 average latent growth curve, 103–104, 103f 

and change across time, 101–103, 105 

change across time and, 107 

definition using LST-R theory, 99b 

description of, 97–100, 97f 

MODEL command, 100 

MODEL CONSTRAINT option, 102, 104 

MODEL RESULTS, 101 

Mplus application, 100–104 

parameters estimated by, 98, 100, 102–103 

STANDARD MODEL RESULTS, 104 

Latent state, defined, 9 

Latent state (LS) model, 113–154 

advantage of, as first step, 114 

assumptions of, 121b–122b 

available information and degrees of freedom, 116, 117b 

change across time and, 125, 126–134 

congeneric measurement structure in, 118 

definition based on LST-R theory, 120 

description of, 114–116 

as extension of confirmatory factor analysis, 114 

flexibility of, 115 

homogeneous indicator assumption of versus LS-IS indicator-specific assumptions, 152 

uses of, 152 

with indicator-specific residual factors, 136–151 (see also Latent stateindicator-specific (LS-IS) model) 

limitations of, 135 

Mplus application, 126–134 

configural ME model and, 127, 128b, 129, 132t 

mean structure analysis in, 128b 

MODEL command, 126 

MODEL RESULTS, 127 

STANDARDIZED MODEL RESULTS, 130 

strict ME model and, 132–133, 132t 

strong ME model and, 128b, 132–133, 132t 

unstandardized model results, 129–130 

weak ME model and, 131–132, 132t 

Latent state (LS) model (cont.) 

multiconstruct extension of, 165–166, 166f 

other features of, 125 

parameters estimated by, 115–116 

path diagram of, 115f 

scale setting and, 116, 118–120 

simplex model and, 115 

special cases of, 155 

as starting point for longitudinal analysis, 308 

summary and comparison of, 224t 

and testing ME across time, 122–125 

uses of, 135, 152 

variables of, 121b–122b alternative method of defining, $1 2 0 b$ correlated versus uncorrelated, 125 measurement of, 118–120 

variance decomposition and reliability coefficient, 120 

Latent state change score (LSC) models, 155, 156–161 

advantages of, 160 

baseline change version of, 157 

limitations of, 160–161 

LS/LS-IS parameters and, 158–159 

LS/LS-IS models and, 159 

Mplus application, 160 

neighbor change version of, 157–158 

parameters estimated by, 159 

path diagram of, 158f 

simplex model and, 160 

variance decomposition and coefficients, 159 

Latent state change/indicator-specific factors (LSC-IS) model, summary and comparison of, 224t 

Latent state indicator-specific (LS-IS) model, as starting point for longitudinal analysis, 308 

Latent state variables 

coefficients for, 13–14 

in simplex model, 46–47 

Latent state-indicator-specific (LS-IS) model, xx 

applications of, 151 

and choice of reference indicator, 136, 139 

correlated errors alternative to, 144b 

definition based on LST-R theory, 140b–141b 

description of, 136–142 

effects in longitudinal data, 137b 

LST-R theory and, 136 

measurement equation in, 157 

MODEL command, 145–146 

MODEL CONSTRAINT option, 149–150 

MODEL RESULTS, 150–151 

Mplus application, 145–151 

parameters estimated by, 139, 141–142 

path diagram of, 138, 138f 

providing user-defined starting values and, 147b 

strict ME across time and, 145 

summary and comparison of, 224t 

unstandardized versus standardized parameter estimates and, 146, 148–149 

variance decomposition and coefficients, 142–143, 145 

Latent state–trait (LST) models, 155, 171–186; see also LST trait-change (LST-TC) model; Singletrait– multistate (STMS) model 

advantages of, 309–310 

multiple indicator, advantages of, 171–172 

sample description for results report, 313–314 

Latent state–trait theory (LST), 2, 3–14 origins of, 3 

and true individual differences versus random measurement error, 3 

$\xi .$ -congeneric model defined by, 37b 

Latent state–trait theory, revised (LST-R) assumptions of, 16 

basic idea, 3–5 

changes from classical version, 3 

versus classical test theory, 4 

coefficients and, 11, 13–14 

coefficients in, 11, 13–14 

decomposition in path diagram, 9–10, 10f 

decomposition of, 14–15 

functions of, 14–15 

fundamental concepts of, 4–5 

and individual changes over time, 14 

latent variables defined by, 6 

latent variables in, properties of, 10–11, 12b–13b 

person $\times$ situation interactions and, 4 

properties of latent variables, 10–11, 12b 

simplex model defined by, 48b–50b 

situation concept in, 5–6 

situational influences and, 4 

and steps in random experiment, 5 

trait–state–error model and, 72b–74b 

variables in, 5–6, 8–10 

Latent trait variables, 14 

Latent trait-change models, 155, 202–223 

focus of, 202 

versus LS, LSC, LAS/LACS models, 203 

and LST models with autoregression, 202 

trait changes versus short-term state fluctuations, 202–203 

Latent variable scores, as means of intraindividual score distribution, 8 

Latent variables, 14 

and change across time, 10 

components of, 10, 10f 

defined, 2, 16 

in LST-R theory, properties of, 10–11, 12b–13b 

types classified as, 14 

Linear latent growth curve model, 88–96 

change across time and, 88, 89f, 90, 91b, 94, 96, 107, 108 

and definition based on LST-R theory, 91b 

description of, 88–90 

linear trait-change factor in, 88 

Mplus application, 92–96 

graph of estimated intercept and slope factor, 95f 

MODEL command, 92 

MODEL RESULTS, 94 

PLOT command, 92, 93f, 94 

STANDARDIZED MODEL RESULTS, 96 

true change scores and, 94 

path diagram of, 89f 

possible model-implied trait-change patterns in, 89f 

versus random intercept model, 96 

restrictive assumptions of, 97 

summary of, 96 

and trait changes over time, interindividual differences, 96 

and variance decomposition and reliability coefficient, 90–91 

Linear latent growth model as multilevel model, 243–247 

ANALYSIS type, TWOLEVEL RANDOM, 245 

downside of, 246 

BETWEEN level, 246–247 

MODEL RESULTS, 246 

MODEL statement, 245 

wide-versus long-format versions, 243, 244f, 245 

Long-format data, versus wide-format data, 232–233, 233t 

Longitudinal data analysis 

correcting for measurement error in, 2 latent variables in, 2 

measurement equivalence across time and, 2 

Longitudinal measurement models, simplifying restrictions of, 16 

Longitudinal models, choosing, 307–310 

Longitudinal studies 

missing scores in (see Missing data handling) 

variable-specific or method effects in, 2–3 

LST trait-change (LST-TC) model, 204–212 

definition based on LST-R theory, 207b 

description of, 204, 205f, 206–207 

key idea of, 211 

limitations of, 211–212 

Mplus application, 208–211 

alternative equivalent formulations, 209b 

autoregressive alternative, 205f, 209b 

MODEL commands, 208, 210 

MODEL CONSTRAINT option, 210 

MODEL RESULTS, 210 

trait-change variable alternative, 209b 

parameters estimated by, 206–207 

path diagrams of, 204, 205f 

STMS measurement approach and, 211 

STMS model and, 206 

summary and comparison of, 224t 

summary of, 211–212 

variance decomposition and coefficients, 208 

# M

Markov chain Monte Carlo (MCMC) 

algorithm, 274 

in DSEM modeling of simplex, 262–263, 265–266 

Maximum likelihood (ML) estimation, 280, 285–290 

ACL model and, 286–287 

Bayesian analysis and, 259–260, 274, 275, 277 

DSEM approach and, 274 

missing data and, 285 

Mplus application, 281f, 286–290 

COVARIANCE COVERAGE, 288–289 

MISSING subcommand, 286 

MODEL command, 287 

OUTPUT command, 287 

STANDARDIZED RESULTS, 289 

VARIABLE command, 286 

sample size and, 275 

as state of art method, 284–285 

Measurement equivalence (ME) 

across time, omission in single-indicator models, 109 

change across time and, 2, 134–135 

levels of, 122–125, 123b, 127, 128b, 129, 131–133, 132t 

and meaningful interpretation of change across time, 151–152 

MI-LGC models and, 226 

omission of testing in single-indicator models, 113 

as prerequisite for across-time comparisons, 113 

testing of, 152, 155 

violations of, 152 

Measurement error 

correcting, in longitudinal data analysis, 2 

in CTT, 7b 

LST theory and, 14 

measurement theory and, 1–2 

variables representing, 14 

Measurement error variances, in simplex 

model, 50–51, 51b 

Measurement theory 

functions of, 1–3, 14 

method factor definition and, 2–3 

Measures, in results report, 312–313 

Method-specific variance components, 2–3 

Missing at random (MAR) mechanism, 282–283 

ML estimation and, 285 

Missing completely at random (MCAR) mechanism, 281–282 

ML estimation and, 285 

Missing data handling, 279–306; see also Maximum likelihood (ML) estimation; Multiple imputation (MI) estimation; Planned missing data designs 

full information maximum likelihood (FIML) estimation and, 285 

mechanisms of, 280–285 

missing at random, 282–283 

missing completely at random, 281–282 

missing not at random, 283–285 

methods for, 279–280 

Missing not at random (MNAR) mechanism, 283–285 

Missingness 

MAR data and, 303–304 

MCAR data and, 303 

MNAR data and, 304 

planned missing data designs and, 304–305 

Model description, in results report, 313–314 

Model fit information, in results report, 316 

Monte Carlo simulation, 280 

with MI estimation, 298–303 

as small sample solution, 308–309 

Mplus; see also Mplus application and specific commands and statements under specific models 

and endogenous versus exogenous variables, 54b–55b 

MODEL CONSTRAINT option in, $4 0 b$ 

MODEL FIT INFORMATION in, 41–42 

MODEL statement for random intercept model, 22–23 

MODEL TEST option in, 40b, 41 

providing user-defined starting values in, 147b 

VARIABLE command, example of, $1 0 9 b$ 

Multifactor longitudinal models; see also Latent growth curve (LGC) models; Simplex model; Trait–state–error (TSE) model 

limitations of, 108 

and limitations of single-factor models, 107 

additional latent factors in, 45 

latent change score model, 62–68 

latent growth curve model, 88–96 

LGC model with unspecified growth pattern, 97–105 

simplex model, 45–62 

trait–state–error model, 69–87 

Multi-indicator models 

advantages of, 171–172 

ME testing and, 113–114 

Multiple imputation (MI) estimation, 285, 290–296 

advantages and disadvantages of, 296 

Mplus application, 286, 291–295, 293f 

ANALYSIS summary, 294 

DATA command, 293 

example, 291–292 

sample statistics, 294–295 

as state of art method, 284–285 

summary, 296 

Multiple-indicator latent growth curve (MI-LGC) models, 155, 212–223; see also Indicator-specific linear growth curve (ISG) model 

advantages of, 223, 226–228 

autoregressive effects and, 227 

and detection of interindividual differences, 227 

limitations of, 228–229 

model identification and df, 223 

and separation of trait, trait-change, state residual, ME components, 228 

simplex model, 223 

versus single-indicator latent growth curve models, 212, 213f 

versus TSE model, 223 

variance decomposition and coefficients, 215 

Multiple-indicator longitudinal models, 155–230; see also Latent 

autoregressive/cross-lagged states 

model; Latent state change models; 

Latent trait-change models; 

Multitrait–multistate (MTMS) model 

advantages of, 156 

Multiple-indicator models 

advantages over single-indicator models, 307 

measurement design requirements for, 308 

Multitrait–multistate (MTMS) model, 192–202 

advantages of, 201–202 

with autoregression, 200b 

path diagram of, 203f 

definition based on LST-R theory, 194b 

description of, 192–195 

LST model and, 192 

Mplus application, 196–201 

MODEL CONSTRAINT option, 200–201 

MODEL CONSTRAINT statement, 197 

MODEL RESULTS, 198–199 

MODEL statement, 196–197 

STMS model and, 199 

STMS-IS model and, 197–198, 199 

WARNING message, 202 

parameters estimated by, 193, 195 

path diagram of, 193f 

summary, 201 

variance decomposition and coefficients, 195–196 

Multitrait–multistate (MTMS) model as multilevel model, 247–252 

ANALYSIS, 249 

chi-square test of, 250 

intraclass correlation coefficients and, 250 

WITHIN and BETWEEN levels, 251 

MODEL statement, 249 

Mplus parameter estimates for, 250–251 

versus single-indicator model, 247, 248f 

versus single-indicator random intercept model, 250 

wide-to-long transformation, 248f, 249 

Multitrait–multistate (MTMS) models, 

summary and comparison of, 224t 

# O

Ordered categorical observed variables, 109b 

# P

Parameter estimates; see also under specific models 

in results report, 317, 318t, 319t 

Parameter trace plots, 266–267, 268f, 269f, 270f, 271f, 272 

Path diagrams; see also under specific models 

value of, 313 

Planned missing data designs, 296–303 

example, 297t 

Mplus analysis and simulations, 297–303 

Monte Carlo simulation and, 298–303 

Potential scale reduction (PSR) values, 265–266 

# R

Random and fixed intercepts model, 28–34 

and absence of changes across time, 28 

and assumption of no individual differences in trait change, 33 

assumptions of, 31b 

defined on LST-R theory, 31b 

description of, 28–32, 29f 

mean structure and, 28–29, 28b 

measurement occasions required by, 43–44 

MODEL command for, 32–33 

MODEL RESULTS, 33 

Mplus commands for, 32–33 

parameters estimated by, 30 

path diagram of, 29f 

restrictive change process in, 34 

summary and comparison of, 106t 

summary of, 43 

trait-change patterns and, 30, 30f, 32, 34 

TSE model and, 71 

variance decomposition and reliability coefficient in, 32 

Random intercept model, 10 

assumptions of, 17 

as baseline model, 27, 309 

CFA version of, 237–238 

versus CTT, 18, 21 

definition based on LST-R theory, 20b 

description of, 17–18, 21 

limitations of, 27, 44 

measurement occasions required by, 43 

Mplus application, 22–23, 25–26 

MODEL command, 22–23 

MODEL FIT INFORMATION, 23, 24b 

MODEL RESULTS, 25–26 

OUTPUT, 23 

and omission of change across time, 17, 20b, 21, 21f, 27 

parameters estimated by, 18 

path diagram of, 17, 18f 

possible model-implied trait scores in, 21, 21f 

single-factor models, 17–27 

standardized solution for, 26 

summary and comparison of, 106t 

summary of, 43 

unstandardized solution for, 26 

useful purposes of, 21 

variance decomposition, reliability coefficient in, 21–22 

Random intercept model as multilevel model, 235–243 

baseline use of, 236 

hierarchical two-level structure of, 236–237 

Mplus application 

ANALYSIS option, 239–240 

and chi-square test, 242 

DATA WIDETOLONG command, 239 

intraclass correlation coefficient (ICC) and, 241–242 

WITHIN and BETWEEN LEVELS, 239–240, 242–243 

OUTPUT option, 240–241 

parameters estimated by, 242–243 

and omission of trait change across time, 236f, 237 

versus as single-indicator model, 235, 236f 

and wide-to-long data transformation in Mplus, 236f, 238b–239b 

Random measurement error, 14 

Reference indicator, selecting, 119, 186 

Reliability, LST-R definition of, 75 

Reporting results, 310–320 

general recommendations, 310–311 

methods section, 311–314 

Open Science Forum repository and, 311 

results section, 315–320 

# S

Sample information, in results report, 312 

Simplex model, 45–62 

assessing stability and change in, 53–56, 54b–55b 

autoregressive features, 46–47, 46f, 56, 59, 61–62, 69, 257 

change across time and, 45, 46f, 53–56, 54b–55b, 107 

definition based on LST-R theory, 48b–50b 

description of, 46–51 

diagram of, 45, 46f 

direct versus indirect variable effects in, 61b, 62 

DSEM application, 262–274 (see also DSEM modeling of simplex model) 

equal state residual factor variances and, 57b 

extension of, 62 

free parameters in, 50–51 

limitations of, 69, 107 

long-format model of, 260, 261f, 262–274 

LST variable decomposition and, 46–47 

measure error variances in, 50–51, 51b 

measurement and structural equations for, 46–47 

versus MI-LGC models, 56–62, 223 

Mplus application, 56–62 

MODEL command, 56 

MODEL CONSTRAINT option and, 56–59 

MODEL RESULTS, 58–59 

MODEL TEST, 58 

NEW ADDITIONAL PARAMETERS, 59–60 

STANDARDIZED MODEL RESULTS, 60 

Wald test of parameter constraints, 59 

occasion-specificity coefficient in, 52–53 

and omission of interindividual variability, 62 

parameters of, 47 

rank-order changes in, 45, 46f 

reliability coefficient in, 52 

and resolution of single-factor issues, 62 

restrictive assumptions of, 156 

versus single-factor models, 52 

standardized parameter estimates for, 60–61 

state residual versus measurement error variances in, 50–51, 51b 

summary and comparison of, 106t 

time points in, 47 

trait variable decomposition in, 48b–50b 

variance decomposition and coefficients in, 51–53 

variances in, 47, 50 

wide-format model of, 260, 261f 

Single-factor models, 16–44; see also Random and fixed intercepts model; Random intercept model 

common features and advantages of, 43–44 

as first-step choice, 309 

limitations of, 69 

random and fixed intercepts model, 28–34 

random intercept model, 17–27 

$\xi$ -congeneric model, 34–43 (see also $\xi$ -Congeneric model) 

Single-indicator data 

defined, 17 

multifactor longitudinal models for (see Multifactor longitudinal models) 

single-factor models for, 16–44 (see Single-factor models) 

Single-indicator models 

applications of, 113 

change across time and, 109 

estimation problems and, 226 

information, degrees of freedom, model identification in, 19b 

limitations of, 109, 113, 152, 155–156 

problems with, 171–172 

summary and comparison of, 106t 

Singletrait–multistate (STMS) model, 172–192 

and change across time, 174 

definition based on LST-R theory, 175b 

description of, 172–175 

with indicator-specific residual factors (STMS-IS), 186–192 

definition based on LST-R theory, 188b 

description of, 186–188 

LS-IS and, 186, 191 

MODEL command, 190 

MODEL CONSTRAINT, 190 

MODEL RESULTS, 190–191 

Mplus application, 190–191 

parameters estimated by, 187–188 

versus STMS model, 189 

summary, 191–192 

versus LAS model, 184 

latent state model and, 172–173 

limitations of, 185–186 

LS model and, 184 

Mplus application, 176–184 

MODEL CONSTRAINT option, 176–178, 182–183 

MODEL statement, 178 

STANDARDIZED MODEL RESULTS, 180–182 

parameters estimated by, 174–175 

path diagram of, 173f, 212, 213f 

specifying as bifactor model, 179b–180b 

summary, 184–186 

summary and comparison of, 224t 

trait-like versus state-like constructs and, 176 

variable decomposition in, 173 

variance decomposition and coefficients, 176–177, 177b 

without versus with autoregressive effects, 185b 

Situation and/or person $\times$ situation variables, 14 

Situation consistency coefficient, in TSE model, 78 

Situation variables, in LST-R, 6 

Situational influences, single-factor models and, 44 

Social sciences, random measurement error in, 1–2 

Standard errors, in results report, 317, 318t 

State residual latent variables, single-factor models and, 69 

Statistical significance, tests of, in results report, 316–317 

Strict measurement equivalence, 123b, 132–133, 132t 

LS-IS model and, 145 

Strong measurement equivalence, 123b, 128b, 132–133, 132t 

Structural equation modeling (SEM); see also Autoregressive effects, DSEM modeling of; Dynamic structural equation modeling (DSEM) 

downside of, 257 

endogenous versus exogenous variables in, 54b–55b 

latent state model and, 118 

model goodness-of-fit assessment and, 24b 

wide-format, single-level, contraindications to, 276–277 

# T

Trait change; see also Change across time versus short-term state fluctuations, 202–203 

Trait variables, decomposition in simplex model, 48b–49b 

Trait–state–error (TSE) model, 69–87 

applications recommendations for, 87 

autoregressive structure of, 69–71, 73b, 74, 78, 80, 82, 83b, 87 

coefficients in, 77–79 

computing coefficients for, 85–86 

MODEL CONSTRAINT option, 85 

MODEL RESULTS option, 86 

definition based on LST-R theory, 72b–74b 

description of, 69–75 

and estimation of free parameters, 74–75 

estimation problems and bias in, 83b 

key advantages of, 86–87 

latent state variables in, 75, 77 

latent variables in, 107 

limitations of, 87, 108 

LST-R reliability definition and, 75 

mean structure in, 75, 76b 

measured variable variance in, 77 

measurement occasions required in, 71, 74 

measurement portion of, 69 

versus MI-LGC models, 223 

Mplus application, 79–87 

MODEL command, 79, 81 

MODEL CONSTRAINT option, 79, 80 

MODEL RESULTS option, 81–82 

STANDARDIZED MODEL RESULTS, 84 

path diagram of, 69, 70f 

restrictive assumptions of, 156 

simplifying restrictions for, 71, 74 

small sample problems with, 308 

structural (latent variable) portion of, 70–71 

summary, 86–87 

variance decomposition and coefficients in, 75, 77–79 

# V

Variables 

endogenous versus exogenous, 54b–55b 

and errors of measurement, 14 

in LST-R theory, 5–6, 8–10 

observed variables, 5–6 

person and situation, 6 

ordered categorical observed, 109b 

Variance components, method- or indicator-specific, 2–3 

Variance decomposition 

of indicator-specific linear growth curve (ISG) model, 215–217 

in latent change score model, 64–65 

in latent growth curve models with unspecified growth pattern, 100 

in latent state change (LSC) models, 159 

in latent state (LS) model, 120 

in latent state-indicator-specific (LS-IS) model, 142–143, 145 

in linear latent growth curve model, 90–91 

in LST trait-change (LST-TC) model, 208 

in multitrait–multistate (MTMS) model, 195–196 

in random and fixed intercepts model, 32 

in random intercept model, 21–22 

in simplex model, 51–53 

in singletrait–multistate (STMS) model, 176–177, 177b 

in STMS-IS model, 188–190 

in trait–state–error (TSE) model, 75, 77–79 

in $\xi$ -congeneric model, 38 

# W

Wald test 

simplex model and, 59–60 

$\xi$ -congeneric model and, 41, 41b, 42 

Weak measurement equivalence, 123b, 131–132, 132t 

Wide-format data, versus long-format data, 232–233, 233t, 276 

# Z

$\xi$ -Congeneric model, 34–43 

change patterns permitted by, 36f, 37 

definition based on LST theory, 37b 

description of, 35–37 

and interindividual differences in trait changes, 43 

Mplus application, 38–42 

MODEL command, 38 

MODEL CONSTRAINT option, 39 

MODEL RESULTS, 38–39 

MODEL TEST option, 39 

parameters estimated by, 36 

path diagram of, 35f 

summary and comparison of, 106t 

tau-congeneric variables in CTT and, 35–36 

variance decomposition and reliability coefficient, 38 

# About the Author

Christian Geiser, PhD, is Professor of Psychology at Utah State University and Director of the Quantitative Psychology PhD Specialization. His research interests are in psychometrics and structural equation modeling, particularly in longitudinal data analysis and multitrait–multimethod modeling. As part of his methodological work, he has presented new longitudinal structural equation modeling approaches for examining effects of situations and person–situation interactions, as well as models for integrating information from multiple reporters or other methods in longitudinal analyses. 