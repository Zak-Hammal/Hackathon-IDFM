// HomeScreen.js
import { useRouter } from "expo-router";
import React, { useState } from 'react';
import {
  Dimensions,
  Image,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View
} from 'react-native';

const { width: SCREEN_WIDTH, height: SCREEN_HEIGHT } = Dimensions.get('window');

const HomeScreen = () => {
  const [searchQuery, setSearchQuery] = useState('');

const router = useRouter();

const handleSearch = () => {
  if (searchQuery.trim()) {
    router.push("/ItineraryScreen")
  }
};

  // Données des trajets quotidiens (à remplacer par les données du backend)
  const dailyRoutes = [
    {
      id: 1,
      title: 'Vers le travail',
      isRecommended: true,
      duration: '15 min',
      transport: [
        { type: 'bus', number: '43', color: '#E3051B' },
        { type: 'walk', duration: '07' },
      ],
      details: '3, 7, 14 min de Saint Georges-Châteaudun',
      trafficAlert: false,
    },
    {
      id: 2,
      title: 'Vers le travail',
      isRecommended: false,
      duration: '16 min',
      transport: [
        { type: 'walk', duration: '05' },
        { type: 'rer', number: 'RER' },
        { type: 'metro', number: '12', color: '#007A3E' },
        { type: 'walk', duration: '09' },
      ],
      details: '3, 7, 14 min de Trinité',
      trafficAlert: true,
      trafficMessage: 'Une info trafic concerne ce trajet',
    },
    {
      id: 3,
      title: 'Vers la maison',
      isRecommended: false,
      duration: '15 min',
      transport: [
        { type: 'walk', duration: '07' },
        { type: 'bus', number: '43', color: '#E3051B' },
      ],
      details: '3, 7, 14 min de Trinité',
      trafficAlert: false,
    },
    {
      id: 4,
      title: 'Vers la maison',
      isRecommended: false,
      duration: '16 min',
      transport: [
        { type: 'walk', duration: '09' },
        { type: 'metro', number: 'M', color: '#000000' },
        { type: 'metro', number: '12', color: '#007A3E' },
        { type: 'walk', duration: '05' },
      ],
      details: '3, 7, 14 min de Trinité - d\'Estienne d\'Orves',
      trafficAlert: false,
    },
  ];

  const savedPlaces = [
    {
      id: 1,
      icon: require('../../assets/images/adrMaison.png'),
      title: 'Maison',
      address: '33 Rue La Fayette, Paris 9e arrondissemen...',
    },
    {
      id: 2,
      icon: require('../../assets/images/adrTravail.png'),
      title: 'Travail',
      address: '11 Rue de Milan, Paris 9e arrondissemen...',
    },
    {
      id: 3,
      icon: require('../../assets/images/adrFavoris.png'),
      title: 'Favori',
      rightButton: 'Définir',
    },
  ];

  return (
    <View style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor="transparent" translucent />
      
      {/* Background Map */}
      <Image
        source={require('../../assets/images/maps.png')}
        style={styles.mapBackground}
        resizeMode="cover"
      />

      {/* Top Action Buttons */}
      <View style={styles.topButtons}>
        <TouchableOpacity style={styles.actionButton}>
          <Image
            source={require('../../assets/images/signalerAffluance.png')}
          />
        </TouchableOpacity>
        <TouchableOpacity style={styles.actionButton}>
          <Image
            source={require('../../assets/images/contactUrgence.png')}
          />
        </TouchableOpacity>
      </View>

      {/* Blue Content Panel */}
      <View style={styles.contentPanel}>
        {/* Search Bar */}
        <TouchableOpacity 
          style={styles.searchContainer}
          onPress={() => navigation.navigate('ItineraryScreen')}
        >
          <View style={styles.searchIconContainer}>
            <Text style={styles.searchIcon}>🔍</Text>
          </View>
          <TextInput
            style={styles.searchInput}
            placeholder="Rechercher un itinéraire"
            placeholderTextColor="#666"
            value={searchQuery}
            onChangeText={setSearchQuery}
            onSubmitEditing={handleSearch}
            returnKeyType="search"
            editable={true}
          />
        </TouchableOpacity>

        {/* IDFM Logo */}
        <Image
          source={require('../../assets/images/logoIDFM.png')}
          style={styles.logo}
          resizeMode="contain"
        />

        <ScrollView 
          style={styles.scrollContent}
          showsVerticalScrollIndicator={false}
        >
          {/* Où allons-nous ? Section */}
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>Où allons-nous ?</Text>
            
            <View style={styles.placesContainer}>
              {savedPlaces.map((place) => (
                <TouchableOpacity key={place.id} style={styles.placeItem}>
                      <Image 
                        source={place.icon}
                       
                      />
                </TouchableOpacity>
              ))}
            </View>
          </View>

          {/* Trajets quotidiens Section */}
          <View style={styles.section}>
           
                <Text style={styles.sectionTitle}>Trajets quotidiens</Text>
                <Image
                  source={require('../../assets/images/trajets.png')}
                />
           

          </View>


        </ScrollView>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FFFFFF',
  },
  mapBackground: {
    position: 'absolute',
    width: SCREEN_WIDTH,
    height: SCREEN_HEIGHT * 0.3,
    top: 0,
    left: 0,
  },
  topButtons: {
    position: 'absolute',
    top: 120,
    right: 16,
    flexDirection: 'row',
    gap: 50,
    zIndex: 10,
  },
  actionButton: {
    width: 56,
    height: 56,
    borderRadius: 28,
    backgroundColor: '#FFFFFF',
    justifyContent: 'center',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  actionButtonImage: {
    width: 40,
    height: 40,
  },
  contentPanel: {
    //position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
    width: SCREEN_WIDTH,
    height: SCREEN_HEIGHT * 0.85,
    borderTopLeftRadius: 16,
    borderTopRightRadius: 16,
    backgroundColor: '#77B3F1',
    marginTop: 200,
    paddingTop: 16,
  },
  searchContainer: {
    width: SCREEN_WIDTH - 25,
    height: 46,
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    borderRadius: 23,
    marginHorizontal: 12.5,
    paddingHorizontal: 16,
    marginBottom: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.1,
    shadowRadius: 2,
    elevation: 2,
  },
  searchIconContainer: {
    marginRight: 8,
  },
  searchIcon: {
    fontSize: 20,
  },
  searchInput: {
    flex: 1,
    fontSize: 16,
    color: '#000',
  },
  logo: {
    width: 120,
    height: 40,
    alignSelf: 'flex-end',
    marginRight: 16,
    marginBottom: 8,
  },
  scrollContent: {
    flex: 1,
    marginBottom:106,
  },
  section: {
    paddingHorizontal: 16,
    marginBottom: 24,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#FFFFFF',
    marginBottom: 12,
  },
  sectionHeader: {
    flexDirection: 'column',
    alignItems: 'center',
    marginBottom: 12,
  },
  trajetsIconContainer: {
    width: 32,
    height: 32,
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 8,
  },
  trajetsIcon: {
    width: 20,
    height: 20,
  },
  placesContainer: {
    padding: 12,
    flexDirection: 'column',
    gap: 6,
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
  },
  placeItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingVertical: 12,
  },

});

export default HomeScreen;