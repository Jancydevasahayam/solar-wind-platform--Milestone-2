import React, { useEffect, useState } from "react";
import API from "../services/api";
import SiteMap from "./SiteMap";

import {
  Container,
  Grid,
  Card,
  CardContent,
  Typography
} from "@mui/material";

import WbSunnyIcon from "@mui/icons-material/WbSunny";
import AirIcon from "@mui/icons-material/Air";
import PlaceIcon from "@mui/icons-material/Place";
import RecommendIcon from "@mui/icons-material/Recommend";

function Dashboard() {
  const [site, setSite] = useState(null);

  useEffect(() => {
    API.get("/dashboard/site/2")
      .then((res) => setSite(res.data))
      .catch((err) => console.error(err));
  }, []);

  if (!site) return <h2>Loading...</h2>;

  return (
    <Container sx={{ mt: 4 }}>
      <Typography variant="h3" align="center" gutterBottom>
        Solar & Wind Deployment Intelligence Platform
      </Typography>

      <Grid container spacing={3}>

        <Grid item xs={12} md={3}>
          <Card>
            <CardContent>
              <PlaceIcon color="primary" />
              <Typography variant="h6">Latitude</Typography>
              <Typography>{site.location.latitude}</Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={3}>
          <Card>
            <CardContent>
              <PlaceIcon color="secondary" />
              <Typography variant="h6">Longitude</Typography>
              <Typography>{site.location.longitude}</Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={3}>
          <Card>
            <CardContent>
              <WbSunnyIcon color="warning" />
              <Typography variant="h6">Solar</Typography>
              <Typography>
                {site.assessment.solar_potential}
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={3}>
          <Card>
            <CardContent>
              <AirIcon color="success" />
              <Typography variant="h6">Wind</Typography>
              <Typography>
                {site.assessment.wind_potential}
              </Typography>
            </CardContent>
          </Card>
        </Grid>

      </Grid>

      <br />

      <Card>
        <CardContent>
          <Typography variant="h5">
            Site Location
          </Typography>

          <SiteMap
            latitude={site.location.latitude}
            longitude={site.location.longitude}
          />
        </CardContent>
      </Card>

      <br />

      <Card>
        <CardContent>

          <RecommendIcon color="primary" />

          <Typography variant="h5">
            Recommendation
          </Typography>

          <Typography variant="h6">
            {site.assessment.recommendation}
          </Typography>

        </CardContent>
      </Card>

    </Container>
  );
}

export default Dashboard;